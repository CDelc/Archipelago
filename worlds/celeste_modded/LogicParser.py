from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Region
from .ItemLocationClasses import ModdedCelesteLocation
from .ValidateLayout import validate
from .constants import Constants
from worlds.generic.Rules import set_rule
from .level_logic.LogicalLayout import levelList
from .level_logic.LogicalObjects import Level, Room
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

def hasNCrystalHearts(n: int, state: CollectionState, world: "CelesteModdedWorld"):
    count = 0
    for itemName in state.prog_items[world.player]:
        if item_type_dict[itemName] == ItemType.CRYSTAL_HEART_VANILLA:
            count += 1
    return count >= n or world.options.open_heart_gates.value

def ruleFromList(items: list[list[str]], world):
    # Capture 'items' in the local scope using a default argument
    def returnRule(state: CollectionState, items=items, world=world):
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

def ruleFromListPlusCondition(items: list[list[str]], extraItem: str, world):

    list_rule = ruleFromList(items, world)
    
    def returnRule(state: CollectionState, extraItem=extraItem, list_rule=list_rule):
        # Requires BOTH the extra item AND the list requirements
        return state.has(extraItem, world.player) and list_rule(state)
    
    return returnRule

def finalLevelEntryBerryRule(access_rule: list[list[str]], levelName: str, world: "CelesteModdedWorld"):

    level_rule = ruleFromList(access_rule, world) if len(levelName) == 0 else ruleFromListPlusCondition(access_rule, levelName, world)

    def returnRule(state: CollectionState):
        strawberries = state.has(ItemName.STRAWBERRY, world.player, world.required_strawberries)
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
    strawberry_count = countStrawberries(world)
    return max(0, strawberry_count - len(get_filtered_mechanics_list(world)) - getLevelCount(world) + getRoomCheckCount(world) + countHeartsides(world) + (getCrystalHeartCount(world) if world.options.open_heart_gates.value else 0))

def calculate_start_items(world: "CelesteModdedWorld"):
    state = CollectionState(world.multiworld)
    state.sweep_for_advancements()
    items_accessible = {
        loc for loc in world.multiworld.get_locations(world.player) 
        if loc.can_reach(state)
    }
    world.start_items_needed = max(0, Constants.minimum_sphere_one_locations - len(items_accessible))
    
# Ignore level access rules for heart sides when heart gates are open by default
def getLevelAccessRule(level: Level, world: "CelesteModdedWorld"):
    return [[]] if level.heartside and world.options.open_heart_gates.value else level.access_rule


def get_filtered_mechanics_list(world: "CelesteModdedWorld") -> set[ItemType]:

    def add_all_mechanics(set, access_rule_list):
        for item in [item for sublist in access_rule_list for item in sublist]:
            if item in mechanic:
                set.add(item)

    mechanics = set()
    for _,level in levelList.items():
        if levelEnabled(level, world):
            add_all_mechanics(mechanics, level.access_rule)
            for _,room in level.rooms.items():
                for transition in room.transitions:
                    add_all_mechanics(mechanics, transition.access_rule)
                for location in room.locations:
                    add_all_mechanics(mechanics, location.access_rule)

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
        if not levelEnabled(level, world):
            continue
        
        # Create level regions and connect them to Menu
        level_region = Region(levelName, world.player, world.multiworld)
        if levelStartUnlocked(level, world):
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
            if (room.easter_egg and not (world.options.easter_egg_rooms.value or world.options.easter_egg_rooms_difficult.value)) or (room.easter_egg_difficult and not world.options.easter_egg_rooms_difficult.value):
                continue
            room_region = world.multiworld.get_region(getRoomName(levelName, roomName), world.player)
            if(world.options.room_checks.value and not room.is_subregion_of and not room.start_room):
                    loc_name = getRoomName(levelName, roomName)
                    add_location(room_region, loc_name, world)
            if(world.options.randomize_checkpoints.value and room.checkpoint):
                    loc_name = getCheckpointName(levelName, room.checkpoint)
                    add_location(room_region, loc_name, world)
            
            for transition in room.transitions:
                destination_room_name = getRoomName(levelName, transition.destination_room)
                room_region.add_exits({destination_room_name}, {destination_room_name: ruleFromList(transition.access_rule, world)})
            for location in room.locations:
                if location.location_type in {LocationType.GOLDEN_BERRY, LocationType.SILVER_BERRY} and not deathlessEnabled(level.level_category, world):
                    continue
                # Heartside goldens not included in logic
                if location.location_type == LocationType.GOLDEN_BERRY and isStrawberryJam(level.level_category):
                    continue
                if location.location_type == LocationType.WINGED_GOLDEN and not world.options.winged_golden.value:
                    continue
                loc_name = getLocationName(levelName, roomName, location.location_type, location.ID)
                add_location_with_rule(room_region, loc_name, world, location.access_rule)
    calculate_start_items(world)
    create_start_locations(world)


def create_items(world: "CelesteModdedWorld"):
    #Add items based on available locations
    for levelName,level in levelList.items():
        levelCategory = level.level_category
        if levelEnabled(level, world):

            if not levelStartUnlocked(level, world):
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
                    if not world.options.open_heart_gates.value and not level.heartside and location.location_type in {
                        LocationType.CRYSTAL_HEART,
                        LocationType.LEVEL_CLEAR_MINI_HEART,
                    }:
                        add_item(getLocationName(levelName, roomName, location.location_type, location.ID), world)
                    if location.location_type == LocationType.GEM:
                       add_item(getLocationName(levelName, roomName, location.location_type, location.ID), world)
                for key_door in room.key_door_ids:
                    add_item(getKeyDoorName(levelName, roomName, key_door), world)
        # Fix for missing puzzle level hearts breaking logic
        elif level.puzzle and world.options.exclude_puzzle_levels.value and level.level_category in world.levels_categories_in_play and not world.options.open_heart_gates.value:
            for roomName,room in level.rooms.items():
                for location in room.locations:
                    if location.location_type == LocationType.LEVEL_CLEAR_MINI_HEART:
                        item_name = getLocationName(levelName, roomName, location.location_type, location.ID)
                        world.multiworld.push_precollected(world.create_item(item_name))
               
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
    
    assert location != False, f"Win condition location was not found, this should not happen"
    location.place_locked_item(world.create_item(ItemName.LEVEL_VICTORY.value))

    world.multiworld.completion_condition[world.player] = lambda state, req_berries=world.required_strawberries: (
        state.has(ItemName.STRAWBERRY.value, world.player, req_berries) and
        (not world.options.require_moon_berry.value or state.has(ItemName.MOON_BERRY.value, world.player)) and
        state.has(ItemName.LEVEL_VICTORY.value, world.player)
    )

def levelEnabled(level: Level, world: "CelesteModdedWorld"):
    if level.level_id == 142: #Passionfruit Pantheon
        return LevelCategory.GRANDMASTER in world.levels_categories_in_play and LevelCategory.CRACKED_GRANDMASTER in world.levels_categories_in_play
    if level.puzzle and world.options.exclude_puzzle_levels.value:
        return False
    return level.level_category in world.levels_categories_in_play

def levelStartUnlocked(level: Level, world: "CelesteModdedWorld"):
    return levelEnabled(level, world) and (world.start_level_set == LevelCategory.ALL or (level.heartside and world.options.heart_sides_start_unlocked.value) or level.level_category == world.start_level_set)

def deathlessEnabled(levelCategory: LevelCategory, world: "CelesteModdedWorld"):
    match levelCategory:
        case LevelCategory.BEGINNER:
            return world.options.include_beginner_silvers.value
        case LevelCategory.INTERMEDIATE:
            return world.options.include_intermediate_silvers.value
        case LevelCategory.ADVANCED:
            return world.options.include_advanced_silvers.value
        case LevelCategory.EXPERT:
            return world.options.include_expert_silvers.value
        case LevelCategory.GRANDMASTER:
            return world.options.include_grandmaster_silvers.value
        case LevelCategory.CRACKED_GRANDMASTER:
            return world.options.include_cracked_grandmaster_silvers.value
        case LevelCategory.A_SIDE:
            return world.options.include_a_sides_goldens.value
        case LevelCategory.B_SIDE:
            return world.options.include_b_sides_goldens.value
        case LevelCategory.C_SIDE:
            return world.options.include_c_sides_goldens.value
        case LevelCategory.FAREWELL:
            return world.options.include_farewell_golden.value
        case _:
            return False

def isStrawberryJam(levelCategory: LevelCategory):
    return levelCategory in {LevelCategory.BEGINNER, LevelCategory.INTERMEDIATE, LevelCategory.ADVANCED, LevelCategory.EXPERT, LevelCategory.GRANDMASTER, LevelCategory.CRACKED_GRANDMASTER}

def countStrawberries(world: "CelesteModdedWorld") -> int:
    count = 0
    for levelName,level in levelList.items():
        # Skip levels in non-included categories
        if not levelEnabled(level, world):
            continue
        for room in level.rooms:
            for location in level.rooms[room].locations:
                if location.location_type == LocationType.STRAWBERRY:
                    count += 1
    return count

def getLevelCount(world: "CelesteModdedWorld") -> int:
    return len([level for _,level in levelList.items() if levelEnabled(level, world)])

def getCrystalHeartCount(world: "CelesteModdedWorld"):
    return getLevelCount(world) - (1 if levelEnabled(levelList[LevelName.FAREWELL], world) else 0) - countHeartsides(world)

def getRoomCheckCount(world: "CelesteModdedWorld") -> int:
    count = 0
    if not world.options.room_checks.value:
        return count
    for _,level in levelList.items():
        if not levelEnabled(level, world):
            continue
        for _,room in level.rooms.items():
            if room.is_subregion_of:
                continue
            if not world.options.easter_egg_rooms.value and (room.easter_egg or room.easter_egg_difficult):
                continue
            if not world.options.easter_egg_rooms_difficult.value and room.easter_egg_difficult:
                continue
            count = count + 1
    return count

def countHeartsides(world: "CelesteModdedWorld"):
    count = 0
    for _,level in levelList.items():
        if level.heartside and levelEnabled(level, world):
            count = count + 1
    return count

def findStartRoom(level: Level) -> Room:
    for room in Level.rooms:
        if Level.rooms[room].start_room:
            return Level.rooms[room]
    raise ValueError("Missing start room")

def calculateIDOffset(level: Level, room: Room):
    real_room = room
    if room.is_subregion_of:
        real_room = level.rooms.get(room.is_subregion_of)
    return level.level_id * Constants.level_id_multiplier + real_room.room_id * Constants.room_id_multiplier

def getLocationBasedItemID(category: ItemType, level: Level, room: Room, offset: int = 0):
    return Constants.base_id + Constants.item_id_offset[category] + calculateIDOffset(level, room) + offset

def getLocationBasedLocationID(category: LocationType, level: Level, room: Room, offset: int = 0):
    if category in {LocationType.CRYSTAL_HEART, LocationType.LEVEL_CLEAR, LocationType.LEVEL_CLEAR_MINI_HEART, LocationType.CASSETTE}:
        return Constants.base_id + Constants.location_id_offset[category] + level.level_id * Constants.level_id_multiplier
    else:
        return Constants.base_id + Constants.location_id_offset[category] + calculateIDOffset(level, room) + offset

item_type_dict: dict[str, ItemType]
location_type_dict: dict[str, LocationType]

item_id_table: dict[str, int]
location_id_table: dict[str, int]

# validate()
item_type_dict, item_id_table = generate_item_dict()
location_type_dict, location_id_table = generate_location_dict()