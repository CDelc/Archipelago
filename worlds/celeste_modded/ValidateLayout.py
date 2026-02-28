from collections import defaultdict

from .level_logic.LogicalObjects import Level, Room, Transition, Location
from .level_logic.LogicalLayout import levelList
from .constants.ItemNames import ItemName
from .constants.LocationTypes import LocationType
from .constants.LevelNames import LevelCategory, LevelName

RED = "\033[31m"
COLOR = "\033[35m"
RESET = "\033[0m"

def validateConnectivity(rooms: dict[str, Room], startRoom: str):
    remainingRooms = set(rooms.keys())
    validateConnectivityHelper(rooms, startRoom, remainingRooms)
    assert not remainingRooms, f"Some rooms disconnected from start room: {list(remainingRooms)}"
    
def validateConnectivityHelper(rooms: dict[str, Room], currentRoom: str, remainingRooms: set[str]):
    assert currentRoom in rooms.keys(), f"Error during connectivity validation, {currentRoom} does not exist"
    remainingRooms.remove(currentRoom)
    for transition in rooms[currentRoom].transitions:
        if transition.destination_room in remainingRooms:
            validateConnectivityHelper(rooms, transition.destination_room, remainingRooms)

levelList: dict[str, Level]
    
def validate():
    level_ids: set[int] = set()
    for levelName in levelList:
        room_ids: set[int] = set()
        print(f"{COLOR}{levelName}:{RESET}")
        print("---------------------------------------")
        
        locationTracker: dict[ItemName, int] = defaultdict(int)
        roomList = {room for room in levelList[levelName].rooms}
        startRoom = ""
        level = levelList[levelName]
        assert level.level_id not in level_ids, f"Duplicate Level ID: {level.level_id} in level {levelName}"
        assert level.level_id > 0, f"Level ID must be non-zero and positive for level {levelName}"
        assert level.level_id < 1000, f"Level Id must be less than 1000 for level {levelName}"
        level_ids.add(level.level_id)
        for ruleList in level.access_rule:
            assert isinstance(ruleList, list), f"Incorrectly formatted rule in level {levelName}"
        
        for roomName in levelList[levelName].rooms:
            room = levelList[levelName].rooms[roomName]
            assert not (room.start_room and startRoom), f"Second start room found in {levelName}:{roomName}"
            assert room.room_id not in room_ids, f"Duplicate Room ID: {room.room_id} in level {levelName}:{roomName}"
            assert room.room_id >= 0, f"Room ID must be positive for room {levelName}:{roomName}"
            assert room.room_id < 1000, f"Room Id must be less than 1000 for room {levelName}:{roomName}"
            room_ids.add(room.room_id)
            if room.start_room:
                startRoom = roomName
            
            if room.is_subregion_of:
                assert room.is_subregion_of in roomList, f"{roomName} is declared to be a subregion of {room.is_subregion_of} but this room does not exist in {levelName}"
                
            assert isinstance(room.locations, list), f"LOCATIONS NOT INSTANCE OF LIST: {levelName}:{roomName}"
            assert isinstance(room.transitions, list), f"TRANSITIONS NOT INSTANCE OF LIST: {levelName}:{roomName}"
                            
            for transition in room.transitions:
                assert isinstance(transition, Transition), f"INCORRECT TRANSITION TYPE: {levelName}:{roomName}"
                assert roomList.__contains__(transition.destination_room), f"{transition.destination_room} is not a listed room [{levelName}-{roomName}]"
                for ruleList in transition.access_rule:
                    assert isinstance(ruleList, list), f"Incorrectly formatted rule in transition {levelName}:{roomName}->{transition.destination_room}"
                    
            location_type_ids: dict[LocationType, set[int]] = dict()
            for location in room.locations:
                assert isinstance(location, Location), f"INCORRECT LOCATION TYPE: {levelName}:{roomName}"
                assert isinstance(location.access_rule, list), f"INCORRECT LOCATION ACCESS RULE TYPE: {levelName}:{roomName}"
                assert isinstance(location.ID, int), f"INCORRECT LOCATION ID TYPE: {levelName}:{roomName}"
                assert location.ID < 100000 and location.ID >= 0, f"Location ID must be between 0 and 100000 ({location.ID}): {levelName}:{roomName}"
                assert isinstance(location.location_type, LocationType), f"INCORRECT LOCATIONTYPE TYPE: {levelName}:{roomName}"
                assert location.location_type not in location_type_ids or location.ID not in location_type_ids[location.location_type], f"MULTIPLE OCCURRENCES OF LOCATION TYPE {location.location_type} WITH ID {location.ID} IN {levelName}:{roomName}"
                
                loc_type = location.location_type
                
                if loc_type not in location_type_ids:
                    location_type_ids.setdefault(loc_type, set())
                location_type_ids[loc_type].add(location.ID)
                
                if loc_type == LocationType.STRAWBERRY:
                    assert location.ID > 0, f"Strawberry without ID assigned in {levelName}:{roomName}"
                if loc_type == LocationType.LEVEL_CLEAR_MINI_HEART:
                    assert level.level_category in {LevelCategory.BEGINNER, LevelCategory.INTERMEDIATE, LevelCategory.ADVANCED, LevelCategory.EXPERT, LevelCategory.GRANDMASTER, LevelCategory.CRACKED_GRANDMASTER}, f"Level Clear Mini Heart should only exist in collab non-heartside levels ({levelName}:{roomName})"
                if loc_type == LocationType.GOLDEN_BERRY:
                    assert location.ID > 0, f"Strawberry without ID assigned in {levelName}:{roomName}"
                    assert level.level_category not in {LevelCategory.BEGINNER, LevelCategory.INTERMEDIATE, LevelCategory.ADVANCED, LevelCategory.EXPERT, LevelCategory.GRANDMASTER, LevelCategory.CRACKED_GRANDMASTER}, f"Golden Strawberries do not exist in collab non-heartside levels, use silver berry instead ({levelName}:{roomName})"
                if loc_type == LocationType.SILVER_BERRY:
                    assert location.ID > 0, f"Strawberry without ID assigned in {levelName}:{roomName}"
                    assert level.level_category in {LevelCategory.BEGINNER, LevelCategory.INTERMEDIATE, LevelCategory.ADVANCED, LevelCategory.EXPERT, LevelCategory.GRANDMASTER, LevelCategory.CRACKED_GRANDMASTER}, f"Silver berries should only exist in collab non-heartside levels ({levelName}:{roomName})"
                if loc_type == LocationType.LEVEL_CLEAR:
                    assert level.level_category in {LevelCategory.A_SIDE, LevelCategory.FAREWELL}, f"Level clear should only be used in prologues, farewell, and A-Sides. All other levels are either crystal hearts or mini crystal hearts ({levelName}:{roomName})"
                if loc_type == LocationType.GEM:
                    assert levelName == LevelName.SUMMIT_A, f"Gem locations can only exist in Summit A-Side, not {levelName}"
                
                locationTracker[location.location_type] += 1
                if location.location_type in {LocationType.CRYSTAL_HEART, LocationType.GOLDEN_BERRY, LocationType.SILVER_BERRY, LocationType.LEVEL_CLEAR, LocationType.LEVEL_CLEAR_MINI_HEART, LocationType.CASSETTE}:
                    assert locationTracker[location.location_type] < 2, f"{location.location_type} cannot exist more than once in {levelName}"
                for ruleList in location.access_rule:
                    assert isinstance(ruleList, list), f"Incorrectly formatted rule in location {levelName}:{roomName}:{location.location_type}"
                
        if not startRoom:
            raise ValueError(f"No start room found in {levelName}")
        validateConnectivity(level.rooms, startRoom)
        for itemName in locationTracker:
            print(f"{itemName.name} : {locationTracker[itemName]}")
        print("---------------------------------------")
    print(f"{RED}No issues{RESET}")