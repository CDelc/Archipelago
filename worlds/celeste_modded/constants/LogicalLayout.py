from dataclasses import dataclass, field
import dataclasses
from .LocationTypes import LocationType
from .LevelNames import LevelName, LevelCategory
from .ItemNames import ItemName

@dataclass(frozen=True)
class Location:
    location_type: LocationType
    ID: int = 0
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)

@dataclass(frozen=True)
class Transition:
    destination_room: str
    access_rule: list[list[ItemName]] = dataclasses.field(default_factory=list)
    
@dataclass(frozen=True)
class Room:
    room_id: int
    transitions: list[Transition]
    locations: list[Location] = dataclasses.field(default_factory=list)
    is_subregion_of: str = None
    start_room: bool = False
    checkpoint: str = None
    
@dataclass(frozen=True)
class Level:
    rooms: dict[str, Room]
    level_category: LevelCategory
    level_id: int
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)

levelList: dict[LevelName, Level] = {
    LevelName.FORSAKEN_CITY_A:
    Level(
        {
            "1": Room(1, [Transition("2")], [Location(LocationType.GOLDEN_BERRY, 12, [[ItemName.TRAFFIC_BLOCKS, ItemName.CLIMB, ItemName.DASH_CRYSTALS]])], start_room=True),
            "2": Room(2, [Transition("3")], [Location(LocationType.STRAWBERRY, 11)]),
            "3": Room(3, [Transition("4")], [Location(LocationType.STRAWBERRY, 9)]),
            "4": Room(4, [Transition("3b")]),
            "3b": Room(0, [Transition("5")], [Location(LocationType.STRAWBERRY, 2)]),
            "5": Room(5, [Transition("5z"), Transition("5a", [[ItemName.CLIMB], [ItemName.TRAFFIC_BLOCKS]]), Transition("6", [[ItemName.CLIMB], [ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.STRAWBERRY, 21, [[ItemName.CLIMB]])]),
            "5z": Room(13, [Transition("5")], [Location(LocationType.STRAWBERRY, 10)]),
            "5a": Room(14, [Transition("5")], [Location(LocationType.STRAWBERRY, 2)]),
            "6": Room(6, [Transition("6z"), Transition("6a", [[ItemName.CLIMB], [ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 12, [[ItemName.CLIMB], [ItemName.DASH_CRYSTALS]])], checkpoint="Crossing"),
            "6z": Room(15, [Transition("6"), Transition("6zb"), Transition("7zb")]),
            "6zb": Room(16, [Transition("6z")]),
            "7zb": Room(17, [Transition("6z"), Transition("6zb")], [Location(LocationType.STRAWBERRY, 2)]),
            "6a": Room(18, [Transition("6z"), Transition("6b")]),
            "6b": Room(19, [Transition("6a"), Transition("s0"), Transition("6c")]),
            "s0": Room(20, [Transition("6b"), Transition("s1", [[ItemName.TRAFFIC_BLOCKS, ItemName.CLIMB]])]),
            "s1": Room(21, [Transition("s0")], [Location(LocationType.STRAWBERRY, 9), Location(LocationType.CRYSTAL_HEART)]),
            "6c": Room(22, [Transition("6b"), Transition("7"), Transition("7z")]),
            "7z": Room(23, [Transition("6c"), Transition("8z")], [Location(LocationType.STRAWBERRY, 3, [[ItemName.DASH_CRYSTALS]])]),
            "7": Room(7, [Transition("8")]),
            "8z": Room(24, [Transition("7z"), Transition("8zb")]),
            "8zb": Room(25, [Transition("8z"), Transition("8", [[ItemName.CLIMB], [ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 1)]),
            "8": Room(8, [Transition("7a"), Transition("8b"), Transition("9z")]),
            "9z": Room(26, [Transition("8")], [Location(LocationType.STRAWBERRY, 3, [[ItemName.TRAFFIC_BLOCKS]])]),
            "7a": Room(27, [Transition("8")], [Location(LocationType.STRAWBERRY, 12)]),
            "8b": Room(28, [Transition("8"), Transition("9")], [Location(LocationType.STRAWBERRY, 1)]),
            "9": Room(9, [Transition("9b")], [Location(LocationType.STRAWBERRY, 14, [[ItemName.CLIMB, ItemName.TRAFFIC_BLOCKS]])]),
            "9b": Room(30, [Transition("10", [[ItemName.CLIMB, ItemName.TRAFFIC_BLOCKS]]), Transition("10a"), Transition("9c")], [Location(LocationType.STRAWBERRY, 9)], checkpoint="Chasm"),
            "10": Room(10, [Transition("10z"), Transition("9b"), Transition("11-bottom", [[ItemName.TRAFFIC_BLOCKS]])]),
            "10z": Room(31, [Transition("10"), Transition("10zb")]),
            "10zb": Room(32, [Transition("10z")], [Location(LocationType.STRAWBERRY, 1)]),
            "11-bottom": Room(33, [Transition("10", [[ItemName.CLIMB, ItemName.TRAFFIC_BLOCKS]]), Transition("11z", [[ItemName.CLIMB, ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.STRAWBERRY, 9, [[ItemName.CLIMB, ItemName.TRAFFIC_BLOCKS]])], is_subregion_of="11"),
            "11z": Room(34, [Transition("11-bottom")], [Location(LocationType.CASSETTE, access_rule=[[ItemName.BLUE_CASSETTE], [ItemName.PINK_CASSETTE]])]),
            "9c": Room(35, [Transition("9b")], [Location(LocationType.STRAWBERRY, 2, [[ItemName.TRAFFIC_BLOCKS]])]),
            "10a": Room(36, [Transition("9b"), Transition("11")]),
            "11": Room(11, [Transition("10a"), Transition("12", [[ItemName.CLIMB]])]),
            "12": Room(12, [Transition("12a", [[ItemName.CLIMB]]), Transition("12z", [[ItemName.CLIMB]])]),
            "12z": Room(37, [Transition("12")], [Location(LocationType.STRAWBERRY, 8, [[ItemName.DASH_CRYSTALS]])]),
            "12a": Room(38, [Transition("12"), Transition("end", [[ItemName.CLIMB, ItemName.TRAFFIC_BLOCKS], [ItemName.SPRINGS]])]),
            "end": Room(39, [], [Location(LocationType.LEVEL_CLEAR), Location(LocationType.WINGED_GOLDEN, 4, [[ItemName.TRAFFIC_BLOCKS, ItemName.CLIMB, ItemName.DASH_CRYSTALS]])])
        }, LevelCategory.A_SIDE, 1, [[LevelName.FORSAKEN_CITY_A]]
    )
}