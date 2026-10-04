from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Region
from .ItemLocationClasses import ModdedCelesteLocation
from .ValidateLayout import validate
from .constants import Constants
from worlds.generic.Rules import set_rule
from .level_logic.LogicalLayout import levelList
from .level_logic.LogicalObjects import Level, Room, Location
from .constants.ItemNames import ItemName, filler, mechanic, strawberry, moon_berry, level_victory
from .constants.LevelNames import LevelName, LevelCategory
from .constants.LocationTypes import LocationType
from .constants.ItemTypes import ItemType
from .Naming import getCheckpointName, getKeyDoorName, getLocationName, getRoomName, getStartLocationName
from .level_logic.LogicalLayout import levelList
from .level_logic.LogicalObjects import Level

levelList: dict[LevelName, Level]

def levelUnlock(levelName: LevelName):
    return f"Level Unlock: {levelName}{f" ({levelList[levelName].level_category})" if levelList[levelName].level_category not in {LevelCategory.A_SIDE, LevelCategory.B_SIDE, LevelCategory.C_SIDE, LevelCategory.FAREWELL} else ""}"

if TYPE_CHECKING:
    from . import CelesteModdedWorld

levelList: dict[str, Level]

def mapItemList(items: list[list[str]], world: "CelesteModdedWorld"):
    item_map = world.consolidation_mapping
    mapped_list = []
    for itemList in items:
        mapped_sublist = []
        for item in itemList:
            if item in item_map.keys():
                for mapping_result in item_map[item]:
                    mapped_sublist.append(mapping_result)
            else:
                mapped_sublist.append(item)
        mapped_list.append(mapped_sublist)

    return mapped_list

def hasNCrystalHearts(n: int, state: CollectionState, world: "CelesteModdedWorld"):
    count = 0
    for itemName in state.prog_items[world.player]:
        if item_type_dict[itemName] == ItemType.CRYSTAL_HEART_VANILLA:
            count += 1
    return count >= n or world.options.open_heart_gates.value

def ruleFromList(items: list[list[str]], world):

    mapped_items = mapItemList(items, world)
    
    def returnRule(state: CollectionState, items=mapped_items, world=world):
        if not items:
            return True
        result = True
        for andItems in items:
            result = True
            for item in andItems:
                item: str
                if item.startswith("#"):
                    req_hearts = int(item.replace("#", ""))
                    if not hasNCrystalHearts(req_hearts, state, world):
                        result = False
                elif not state.has(item, world.player):
                    result = False
            if not result:
                continue
            else:
                return True
        return result
    return returnRule

def ruleFromListPlusCondition(items: list[list[str]], extraItem: str, world: "CelesteModdedWorld"):

    list_rule = ruleFromList(items, world)

    mapped_extra_items = []
    if extraItem in world.consolidation_mapping.keys():
        mapped_extra_items = world.consolidation_mapping[extraItem]
    else:
        mapped_extra_items = [extraItem]
    
    def returnRule(state: CollectionState, extraItems=mapped_extra_items, list_rule=list_rule):
        # Requires BOTH the extra item AND the list requirements
        return state.has_all(extraItems, world.player) and list_rule(state)
    
    return returnRule

def finalLevelEntryBerryRule(access_rule: list[list[str]], levelName: str, world: "CelesteModdedWorld"):

    level_rule = ruleFromList(access_rule, world) if len(levelName) == 0 else ruleFromListPlusCondition(access_rule, levelName, world)

    def returnRule(state: CollectionState):
        # Need to account for the scenario where the player is 1 short of the required strawberries but has the moon berry, bringing the total up to the required count. (Necessary for bugfix)
        strawberries = (state.has(ItemName.STRAWBERRY.value, world.player, world.required_strawberries) or state.has(ItemName.STRAWBERRY.value, world.player, world.required_strawberries - 1) and state.has(ItemName.MOON_BERRY.value, world.player))
        moon_berry = state.has(ItemName.MOON_BERRY, world.player) if world.options.require_moon_berry.value else True
        return strawberries and moon_berry and level_rule(state)

    return returnRule

def add_location(region: Region, name: str, world: "CelesteModdedWorld"):
    try:
        region.add_locations({name: world.location_name_to_id[name]}, ModdedCelesteLocation)
    except KeyError:
        raise ValueError(f"Location not found in location table: {name}")
    
def add_location_with_rule(region: Region, name: str, world: "CelesteModdedWorld", rule: list[list[str]]):
    add_location(region, name, world)
    set_rule(world.multiworld.get_location(name, world.player), ruleFromList(rule, world))
    
def add_item(name: str, world: "CelesteModdedWorld"):
    world.multiworld.itempool.append(world.create_item(name))
    
def calculate_strawberries(world: "CelesteModdedWorld"):
    world.total_strawberries_generated = min(calculate_maximum_possible_berries(world), world.options.total_strawberries.value)
    world.required_strawberries = round((world.options.strawberries_required_percentage.value / 100) * world.total_strawberries_generated)

def calculate_maximum_possible_berries(world: "CelesteModdedWorld"):
    extra_locations = 0
    for levelName,level in levelList.items():
        if levelEnabled(levelName, level, world) and (world.win_condition_level != levelName or not world.options.require_berries_for_goal.value): #If berries are needed to access the win condition level, we can't place berries there
            if not levelStartUnlocked(levelName, level, world):
                extra_locations -= 1 #Level unlock item
            for roomName,room in level.rooms.items():
                if not roomEnabled(level, room, world): # Skip easter egg rooms if necessary
                    continue
                if roomCheckEnabled(level, room, world):
                    extra_locations += 1 #Room check location
                if checkpointEnabled(level, room, world):
                    extra_locations += 1
                    extra_locations -= 1
                for location in room.locations:
                    if isEnabledLocation(location, levelName, level, room, world):
                        extra_locations += 1
                    if isEnabledItemByLocation(location, levelName, level, room, world):
                        extra_locations -= 1

                extra_locations -= len(room.key_door_ids) #Need space for locked door items
                
    extra_locations -= len(get_filtered_mechanics_list(world)) #Need space for mechanic items
    extra_locations -= 1 # One location must contain the win condition item
    return max(0, extra_locations)


# Regions must be built before this is run
def calculate_start_items(world: "CelesteModdedWorld"):
    state = CollectionState(world.multiworld)
    state.sweep_for_advancements()
    items_accessible = {
        loc for loc in world.multiworld.get_locations(world.player) 
        if loc.can_reach(state)
    }

    start_item_mapping = (Constants.min_sphere_one_locations_a_side if LevelCategory.A_SIDE in world.levels_categories_in_play
                          else Constants.min_sphere_one_locations_no_room_no_a_side if world.room_check_categories.isdisjoint(world.levels_categories_in_play - {LevelCategory.C_SIDE})
                          else Constants.min_sphere_one_locations_room_no_a_side)

    world.start_items_needed = max(0, start_item_mapping[world.options.item_consolidation_mode.value] - len(items_accessible))
    
# Ignore level access rules for heart sides when heart gates are open by default
def getLevelAccessRule(level: Level, world: "CelesteModdedWorld"):
    return [[]] if level.heartside and world.options.open_heart_gates.value else level.access_rule


def get_filtered_mechanics_list(world: "CelesteModdedWorld") -> set[ItemType]:

    def add_all_mechanics(set, access_rule_list, world):
        mapped_access_rule_list = mapItemList(access_rule_list, world)
        for item in [item for sublist in mapped_access_rule_list for item in sublist]:
            if item in mechanic.keys():
                set.add(item)

    mechanics = set()
    for levelName,level in levelList.items():
        if levelEnabled(levelName, level, world):
            add_all_mechanics(mechanics, level.access_rule, world)
            for _,room in level.rooms.items():
                for transition in room.transitions:
                    add_all_mechanics(mechanics, transition.access_rule, world)
                for location in room.locations:
                    add_all_mechanics(mechanics, location.access_rule, world)

    return mechanics

def create_start_locations(world: "CelesteModdedWorld"):
    root_region = world.get_region("Menu")
    for i in range(world.start_locations_created + 1, world.start_items_needed + 1):
        add_location(root_region, getStartLocationName(i), world)
        world.start_locations_created = world.start_locations_created + 1
        location = world.get_location(getStartLocationName(i))
        # location.item_rule = lambda item: item.player != location.player or item_type_dict[item.name] not in {ItemType.STRAWBERRY, ItemType.MOON_BERRY, ItemType.FILLER}

def generate_item_dict() -> tuple[dict[str, ItemType], dict[str, int]]:
    id_table: dict[str, int] = dict()
    checkpoint_items = []
    crystal_heart_items = []
    crystal_heart_clear_items = []
    # silver_berry_collect_items = []
    key_door_items = []
    gem_items = []
    for levelName in levelList:
        level = levelList[levelName]
        id_table[levelUnlock(levelName)] = level.level_id * Constants.level_id_multiplier + Constants.base_id + Constants.item_id_offset[ItemType.LEVEL]
        for roomName in levelList[levelName].rooms:
            room = levelList[levelName].rooms[roomName]
            if room.checkpoint:
                name = getCheckpointName(levelName, room.checkpoint)
                checkpoint_items.append(name)
                id_table[name] = getLocationBasedItemID(ItemType.CHECKPOINT, level, room)
            for location in room.locations:
                if location.location_type == LocationType.CRYSTAL_HEART:
                    name = getLocationName(levelName, roomName, LocationType.CRYSTAL_HEART, location.ID)
                    crystal_heart_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.CRYSTAL_HEART_VANILLA, level, room, location.ID)
                elif location.location_type == LocationType.LEVEL_CLEAR_MINI_HEART:
                    name = getLocationName(levelName, roomName, LocationType.LEVEL_CLEAR_MINI_HEART, location.ID)
                    crystal_heart_clear_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.CRYSTAL_HEART_SJ, level, room, location.ID)
                elif location.location_type == LocationType.GEM:
                    name = getLocationName(levelName, roomName, LocationType.GEM, location.ID)
                    gem_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.GEM, level, room, location.ID)
            for key_door in room.key_door_ids:
                name = getKeyDoorName(levelName, roomName, key_door)
                key_door_items.append(name)
                id_table[name] = getLocationBasedItemID(ItemType.KEY_DOOR, level, room, key_door)
                
                
    
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.MECHANIC] for name, id in mechanic.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.MOON_BERRY] for name, id in moon_berry.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.STRAWBERRY] for name, id in strawberry.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.VICTORY] for name, id in level_victory.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.FILLER] for name, id in filler.items()})
    
    item_dict = {
        **{item.value: ItemType.MECHANIC for item in mechanic},
        **{item.value: ItemType.FILLER for item in filler},
        **{item.value: ItemType.STRAWBERRY for item in strawberry},
        **{levelUnlock(level): ItemType.LEVEL for level in levelList.keys()},
        **{checkpoint: ItemType.CHECKPOINT for checkpoint in checkpoint_items},
        **{heart: ItemType.CRYSTAL_HEART_VANILLA for heart in crystal_heart_items},
        **{heart: ItemType.CRYSTAL_HEART_SJ for heart in crystal_heart_clear_items},
        **{key: ItemType.KEY_DOOR for key in key_door_items},
        **{item.value: ItemType.MOON_BERRY for item in moon_berry},
        **{gem: ItemType.GEM for gem in gem_items},
        **{item.value: ItemType.VICTORY for item in level_victory},
    }

    return item_dict, id_table
        

def generate_location_dict() -> tuple[dict[str, LocationType], dict[str, int]]:
    location_dict: dict[str, LocationType] = dict()
    id_table: dict[str, int] = dict()
    for i in range(1, Constants.maximum_possible_starting_items + 1):
        name = getStartLocationName(i)
        location_dict[name] = LocationType.STARTING_LOCATION
        id_table[name] = i
    for levelName in levelList:
        level = levelList[levelName]
        for roomName in levelList[levelName].rooms:
            room = level.rooms[roomName]
            if(not room.is_subregion_of):
                name = getRoomName(levelName, roomName)
                location_dict[name] = LocationType.ROOM
                id_table[name] = getLocationBasedLocationID(LocationType.ROOM, level, room)
            if room.checkpoint:
                name = getCheckpointName(levelName, level.rooms[roomName].checkpoint)
                location_dict[name] = LocationType.CHECKPOINT
                id_table[name] = getLocationBasedLocationID(LocationType.CHECKPOINT, level, room)
            for location in levelList[levelName].rooms[roomName].locations:
                location_name = getLocationName(levelName, roomName, location.location_type, location.ID)
                location_dict[location_name] = location.location_type
                id_table[location_name] = getLocationBasedLocationID(location.location_type, level, room, location.ID)
    
    return location_dict, id_table


def parse_regions(world: "CelesteModdedWorld"):
    root_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(root_region)
    
    for levelName,level in levelList.items():
        level = levelList[levelName]
        # Skip levels in non-included categories
        if not levelEnabled(levelName, level, world):
            continue
        
        # Create level regions and connect them to Menu
        level_region = Region(levelName, world.player, world.multiworld)
        if levelStartUnlocked(levelName, level, world):
            if world.options.require_berries_for_goal.value and levelName == world.win_condition_level:
                root_region.connect(level_region, rule=finalLevelEntryBerryRule(getLevelAccessRule(level, world), "", world))
            else:
                root_region.connect(level_region, rule=ruleFromList(getLevelAccessRule(level, world), world))
        else:
            if world.options.require_berries_for_goal.value and levelName == world.win_condition_level:
                root_region.connect(level_region, rule=finalLevelEntryBerryRule(getLevelAccessRule(level, world), levelUnlock(levelName), world))
            else:
                root_region.connect(level_region, rule=ruleFromListPlusCondition(getLevelAccessRule(level, world), levelUnlock(levelName), world))
        world.multiworld.regions.append(level_region)

        #Create room regions and connect the start room and checkpoints to the level region
        for roomName in level.rooms:
            room = level.rooms[roomName]
            
            room_region = Region(getRoomName(levelName, roomName), world.player, world.multiworld)
            world.multiworld.regions.append(room_region)
            if room.start_room:
                level_region.connect(room_region)
            elif room.checkpoint:
                level_region.connect(room_region, rule=ruleFromList([[getCheckpointName(levelName, room.checkpoint)]], world))
        
        #Connect rooms to each other and add locations
        for roomName in level.rooms:
            room = level.rooms[roomName]
            if not roomEnabled(level, room, world):
                continue
            room_region = world.multiworld.get_region(getRoomName(levelName, roomName), world.player)

            if roomCheckEnabled(level, room, world):
                    loc_name = getRoomName(levelName, roomName)
                    add_location(room_region, loc_name, world)

            if checkpointEnabled(level, room, world):
                    loc_name = getCheckpointName(levelName, room.checkpoint)
                    add_location(room_region, loc_name, world)
            
            for transition in room.transitions:
                destination_room_name = getRoomName(levelName, transition.destination_room)
                room_region.add_exits({destination_room_name}, {destination_room_name: ruleFromList(transition.access_rule, world)})
            for location in room.locations:
                if isEnabledLocation(location, levelName, level, room, world):
                    loc_name = getLocationName(levelName, roomName, location.location_type, location.ID)
                    add_location_with_rule(room_region, loc_name, world, location.access_rule)
    calculate_start_items(world)
    create_start_locations(world)


def create_items(world: "CelesteModdedWorld"):
    #Add items based on available locations
    for levelName,level in levelList.items():
        levelCategory = level.level_category
        if levelEnabled(levelName, level, world):

            if not levelStartUnlocked(levelName, level, world):
                add_item(levelUnlock(levelName), world)

            for roomName,room in level.rooms.items():
                if room.checkpoint and world.options.randomize_checkpoints.value:
                    #Win condition level checkpoint lock
                    if levelName == world.win_condition_level and world.options.protect_victory_level_checkpoints.value:
                        location = world.multiworld.get_location(getCheckpointName(levelName, room.checkpoint), world.player)
                        location.place_locked_item(world.create_item(getCheckpointName(levelName, room.checkpoint)))
                    else: 
                        add_item(getCheckpointName(levelName, room.checkpoint), world)
                if (room.easter_egg and not (world.options.easter_egg_rooms.value or world.options.easter_egg_rooms_difficult.value)) or (room.easter_egg_difficult and not world.options.easter_egg_rooms_difficult.value):
                    continue
                for location in room.locations:
                    if isEnabledItemByLocation(location, levelName, level, room, world):
                       add_item(getLocationName(levelName, roomName, location.location_type, location.ID), world)
                for key_door in room.key_door_ids:
                    add_item(getKeyDoorName(levelName, roomName, key_door), world)

        # Precollect disabled levels' hearts that we need
        elif heartNeeded(levelName, level, world):
            for roomName,room in level.rooms.items():
                for location in room.locations:
                    if location.location_type in {LocationType.LEVEL_CLEAR_MINI_HEART, LocationType.CRYSTAL_HEART}:
                        item_name = getLocationName(levelName, roomName, location.location_type, location.ID)
                        world.multiworld.push_precollected(world.create_item(item_name))
                        world.precollected_items = world.precollected_items + 1
    
    for mechanicItem in get_filtered_mechanics_list(world):
        add_item(mechanicItem, world)
    
    #Add strawberries + moonberry
    for i in range(world.total_strawberries_generated - 1):
        add_item(ItemName.STRAWBERRY.value, world)
    if world.total_strawberries_generated > 0 or world.options.require_moon_berry.value:
        add_item(ItemName.MOON_BERRY.value, world)
    
    setWinCondition(world)
    
    location_count = len(world.multiworld.get_unfilled_locations(world.player))

    # Thank you to Littlemuzz5 for catching a mistake here and fixing it
    item_count = sum(
        1 for item in world.multiworld.itempool
        if item.player == world.player
    )
    if item_count > location_count:
        world.start_items_needed = world.start_items_needed + (item_count - location_count)
        create_start_locations(world)
        location_count = len(world.multiworld.get_unfilled_locations(world.player))
    
    assert item_count <= location_count, "Celeste Modded has too many items to place in available locations"
    item_difference = location_count - item_count
    for i in range(item_difference):
        add_item(world.get_filler_item_name(), world)
    i = 0

def setWinCondition(world: "CelesteModdedWorld"):
    location = False

    if world.win_condition_level == LevelName.SUMMIT_A:
        location = world.multiworld.get_location(getLocationName(LevelName.SUMMIT_A, "g-03", LocationType.LEVEL_CLEAR), world.player)
    elif world.win_condition_level == LevelName.SUMMIT_B:
        location = world.multiworld.get_location(getLocationName(LevelName.SUMMIT_B, "g-03", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.FAREWELL:
        location = world.multiworld.get_location(getLocationName(LevelName.FAREWELL, "j-16", LocationType.LEVEL_CLEAR), world.player)
    elif world.win_condition_level == LevelName.BLUEBERRY_BAY:
        location = world.multiworld.get_location(getLocationName(LevelName.BLUEBERRY_BAY, "heartside_outro", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.RASPBERRY_ROOTS:
        location = world.multiworld.get_location(getLocationName(LevelName.RASPBERRY_ROOTS, "cp4-5-Heart", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.MANGO_MESA:
        location = world.multiworld.get_location(getLocationName(LevelName.MANGO_MESA, "Fin", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.STARFRUIT_SUPERNOVA:
        location = world.multiworld.get_location(getLocationName(LevelName.STARFRUIT_SUPERNOVA, "f07_and_you", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.PASSIONFRUIT_PANTHEON:
        location = world.multiworld.get_location(getLocationName(LevelName.PASSIONFRUIT_PANTHEON, "gg_Heart", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.CORE_A:
        location = world.multiworld.get_location(getLocationName(LevelName.CORE_A, "space", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.CORE_B:
        location = world.multiworld.get_location(getLocationName(LevelName.CORE_B, "space", LocationType.CRYSTAL_HEART), world.player)
    elif world.win_condition_level == LevelName.CORE_C:
        location = world.multiworld.get_location(getLocationName(LevelName.CORE_C, "02", LocationType.CRYSTAL_HEART), world.player)
    
    assert location != False, f"Win condition location was not found, this should not happen"
    location.place_locked_item(world.create_item(ItemName.LEVEL_VICTORY.value))

    world.multiworld.completion_condition[world.player] = lambda state, req_berries=world.required_strawberries: (
        (state.has(ItemName.STRAWBERRY.value, world.player, req_berries) or state.has(ItemName.STRAWBERRY.value, world.player, req_berries - 1) and state.has(ItemName.MOON_BERRY.value, world.player)) and
        (not world.options.require_moon_berry.value or state.has(ItemName.MOON_BERRY.value, world.player)) and
        state.has(ItemName.LEVEL_VICTORY.value, world.player)
    )

def isEnabledLocation(location: Location, levelName: str, level: Level, room: Room, world: "CelesteModdedWorld"):
    if location.location_type in {LocationType.GOLDEN_BERRY, LocationType.SILVER_BERRY} and not deathlessEnabled(levelName, level, world):
        return False
    if location.location_type == LocationType.WINGED_GOLDEN and not world.options.winged_golden.value:
        return False
    if location.multi_room_berry and world.options.exclude_multiroom_berries.value:
        return False
    if location.location_type == LocationType.ROOM:
        return roomCheckEnabled(level, room, world)
    if location.location_type == LocationType.CHECKPOINT:
        return 
    return True

def isEnabledItemByLocation (location: Location, levelName: str, level: Level, room: Room, world: "CelesteModdedWorld"):
    if heartNeeded(levelName, level, world) and location.location_type in {
        LocationType.CRYSTAL_HEART,
        LocationType.LEVEL_CLEAR_MINI_HEART,
    }:
        return True
    if location.location_type == LocationType.GEM:
        return True
    return False

def checkpointEnabled(level: Level, room: Room, world: "CelesteModdedWorld"):
    return world.options.randomize_checkpoints.value and room.checkpoint

def roomEnabled(level: Level, room: Room, world: "CelesteModdedWorld"):
    return ((room.easter_egg and (world.options.easter_egg_rooms.value or world.options.easter_egg_rooms_difficult.value))
            or (room.easter_egg_difficult and world.options.easter_egg_rooms_difficult.value)
            or (not room.easter_egg and not room.easter_egg_difficult))

def roomCheckEnabled(level: Level, room: Room, world: "CelesteModdedWorld"):
    return ((world.options.room_checks.value or level.level_category in world.room_check_categories)
            and not room.start_room
            and not room.is_subregion_of
            and not (world.options.trivial_room_checks.value == 1 and room.trivial_access)
            and roomEnabled(level, room, world))

def any_levels_enabled(levelNameList: list[str], world: "CelesteModdedWorld"):
    for levelName in levelNameList:
        if level_enabled(levelName, world):
            return True
    return False

def level_enabled(levelName: str, world: "CelesteModdedWorld"):
    return levelEnabled(levelName, levelList[levelName], world)

def levelEnabled(levelName: str, level: Level, world: "CelesteModdedWorld"):
    if levelName == world.win_condition_level:
        return True
    if level.puzzle and world.options.exclude_puzzle_levels.value:
        return False
    return level.level_category in world.levels_categories_in_play and getMaximumDifficulty(level.level_category, world) >= level.level_difficulty

def levelStartUnlocked(levelName: str, level: Level, world: "CelesteModdedWorld"):
    return levelEnabled(levelName, level, world) and (world.start_level_set == LevelCategory.ALL or (level.heartside and world.options.heart_sides_start_unlocked.value) or level.level_category == world.start_level_set)

def deathlessEnabled(levelName: str, level: Level, world: "CelesteModdedWorld"):
    if level.heartside:
        return False
    return level.level_category in world.deathless_categories_in_play

def calculateIDOffset(level: Level, room: Room):
    real_room = room
    if room.is_subregion_of:
        real_room = level.rooms.get(room.is_subregion_of)
    return level.level_id * Constants.level_id_multiplier + real_room.room_id * Constants.room_id_multiplier

def getLocationBasedItemID(category: ItemType, level: Level, room: Room, offset: int = 0):
    return Constants.base_id + Constants.item_id_offset[category] + calculateIDOffset(level, room) + offset

def getLocationBasedLocationID(category: LocationType, level: Level, room: Room, offset: int = 0):
    if category in {LocationType.CRYSTAL_HEART, LocationType.LEVEL_CLEAR, LocationType.LEVEL_CLEAR_MINI_HEART, LocationType.CASSETTE}: # these are 1 per level, and it helps with text mapping stuff on the mod side
        return Constants.base_id + Constants.location_id_offset[category] + level.level_id * Constants.level_id_multiplier
    else:
        return Constants.base_id + Constants.location_id_offset[category] + calculateIDOffset(level, room) + offset

def getMaximumDifficulty(levelCategory: LevelCategory, world: "CelesteModdedWorld"):
    match levelCategory:
        case LevelCategory.BEGINNER:
            return max(world.options.include_beginner.value, world.options.strawberry_jam_max_difficulty.value)
        case LevelCategory.INTERMEDIATE:
            return max(world.options.include_intermediate.value, world.options.strawberry_jam_max_difficulty.value - 3)
        case LevelCategory.ADVANCED:
            return max(world.options.include_advanced.value, world.options.strawberry_jam_max_difficulty.value - 6)
        case LevelCategory.EXPERT:
            return max(world.options.include_expert.value, world.options.strawberry_jam_max_difficulty.value - 9)
        case LevelCategory.GRANDMASTER:
            return max(world.options.include_grandmaster.value, world.options.strawberry_jam_max_difficulty.value - 12)
        case LevelCategory.A_SIDE:
            return 4
        case LevelCategory.B_SIDE:
            return 4
        case LevelCategory.C_SIDE:
            return 4
        case LevelCategory.FAREWELL:
            return 4
        case _:
            return 4

# Levels that have heart gates that expect hearts from the given level category to be available
def heartNeeded(levelName: str, level: Level, world: "CelesteModdedWorld") -> bool:
    dependent_levels = []
    if world.options.open_heart_gates.value or level.heartside:
        return False
    match level.level_category:
        case LevelCategory.BEGINNER:
            dependent_levels = [LevelName.BLUEBERRY_BAY]
        case LevelCategory.INTERMEDIATE:
            dependent_levels = [LevelName.RASPBERRY_ROOTS]
        case LevelCategory.ADVANCED:
            dependent_levels = [LevelName.MANGO_MESA]
        case LevelCategory.EXPERT:
            dependent_levels = [LevelName.STARFRUIT_SUPERNOVA]
        case LevelCategory.GRANDMASTER:
            dependent_levels = [LevelName.PASSIONFRUIT_PANTHEON]
        case LevelCategory.A_SIDE:
            dependent_levels = [LevelName.CORE_A, LevelName.CORE_B, LevelName.CORE_C, LevelName.FAREWELL]
        case LevelCategory.B_SIDE:
            dependent_levels = [LevelName.CORE_B, LevelName.CORE_C, LevelName.FAREWELL]
        case LevelCategory.C_SIDE:
            dependent_levels = [LevelName.CORE_C]
        case LevelCategory.FAREWELL:
            dependent_levels = []
        case _:
            dependent_levels = []
    return any_levels_enabled(dependent_levels, world)
    


def getActiveLevelList(world: "CelesteModdedWorld"):
    rValue: list[int] = []
    for levelName,level in levelList.items():
        if levelEnabled(levelName, level, world):
            rValue.append(level.level_id)
    return rValue

def getStartUnlockedLevelList(world: "CelesteModdedWorld"):
    rValue: list[int] = []
    for levelName,level in levelList.items():
        if levelStartUnlocked(levelName, level, world):
            rValue.append(level.level_id)
    return rValue

def getDeathlessLevelList(world: "CelesteModdedWorld"):
    rValue: list[int] = []
    for levelName,level in levelList.items():
        if deathlessEnabled(levelName, level, world):
            rValue.append(level.level_id)
    return rValue

def getRoomCheckLevelList(world: "CelesteModdedWorld"):
    rValue: list[int] = []
    for levelName,level in levelList.items():
        if level.level_category in world.room_check_categories:
            rValue.append(level.level_id)
    return rValue

# (location ID -> id based access_rule)
def getAutoCheckLocations(world: "CelesteModdedWorld"):
    rValue: dict[int, list[list[int]]] = dict()
    pre_processed_rValue: dict[int, list[list[str]]] = dict()
    #Start Locations
    for i in range(1, world.start_items_needed + 1):
        pre_processed_rValue[i] = []
    # Trivial Room Access Auto Collect
    if world.options.trivial_room_checks.value == 3:
        for levelName,level in levelList.items():
            if levelEnabled(levelName, level, world):
                for roomName,room in level.rooms.items():
                    if room.trivial_access:
                        full_access_rule = []
                        level_access_rule = mapItemList(getLevelAccessRule(level, world), world)
                        if len(level_access_rule) == 0:
                            level_access_rule = [[]]
                        if not levelStartUnlocked(levelName, level, world):
                            full_access_rule = [sublist + [levelUnlock(levelName)] for sublist in level_access_rule]
                        else:
                            full_access_rule = level_access_rule
                        pre_processed_rValue[getLocationBasedLocationID(LocationType.ROOM, level, room)] = full_access_rule

    # Crystal Heart requirements set to negative numbers (0 - number of hearts needed)
    return {location: [[0 - int(item.replace("#", "")) if item.startswith("#") else world.item_name_to_id[item] for item in sublist] for sublist in access] for location,access in pre_processed_rValue.items()}

def getAllLocationsPerLevel(world: "CelesteModdedWorld") -> dict[int, list[int]]:
    rValue: dict[int, list[int]] = dict()
    for levelName,level in levelList.items():
        if not levelEnabled(levelName, level, world):
            continue
        rValue[level.level_id] = []
        for roomName,room in level.rooms.items():
            if not roomEnabled(level, room, world):
                continue
            if roomCheckEnabled(level, room, world):
                rValue[level.level_id].append(getLocationBasedLocationID(LocationType.ROOM, level, room))
            if room.checkpoint and world.options.randomize_checkpoints.value:
                rValue[level.level_id].append(getLocationBasedLocationID(LocationType.CHECKPOINT, level, room))
            for location in room.locations:
                if isEnabledLocation(location, levelName, level, room, world):
                    rValue[level.level_id].append(getLocationBasedLocationID(location.location_type, level, room, location.ID))
    return rValue


item_type_dict: dict[str, ItemType]
location_type_dict: dict[str, LocationType]

item_id_table: dict[str, int]
location_id_table: dict[str, int]

# validate()
item_type_dict, item_id_table = generate_item_dict()
location_type_dict, location_id_table = generate_location_dict()