from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Region
from worlds.celeste_modded.ItemLocationClasses import ModdedCelesteLocation
from worlds.celeste_modded.constants import Constants
from worlds.generic.Rules import set_rule
from .constants.LogicalLayout import levelList, Level, Room, Transition, Location
from .constants.ItemNames import ItemName, filler, mechanic, strawberry, moon_berry, level_victory
from .constants.LevelNames import LevelName, LevelCategory
from .constants.LocationTypes import LocationType, RAINBOW_BERRIES, BEGINNER_RAINBOW_BERRY, INTERMEDIATE_RAINBOW_BERRY, ADVANCED_RAINBOW_BERRY, EXPERT_RAINBOW_BERRY, GRANDMASTER_RAINBOW_BERRY
from .constants.ItemTypes import ItemType
if TYPE_CHECKING:
    from . import CelesteModdedWorld

levelList: dict[str, Level]

def ruleFromList(items: list[list[str]], world):
    # Capture 'items' in the local scope using a default argument
    def returnRule(state: CollectionState, items=items):
        if not items:
            return True
        for andItems in items:
            if state.has_all(andItems, world.player):
                return True
        return False
    return returnRule

def ruleFromListPlusCondition(items: list[list[str]], extraItem: str, world):

    list_rule = ruleFromList(items, world)
    
    def returnRule(state: CollectionState, extraItem=extraItem, list_rule=list_rule):
        # Requires BOTH the extra item AND the list requirements
        return state.has(extraItem, world.player) and list_rule(state)
    
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
    
def generate_item_dict() -> tuple[dict[str, ItemType], dict[str, int]]:
    id_table: dict[str, int] = dict()
    checkpoint_items = []
    crystal_heart_items = []
    crystal_heart_clear_items = []
    silver_berry_collect_items = []
    key_items = []
    gem_items = []
    for levelName in levelList:
        level = levelList[levelName]
        if not level.level_category == LevelCategory.ALWAYS_ON:
            id_table[levelName.value] = level.level_id + Constants.base_id + Constants.item_id_offset[ItemType.LEVEL]
        for roomName in levelList[levelName].rooms:
            room = levelList[levelName].rooms[roomName]
            if level.rooms[roomName].checkpoint:
                name = getCheckpointName(levelName, level.rooms[roomName].checkpoint)
                checkpoint_items.append(name)
                id_table[name] = getLocationBasedItemID(ItemType.CHECKPOINT, level, room)
            for location in level.rooms[roomName].locations:
                if location.location_type == LocationType.CRYSTAL_HEART:
                    name = getLocationName(levelName, roomName, LocationType.CRYSTAL_HEART)
                    crystal_heart_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.CRYSTAL_HEART_VANILLA, level, room)
                elif location.location_type == LocationType.LEVEL_CLEAR_MINI_HEART:
                    name = getLocationName(levelName, roomName, LocationType.LEVEL_CLEAR_MINI_HEART)
                    crystal_heart_clear_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.CRYSTAL_HEART_SJ, level, room)
                elif location.location_type == LocationType.SILVER_BERRY:
                    name = getLocationName(levelName, roomName, LocationType.SILVER_BERRY)
                    silver_berry_collect_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.SILVER_BERRY, level, room)
                elif location.location_type == LocationType.KEY:
                    name = getLocationName(levelName, roomName, LocationType.KEY)
                    key_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.KEY, level, room)
                elif location.location_type == LocationType.GEM:
                    name = getLocationName(levelName, roomName, LocationType.GEM)
                    gem_items.append(name)
                    id_table[name] = getLocationBasedItemID(ItemType.GEM, level, room)
    
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.MECHANIC] for name, id in mechanic.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.MOON_BERRY] for name, id in moon_berry.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.STRAWBERRY] for name, id in strawberry.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.VICTORY] for name, id in level_victory.items()})
    id_table.update({name.value: id + Constants.base_id + Constants.item_id_offset[ItemType.FILLER] for name, id in filler.items()})
    
    item_dict = {
        **{item.value: ItemType.MECHANIC for item in mechanic},
        **{item.value: ItemType.FILLER for item in filler},
        **{item.value: ItemType.STRAWBERRY for item in strawberry},
        **{level.value: ItemType.LEVEL for level in levelList.keys() if not levelList[level].level_category == LevelCategory.ALWAYS_ON},
        **{checkpoint: ItemType.CHECKPOINT for checkpoint in checkpoint_items},
        **{heart: ItemType.CRYSTAL_HEART_VANILLA for heart in crystal_heart_items},
        **{heart: ItemType.CRYSTAL_HEART_SJ for heart in crystal_heart_clear_items},
        **{silver: ItemType.SILVER_BERRY for silver in silver_berry_collect_items},
        **{key: ItemType.KEY for key in key_items},
        **{item.value: ItemType.MOON_BERRY for item in moon_berry},
        **{gem: ItemType.GEM for gem in gem_items},
        **{item.value: ItemType.VICTORY for item in level_victory},
    }
                    
    return item_dict, id_table
        
        

def generate_location_dict() -> tuple[dict[str, LocationType], dict[str, int]]:
    location_dict: dict[str, LocationType] = dict()
    id_table: dict[str, int] = dict()
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
                location_name = getLocationName(levelName, roomName, location.location_type)
                location_dict[location_name] = location.location_type
                id_table[location_name] = getLocationBasedLocationID(location.location_type, level, room)
    
    for rainbow_berry in RAINBOW_BERRIES:
        location_dict[rainbow_berry] = LocationType.RAINBOW_BERRY
    id_table.update({name: id for id, name in enumerate(RAINBOW_BERRIES, start=Constants.base_id + Constants.location_id_offset[LocationType.RAINBOW_BERRY])})
    return location_dict, id_table


def parse_regions(world: "CelesteModdedWorld"):
    root_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(root_region)
    
    for levelName in levelList:
        level = levelList[levelName]
        # Skip levels in non-included categories
        if level.level_category not in world.levels_categories_in_play:
            continue
        
        # Create level regions and connect them to Menu
        level_region = Region(levelName, world.player, world.multiworld)
        if level.level_category == LevelCategory.ALWAYS_ON:
            root_region.connect(level_region)
        else:
            root_region.connect(level_region, rule=ruleFromListPlusCondition(level.access_rule, levelName, world))
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
            room_region = world.multiworld.get_region(getRoomName(levelName, roomName), world.player)
            if(world.options.room_checks and not room.is_subregion_of):
                    loc_name = getRoomName(levelName, roomName)
                    add_location(room_region, loc_name, world)
            if(world.options.randomize_checkpoints and room.checkpoint):
                    loc_name = getCheckpointName(levelName, room.checkpoint)
                    add_location(room_region, loc_name, world)
            
            for transition in room.transitions:
                destination_room_name = getRoomName(levelName, transition.destination_room)
                room_region.add_exits({destination_room_name}, {destination_room_name: ruleFromList(transition.access_rule, world)})
            for location in room.locations:
                if location.location_type == LocationType.GOLDEN_BERRY:
                    if not world.options.include_a_sides_goldens and level.level_category == LevelCategory.A_SIDE:
                        continue
                    if not world.options.include_b_sides_goldens and level.level_category == LevelCategory.B_SIDE:
                        continue
                    if not world.options.include_c_sides_goldens and level.level_category == LevelCategory.C_SIDE:
                        continue
                    if not world.options.include_farewell_golden and level.level_category == LevelCategory.FAREWELL:
                        continue
                    if not world.options.include_beginner_silvers and level.level_category == LevelCategory.BEGINNER_HEARTSIDE:
                        continue
                    if not world.options.include_intermediate_silvers and level.level_category == LevelCategory.INTERMEDIATE_HEARTSIDE:
                        continue
                    if not world.options.include_advanced_silvers and level.level_category == LevelCategory.ADVANCED_HEARTSIDE:
                        continue
                    # Expert and GM heartsides have goldens permanently disabled, as those challenges are out of scope of an archipelago world
                    if level.level_category == LevelCategory.EXPERT_HEARTSIDE:
                        continue
                    if level.level_category == LevelCategory.GRANDMASTER_HEARTSIDE:
                        continue
                
                if location.location_type == LocationType.SILVER_BERRY:
                    if not world.options.include_beginner_silvers and level.level_category == LevelCategory.BEGINNER:
                        continue
                    if not world.options.include_intermediate_silvers and level.level_category == LevelCategory.INTERMEDIATE:
                        continue
                    if not world.options.include_advanced_silvers and level.level_category == LevelCategory.ADVANCED:
                        continue
                    if not world.options.include_expert_silvers and level.level_category == LevelCategory.EXPERT:
                        continue
                    if not world.options.include_grandmaster_silvers and level.level_category == LevelCategory.GRANDMASTER:
                        continue
                    if not world.options.include_cracked_grandmaster_silvers and level.level_category == LevelCategory.CRACKED_GRANDMASTER:
                        continue
                
                if world.options.include_beginner_silvers:
                    add_location(root_region, BEGINNER_RAINBOW_BERRY, world)
                if world.options.include_intermediate_silvers:
                    add_location(root_region, INTERMEDIATE_RAINBOW_BERRY, world)
                if world.options.include_advanced_silvers:
                    add_location(root_region, ADVANCED_RAINBOW_BERRY, world)
                if world.options.include_expert_silvers:
                    add_location(root_region, EXPERT_RAINBOW_BERRY, world)
                if world.options.include_grandmaster_silvers and world.options.include_cracked_grandmaster_silvers:
                    add_location(root_region, GRANDMASTER_RAINBOW_BERRY, world)    
                    
                loc_name = getLocationName(levelName, roomName, location.location_type)
                add_location_with_rule(room_region, loc_name, world, location.access_rule)
            
    
def create_items(world: "CelesteModdedWorld"):
    strawberry_count = countStrawberries()
        
    #Add items based on available locations
    for levelName,level in levelList.items():
        levelCategory = level.level_category
        if levelCategory in world.levels_categories_in_play:
            #Precollect start level set access
            if not levelCategory == LevelCategory.ALWAYS_ON:
                if world.start_level_set == levelCategory:
                    world.multiworld.push_precollected(world.create_item(levelName))
                else:
                    add_item(levelName, world)
                
            for roomName,room in level.rooms.items():
                if room.checkpoint and world.options.randomize_checkpoints:
                    add_item(getCheckpointName(levelName, room.checkpoint), world)
                for location in room.locations:
                    if location.location_type in {
                        LocationType.GEM,
                        LocationType.KEY,
                        LocationType.CRYSTAL_HEART,
                        LocationType.LEVEL_CLEAR_MINI_HEART,
                        LocationType.SILVER_BERRY
                    }:
                       add_item(getLocationName(levelName, roomName, location.location_type), world) 
               
    #Add mechanics (precollect climb if option dictates it)         
    for mechanicItem in mechanic:
        if mechanicItem == ItemName.CLIMB.value and not world.options.randomize_climb:
            world.multiworld.push_precollected(world.create_item(ItemName.CLIMB.value))
        else:
            add_item(mechanicItem, world)
    
    #Add strawberries + moonberry
    world.total_strawberries_generated = min(strawberry_count - len(mechanic) - countCrystalHearts(), world.options.total_strawberries)
    for i in range(world.total_strawberries_generated - 1):
        add_item(ItemName.STRAWBERRY.value, world)
    add_item(ItemName.MOON_BERRY.value, world)
    
    setWinCondition(world)
    
    location_count = len(world.multiworld.get_unfilled_locations(world.player))
    item_count = len(world.multiworld.itempool)
    assert item_count <= location_count, "Celeste Modded has too many items to place in available locations"
    item_deficit = location_count - item_count
    for i in range(item_deficit):
        add_item(world.get_filler_item_name(), world)
    
    
def setWinCondition(world: "CelesteModdedWorld"):
    required_strawberries = round((world.options.strawberries_required_percentage / 100) * world.total_strawberries_generated)
    location = world.multiworld.get_location(getLocationName(LevelName.FORSAKEN_CITY_A, "end", LocationType.LEVEL_CLEAR), world.player)
    
    if world.win_condition_level == LevelName.FORSAKEN_CITY_A:
        location = world.multiworld.get_location(getLocationName(LevelName.FORSAKEN_CITY_A, "end", LocationType.LEVEL_CLEAR), world.player)
    location.place_locked_item(world.create_item(ItemName.LEVEL_VICTORY.value))
    
    # level = levelList[world.options.win_condition_level]
    # if world.options.lock_win_condition_behind_strawberries:
    #     level_region = world.multiworld.get_region(world.options.win_condition_level, world.player)
    #     world.multiworld.get_entrance()
    
    world.multiworld.completion_condition[world.player] = lambda state, req_berries=required_strawberries: (
        state.has(ItemName.STRAWBERRY.value, world.player, req_berries) and
        (not world.options.require_moon_berry or state.has(ItemName.MOON_BERRY.value, world.player)) and
        state.has(ItemName.LEVEL_VICTORY.value, world.player)
    )

def countStrawberries() -> int:
    count = 0
    for level in levelList:
        for room in levelList[level].rooms:
            for location in levelList[level].rooms[room].locations:
                if location.location_type == LocationType.STRAWBERRY:
                    count += 1
    return count

def countCrystalHearts() -> int:
    count = 0
    for level in levelList:
        for room in levelList[level].rooms:
            for location in levelList[level].rooms[room].locations:
                if location.location_type == LocationType.CRYSTAL_HEART:
                    count += 1
    return count
    
def findStartRoom(level: Level) -> Room:
    for room in Level.rooms:
        if Level.rooms[room].start_room:
            return Level.rooms[room]
    raise ValueError("Missing start room")

def calculateIDOffset(level: Level, room: Room):
    return level.level_id * 0x00001000 + room.room_id * 0x00000001

def getLocationBasedItemID(category: ItemType, level: Level, room: Room):
    return Constants.base_id + Constants.item_id_offset[category] + calculateIDOffset(level, room)

def getLocationBasedLocationID(category: LocationType, level: Level, room: Room):
    return Constants.base_id + Constants.location_id_offset[category] + calculateIDOffset(level, room)

def getCheckpointName(levelName: LevelName, checkpointName: str):
    return f"{levelName}: {checkpointName}"

def getRoomName(levelName: LevelName, roomName: str):
    return f"{levelName.value}:{roomName}"

def getLocationName(levelName: LevelName, roomName: str, location_type: LocationType):
    name = _getLocationNameNoAlias(levelName, roomName, location_type)
    if name in _location_alias:
        return _location_alias[name]
    else:
        return name

def _getLocationNameNoAlias(levelName: LevelName, roomName: str, location_type: LocationType):
    name = ""
    if location_type == LocationType.LEVEL_CLEAR_MINI_HEART:
        name = f"{levelName} Clear Heart"
    if location_type == LocationType.LEVEL_CLEAR:
        name = f"{levelName} Level Clear"
    if location_type == LocationType.GOLDEN_BERRY:
        name = f"{levelName} Golden Berry"
    if location_type == LocationType.SILVER_BERRY:
        name = f"{levelName} Silver Berry"
    if location_type == LocationType.CASSETTE:
        name = f"{levelName} Cassette"
    if location_type == LocationType.CRYSTAL_HEART:
        name = f"{levelName} Crystal Heart"
    else:
        name = f"{getRoomName(levelName, roomName)}:{location_type.value}"
    return name

_location_alias: dict[str, str] = {}

item_type_dict: dict[str, ItemType]
location_type_dict: dict[str, LocationType]

item_id_table: dict[str, int]
location_id_table: dict[str, int]

item_type_dict, item_id_table = generate_item_dict()
location_type_dict, location_id_table = generate_location_dict()