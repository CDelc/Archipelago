from dataclasses import dataclass, field
import dataclasses
from worlds.celeste_modded.Naming import getKeyDoorName, getLocationName
from worlds.celeste_modded.constants.LocationTypes import LocationType
from worlds.celeste_modded.constants.LevelNames import LevelName, LevelCategory
from worlds.celeste_modded.constants.ItemNames import ItemName

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
    excluded: bool = False
    key_door_ids: list[int] = dataclasses.field(default_factory=list)
    
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
            "1": Room(1, [Transition("2")], [Location(LocationType.GOLDEN_BERRY, 12, [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS]])], start_room=True),
            "2": Room(2, [Transition("3")], [Location(LocationType.STRAWBERRY, 11)]),
            "3": Room(3, [Transition("4")], [Location(LocationType.STRAWBERRY, 9)]),
            "4": Room(4, [Transition("3b")]),
            "3b": Room(0, [Transition("5")], [Location(LocationType.STRAWBERRY, 2)]),
            "5": Room(5, [Transition("5z"), Transition("5a", [[ItemName.TRAFFIC_BLOCKS]]), Transition("6", [[ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.STRAWBERRY, 21)]),
            "5z": Room(13, [Transition("5")], [Location(LocationType.STRAWBERRY, 10)]),
            "5a": Room(14, [Transition("5")], [Location(LocationType.STRAWBERRY, 2)]),
            "6": Room(6, [Transition("6z"), Transition("6a", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 12, [[ItemName.DASH_CRYSTALS]])], checkpoint="Crossing"),
            "6z": Room(15, [Transition("6"), Transition("6zb"), Transition("7zb")]),
            "6zb": Room(16, [Transition("6z")]),
            "7zb": Room(17, [Transition("6z"), Transition("6zb")], [Location(LocationType.STRAWBERRY, 2)]),
            "6a": Room(18, [Transition("6z"), Transition("6b")]),
            "6b": Room(19, [Transition("6a"), Transition("s0"), Transition("6c")]),
            "s0": Room(20, [Transition("6b"), Transition("s1", [[ItemName.TRAFFIC_BLOCKS]])]),
            "s1": Room(21, [Transition("s0")], [Location(LocationType.STRAWBERRY, 9), Location(LocationType.CRYSTAL_HEART)]),
            "6c": Room(22, [Transition("6b"), Transition("7"), Transition("7z")]),
            "7z": Room(23, [Transition("6c"), Transition("8z")], [Location(LocationType.STRAWBERRY, 3, [[ItemName.DASH_CRYSTALS]])]),
            "7": Room(7, [Transition("8")]),
            "8z": Room(24, [Transition("7z"), Transition("8zb")]),
            "8zb": Room(25, [Transition("8z"), Transition("8", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 1)]),
            "8": Room(8, [Transition("7a"), Transition("8b"), Transition("9z")]),
            "9z": Room(26, [Transition("8")], [Location(LocationType.STRAWBERRY, 3, [[ItemName.TRAFFIC_BLOCKS]])]),
            "7a": Room(27, [Transition("8")], [Location(LocationType.STRAWBERRY, 12)]),
            "8b": Room(28, [Transition("8"), Transition("9")], [Location(LocationType.STRAWBERRY, 1)]),
            "9": Room(9, [Transition("9b")], [Location(LocationType.STRAWBERRY, 14, [[ItemName.TRAFFIC_BLOCKS]])]),
            "9b": Room(30, [Transition("10", [[ItemName.TRAFFIC_BLOCKS]]), Transition("10a"), Transition("9c")], [Location(LocationType.STRAWBERRY, 9)], checkpoint="Chasm"),
            "10": Room(10, [Transition("10z"), Transition("9b"), Transition("11-bottom", [[ItemName.TRAFFIC_BLOCKS]])]),
            "10z": Room(31, [Transition("10"), Transition("10zb")]),
            "10zb": Room(32, [Transition("10z")], [Location(LocationType.STRAWBERRY, 1)]),
            "11-bottom": Room(33, [Transition("10", [[ItemName.TRAFFIC_BLOCKS]]), Transition("11z", [[ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.STRAWBERRY, 9, [[ItemName.TRAFFIC_BLOCKS]])], is_subregion_of="11"),
            "11z": Room(34, [Transition("11-bottom")], [Location(LocationType.CASSETTE, access_rule=[[ItemName.BLUE_CASSETTE], [ItemName.PINK_CASSETTE]])]),
            "9c": Room(35, [Transition("9b")], [Location(LocationType.STRAWBERRY, 2, [[ItemName.TRAFFIC_BLOCKS]])]),
            "10a": Room(36, [Transition("9b"), Transition("11")]),
            "11": Room(11, [Transition("10a"), Transition("12")]),
            "12": Room(12, [Transition("12a"), Transition("12z")]),
            "12z": Room(37, [Transition("12")], [Location(LocationType.STRAWBERRY, 8, [[ItemName.DASH_CRYSTALS]])]),
            "12a": Room(38, [Transition("12"), Transition("end", [[ItemName.TRAFFIC_BLOCKS], [ItemName.SPRINGS]])]),
            "end": Room(39, [], [Location(LocationType.LEVEL_CLEAR), Location(LocationType.WINGED_GOLDEN, 4, [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS]])])
        }, LevelCategory.A_SIDE, 1
    ),
    LevelName.FORSAKEN_CITY_B:
    Level(
        {
            "00": Room(0, [Transition("01")], [Location(LocationType.GOLDEN_BERRY, 25, [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS]])], start_room=True),
            "01": Room(1, [Transition("02")]),
            "02": Room(2, [Transition("02b", [[ItemName.TRAFFIC_BLOCKS]])]),
            "02b": Room(3, [Transition("03")]),
            "03": Room(4, [Transition("04", [[ItemName.DASH_CRYSTALS]])]),
            "04": Room(5, [Transition("05", [[ItemName.TRAFFIC_BLOCKS]]), Transition("03")], checkpoint="Contraption"),
            "05": Room(6, [Transition("05b")]),
            "05b": Room(7, [Transition("06", [[ItemName.DASH_CRYSTALS]])]),
            "06": Room(8, [Transition("07")]),
            "07": Room(9, [Transition("08"), Transition("06")]),
            "08": Room(10, [Transition("08b", [[ItemName.TRAFFIC_BLOCKS, ItemName.CRUMBLING_PLATFORM]])], checkpoint="Scrap Pit"),
            "08b": Room(11, [Transition("09")]),
            "09": Room(12, [Transition("10")]),
            "10": Room(13, [Transition("11", [[ItemName.DASH_CRYSTALS]]), Transition("09")]),
            "11": Room(14, [Transition("end", [[ItemName.CRUMBLING_PLATFORM]])]),
            "end": Room(15, [], [Location(LocationType.CRYSTAL_HEART, access_rule=[[ItemName.BLUE_CASSETTE]])])
        }, LevelCategory.B_SIDE, 2
    ),
    LevelName.FORSAKEN_CITY_C:
    Level(
        {
            "00": Room(0, [Transition("01", [[ItemName.DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.GOLDEN_BERRY, 50)], start_room=True),
            "01": Room(1, [Transition("02")]),
            "02": Room(2, [], [Location(LocationType.CRYSTAL_HEART, access_rule=[[ItemName.TOUCH_SWITCH]])])
        }, LevelCategory.C_SIDE, 3
    ),
    LevelName.SUMMIT_A:
    Level(
        {
            "a-00": Room(0, [Transition("a-01")], [Location(LocationType.GOLDEN_BERRY, 57, [[ItemName.DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS, ItemName.SPRINGS, ItemName.BADELINE_ORB, ItemName.DREAM_BLOCK, ItemName.TOUCH_SWITCH, ItemName.SINKING_PLATFORM, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.MOVING_BLOCK, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.MOVING_PLATFORM, ItemName.SWAP_BLOCK, ItemName.DASH_SWITCH, ItemName.FEATHER, getKeyDoorName(LevelName.SUMMIT_A, "f-05", 700)]])], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.DASH_CRYSTALS]]), Transition("a-00")]),
            "a-02": Room(2, [Transition("a-03"), Transition("a-01"), Transition("a-02b")]),
            "a-02b": Room(3, [Transition("a-02")], [Location(LocationType.STRAWBERRY, 61)]),
            "a-03": Room(4, [Transition("a-04", [[ItemName.SPRINGS]]), Transition("a-02")]),
            "a-04": Room(5, [Transition("a-05"), Transition("a-03"), Transition("a-04b")]),
            "a-04b": Room(6, [Transition("a-04")], [Location(LocationType.STRAWBERRY, 136), Location(LocationType.STRAWBERRY, 85)]),
            "a-05": Room(7, [Transition("a-06"), Transition("a-04")], [Location(LocationType.STRAWBERRY, 54)]),
            "a-06": Room(8, [Transition("b-00", [[ItemName.BADELINE_ORB]]), Transition("a-05")], [Location(LocationType.GEM, 110)]),
            "b-00": Room(9, [Transition("b-01")], checkpoint="500m"),
            "b-01": Room(10, [Transition("b-02", [[ItemName.SPRINGS]])]),
            "b-02": Room(11, [Transition("b-03"), Transition("b-01"), Transition("b-02b", [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 101)]),
            "b-02b": Room(12, [Transition("b-02"), Transition("b-02e"), Transition("b-02c")], [Location(LocationType.STRAWBERRY, 102)]),
            "b-03": Room(13, [Transition("b-05", [[ItemName.TRAFFIC_BLOCKS]]), Transition("b-04")]),
            "b-04": Room(14, [Transition("b-03")], [Location(LocationType.STRAWBERRY, 67)]),
            "b-05": Room(15, [Transition("b-06", [[ItemName.TOUCH_SWITCH]])]),
            "b-06": Room(16, [Transition("b-07"), Transition("b-05")]),
            "b-07": Room(17, [Transition("b-08"), Transition("b-06")]),
            "b-08": Room(18, [Transition("b-09"), Transition("b-07")], [Location(LocationType.STRAWBERRY, 129)]),
            "b-09": Room(19, [Transition("c-00", [[ItemName.TRAFFIC_BLOCKS, ItemName.BADELINE_ORB]]), Transition("b-08")], [Location(LocationType.STRAWBERRY, 167, [[ItemName.TRAFFIC_BLOCKS, ItemName.BADELINE_ORB]])]),
            "c-00": Room(20, [Transition("c-01", [[ItemName.DREAM_BLOCK]])], checkpoint="1000m"),
            "c-01": Room(21, [Transition("c-02")]),
            "c-02": Room(22, [Transition("c-03", [[ItemName.TOUCH_SWITCH]])]),
            "c-03": Room(23, [Transition("c-04"), Transition("c-03b")]),
            "c-03b": Room(24, [Transition("c-03")], [Location(LocationType.STRAWBERRY, 228, [[ItemName.DASH_CRYSTALS]])]),
            "c-04": Room(25, [Transition("c-06b"), Transition("c-05"), Transition("c-06")]),
            "c-05": Room(26, [Transition("c-04")], [Location(LocationType.STRAWBERRY, 248)]),
            "c-06": Room(27, [Transition("c-04"), Transition("c-07"), Transition("c-06b-strawberry-subroom")]),
            "c-06b": Room(28, [Transition("c-07", [[ItemName.CRUMBLING_PLATFORM]]), Transition("c-04"), Transition("c-06c", [[ItemName.CRUMBLING_PLATFORM]])]),
            "c-06b-strawberry-subroom": Room(96, [Transition("c-06b")], [Location(LocationType.STRAWBERRY, 218)], is_subregion_of="c-06b"),
            "c-06c": Room(29, [Transition("c-06b")], [Location(LocationType.GEM, 333, access_rule=[[ItemName.TOUCH_SWITCH]])]),
            "c-07": Room(30, [Transition("c-08"), Transition("c-07b")]),
            "c-07b": Room(31, [Transition("c-07")], [Location(LocationType.STRAWBERRY, 291)]),
            "c-08": Room(32, [Transition("c-09"), Transition("c-07")], [Location(LocationType.STRAWBERRY, 331)]),
            "c-09": Room(33, [Transition("d-00", [[ItemName.BADELINE_ORB]]), Transition("c-08")], [Location(LocationType.STRAWBERRY, 354, [[ItemName.BADELINE_ORB]])]),
            "d-00": Room(34, [Transition("d-01", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 43)], checkpoint="1500m"),
            "d-01": Room(35, [Transition("d-01b", [[ItemName.SINKING_PLATFORM]])]),
            "d-01b": Room(36, [Transition("d-02"), Transition("d-01"), Transition("d-01c")]),
            "d-01c": Room(37, [Transition("d-01b"), Transition("d-01d")], [Location(LocationType.STRAWBERRY, 226)]),
            "d-02": Room(38, [Transition("d-03", [[ItemName.TOUCH_SWITCH]]), Transition("d-01b")]),
            "d-03": Room(39, [Transition("d-04"), Transition("d-03b")], [Location(LocationType.STRAWBERRY, 383)]),
            "d-03b": Room(40, [Transition("d-03")], [Location(LocationType.CASSETTE, access_rule=[[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE]])]),
            "d-04": Room(41, [Transition("d-05"), Transition("d-03")], [Location(LocationType.STRAWBERRY, 388)]),
            "d-05": Room(42, [Transition("d-06"), Transition("d-04"), Transition("d-05b")]),
            "d-05b": Room(43, [Transition("d-05")], [Location(LocationType.GEM, 449)]),
            "d-06": Room(44, [Transition("d-09"), Transition("d-05"), Transition("d-07"), Transition("d-08")]),
            "d-07": Room(45, [Transition("d-06")], [Location(LocationType.STRAWBERRY, 484)]),
            "d-08": Room(46, [Transition("d-06"), Transition("d-10")], [Location(LocationType.STRAWBERRY, 527)]),
            "d-09": Room(47, [Transition("d-10"), Transition("d-06")]),
            "d-10": Room(48, [Transition("d-11"), Transition("d-10b")]),
            "d-10b": Room(49, [Transition("d-10")], [Location(LocationType.STRAWBERRY, 682, [[ItemName.SPRINGS]])]),
            "d-11": Room(50, [Transition("e-00b", [[ItemName.BADELINE_ORB]]), Transition("d-10")]),
            "e-00b": Room(51, [Transition("e-00", [[ItemName.GREEN_BUBBLES]])], checkpoint="2000m"),
            "e-00": Room(52, [Transition("e-03", [[ItemName.CLOUDS]]), Transition("e-02"), Transition("e-01")]),
            "e-02": Room(53, [Transition("e-00"), Transition("e-04", [[ItemName.PINK_CLOUDS]])], [Location(LocationType.STRAWBERRY, 7, [[ItemName.PINK_CLOUDS]])]),
            "e-03": Room(54, [Transition("e-04", [[ItemName.MOVING_PLATFORM]]), Transition("e-00")]),
            "e-04": Room(55, [Transition("e-05", [[ItemName.SPRINGS]])]),
            "e-05": Room(56, [Transition("e-06"), Transition("e-04")], [Location(LocationType.STRAWBERRY, 237)]),
            "e-06": Room(57, [Transition("e-07", [[ItemName.MOVING_BLOCK]]), Transition("e-05")]),
            "e-07": Room(58, [Transition("e-08"), Transition("e-06")], [Location(LocationType.STRAWBERRY, 473, [[ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS]])]),
            "e-08": Room(59, [Transition("e-10"), Transition("e-09", [[ItemName.CLOUDS]])]),
            "e-09": Room(60, [Transition("e-08"), Transition("e-11")], [Location(LocationType.STRAWBERRY, 398)]),
            "e-10": Room(61, [Transition("e-10b"), Transition("e-08")], [Location(LocationType.STRAWBERRY, 515)]),
            "e-10b": Room(62, [Transition("e-13"), Transition("e-10")]),
            "e-13": Room(63, [Transition("f-00", [[ItemName.BADELINE_ORB]])], [Location(LocationType.STRAWBERRY, 829, [[ItemName.BADELINE_ORB]])]),
            "f-00": Room(64, [Transition("f-02", [[ItemName.RED_BUBBLES]]), Transition("f-01", [[ItemName.RED_BUBBLES]])], [Location(LocationType.STRAWBERRY, 590, [[ItemName.RED_BUBBLES, ItemName.CRUMBLING_PLATFORM]])], checkpoint="2500m"),
            "f-01": Room(65, [Transition("f-00"), Transition("f-02b")], [Location(LocationType.STRAWBERRY, 639, [[ItemName.SWAP_BLOCK]])]),
            "f-02": Room(66, [Transition("f-04")]),
            "f-02b": Room(67, [Transition("f-02"), Transition("f-07", [[ItemName.DASH_CRYSTALS, ItemName.SWAP_BLOCK, ItemName.DASH_SWITCH]])], [Location(LocationType.GEM, 679, access_rule=[[ItemName.DASH_CRYSTALS, ItemName.SWAP_BLOCK, ItemName.DASH_SWITCH]])]),
            "f-04": Room(68, [Transition("f-03"), Transition("f-02")]),
            "f-03": Room(69, [Transition("f-05")]),
            "f-05": Room(70, [Transition("f-08", [[getKeyDoorName(LevelName.SUMMIT_A, "f-05", 700)]]), Transition("f-07", [[ItemName.RED_BUBBLES]]), Transition("f-06")], key_door_ids=[700]),
            "f-07": Room(71, [Transition("f-05")], [Location(LocationType.STRAWBERRY, 711), Location(LocationType.KEY, 712)]),
            "f-06": Room(72, [Transition("f-05")]),
            "f-08": Room(73, [Transition("f-09"), Transition("f-05"), Transition("f-08b", [[ItemName.RED_BUBBLES]])]),
            "f-08b": Room(74, [Transition("f-08"), Transition("f-08d")], [Location(LocationType.STRAWBERRY, 856)]),
            "f-09": Room(75, [Transition("f-10")]),
            "f-10": Room(76, [Transition("f-10b")]),
            "f-10b": Room(77, [Transition("f-11", [[ItemName.DASH_CRYSTALS, ItemName.DASH_SWITCH]])]),
            "f-11": Room(78, [Transition("g-00", [[ItemName.BADELINE_ORB]])], [Location(LocationType.STRAWBERRY, 1068, [[ItemName.BADELINE_ORB]]), Location(LocationType.STRAWBERRY, 1229, [[ItemName.BADELINE_ORB]]), Location(LocationType.STRAWBERRY, 1238)]),
            "g-00": Room(79, [Transition("g-00b")], checkpoint="3000m"),
            "g-00b": Room(80, [Transition("g-01", [[ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS]])], [Location(LocationType.STRAWBERRY, 37, [[ItemName.DASH_CRYSTALS]]), Location(LocationType.STRAWBERRY, 127, [[ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]]), Location(LocationType.STRAWBERRY, 114, [[ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS]]), Location(LocationType.CRYSTAL_HEART, access_rule=[[getLocationName(LevelName.SUMMIT_A, "a-06", LocationType.GEM, 110), getLocationName(LevelName.SUMMIT_A, "b-02d", LocationType.GEM, 109), getLocationName(LevelName.SUMMIT_A, "c-06c", LocationType.GEM, 333), getLocationName(LevelName.SUMMIT_A, "d-05b", LocationType.GEM, 449), getLocationName(LevelName.SUMMIT_A, "e-01c", LocationType.GEM, 8), getLocationName(LevelName.SUMMIT_A, "f-02b", LocationType.GEM, 679)]])]),
            "g-01": Room(81, [Transition("g-02", [[ItemName.CLOUDS, ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.TOUCH_SWITCH]])], [Location(LocationType.STRAWBERRY, 66, [[ItemName.CLOUDS, ItemName.DASH_CRYSTALS]]), Location(LocationType.STRAWBERRY, 279, [[ItemName.CLOUDS, ItemName.DASH_CRYSTALS]]), Location(LocationType.STRAWBERRY, 342, [[ItemName.CLOUDS, ItemName.DASH_CRYSTALS]])]),
            "g-02": Room(82, [Transition("g-03")]),
            "g-03": Room(83, [], [Location(LocationType.STRAWBERRY, 1504, [[ItemName.FEATHER]]), Location(LocationType.LEVEL_CLEAR, access_rule=[[ItemName.FEATHER]])]),
            "b-02e": Room(85, [Transition("b-02b")], [Location(LocationType.STRAWBERRY, 112)]),
            "b-02c": Room(86, [Transition("b-02d", [[ItemName.TRAFFIC_BLOCKS], [ItemName.DASH_CRYSTALS]]), Transition("b-02b"), Transition("b-05", [[ItemName.TRAFFIC_BLOCKS], [ItemName.DASH_CRYSTALS]])]),
            "b-02d": Room(87, [Transition("b-02c"), Transition("b-02")], [Location(LocationType.GEM, 109)]),
            "d-01d": Room(88, [Transition("d-01c")], [Location(LocationType.STRAWBERRY, 282, [[ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "e-01": Room(89, [Transition("e-01b")]),
            "e-01b": Room(90, [Transition("e-01"), Transition("e-01c")]),
            "e-01c": Room(91, [Transition("e-01")], [Location(LocationType.GEM, 8)]),
            "e-11": Room(92, [Transition("e-12"), Transition("e-10"), Transition("e-09")], [Location(LocationType.STRAWBERRY, 425)]),
            "e-12": Room(93, [Transition("e-11")], [Location(LocationType.STRAWBERRY, 504)]),
            "f-08d": Room(94, [Transition("f-08c", [[ItemName.DASH_SWITCH]])]),
            "f-08c": Room(95, [Transition("f-10", [[ItemName.SWAP_BLOCK, ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 759)])
        }, LevelCategory.A_SIDE, 19
    )
}

1+1