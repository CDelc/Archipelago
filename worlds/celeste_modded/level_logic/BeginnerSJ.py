from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType



beginner_levels_sj : dict[LevelName, Level] = {
    LevelName.LOOPY_LAGOON:
    Level(
        {
            "c-01": Room(0, [Transition("c-02")], [Location(LocationType.SILVER_BERRY, 60, [[ItemName.LOOP_BLOCK, ItemName.GREEN_BUBBLES]])], start_room=True),
            "c-02": Room(1, [Transition("c-03", [[ItemName.LOOP_BLOCK, ItemName.GREEN_BUBBLES]])]),
            "c-03": Room(2, [Transition("c-04")]),
            "c-04": Room(3, [Transition("c-05")]),
            "c-05": Room(4, [Transition("c-06")]),
            "c-06": Room(5, [Transition("c-07")]),
            "c-07": Room(6, [Transition("c-08")]),
            "c-08": Room(7, [Transition("c-09"), Transition("c-08b")]),
            "c-08b": Room(8, [Transition("c-08")], [Location(LocationType.STRAWBERRY, 2428)]),
            "c-09": Room(9, [Transition("c-10")]),
            "c-10": Room(10, [Transition("c-1")]),
            "c-1": Room(11, [Transition("c-12")], [Location(LocationType.STRAWBERRY, 1037)]),
            "c-12": Room(12, [Transition("c-13")]),
            "c-13": Room(13, [Transition("c-14"), Transition("c-13b")], [Location(LocationType.STRAWBERRY, 2140)]),
            "c-13b": Room(14, [Transition("c-13")]),
            "c-14": Room(15, [Transition("c-15")]),
            "c-15": Room(16, [Transition("c-16")]),
            "c-16": Room(17, [Transition("c-17")]),
            "c-17": Room(18, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 27, [[ItemName.GREEN_BUBBLES]]
    ),
    LevelName.FOREST_PATH:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.SPRINGS]])], [Location(LocationType.SILVER_BERRY, 1329, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DREAM_DASH_CRYSTAL, ItemName.SPRINGS]])], start_room=True),
            "a-02": Room(1, [Transition("a-03", [[ItemName.DASH_CRYSTALS]])]),
            "a-03": Room(2, [Transition("a-04", [[ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 3, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-04": Room(3, [Transition("a-05", [[ItemName.DREAM_DASH_CRYSTAL]])]),
            "a-05": Room(4, [Transition("a-06")]),
            "a-06": Room(5, [Transition("a-07")]),
            "a-07": Room(6, [Transition("a-08")]),
            "a-08": Room(7, [Transition("a-09")]),
            "a-09": Room(8, [Transition("a-10")]),
            "a-10": Room(9, [Transition("a-11")]),
            "a-11": Room(10, [Transition("a-12")], [Location(LocationType.STRAWBERRY, 1244)]),
            "a-12": Room(11, [Transition("a-13"), Transition("a-16")]),
            "a-13": Room(12, [Transition("a-14")]),
            "a-16": Room(13, [Transition("a-17")]),
            "a-14": Room(14, [Transition("a-15"), Transition("a-17")]),
            "a-17": Room(15, [Transition("a-18")], [Location(LocationType.STRAWBERRY, 1634)]),
            "a-15": Room(16, [Transition("a-17")]),
            "a-18": Room(17, [Transition("a-19")]),
            "a-19": Room(18, [Transition("a-20")], [Location(LocationType.STRAWBERRY, 523)]),
            "a-20": Room(19, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 28
    ),
    LevelName.DRIVEWAY_DID_YOU_IN:
    Level(
        {
            "00- intro": Room(0, [Transition("01- Crusher")], [Location(LocationType.SILVER_BERRY, 581, [[ItemName.INTRO_CRUSHER, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS, ItemName.SPRINGS, ItemName.GREEN_BUBBLES]])], start_room=True),
            "01- Crusher": Room(1, [Transition("02- Bait N'Switch", [[ItemName.INTRO_CRUSHER]])]),
            "02- Bait N'Switch": Room(2, [Transition("03- Uberjump", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS]]), Transition("02B- a strwawbewwy??")]),
            "02B- a strwawbewwy??": Room(3, [], [Location(LocationType.STRAWBERRY, 682)]),
            "03- Uberjump": Room(4, [Transition("04- Head Trauma")]),
            "04- Head Trauma": Room(5, [Transition("05- Boing")]),
            "05- Boing": Room(6, [Transition("06- Bubbles", [[ItemName.SPRINGS]])]),
            "06- Bubbles": Room(7, [Transition("07- Falling Cannon", [[ItemName.GREEN_BUBBLES]])]),
            "07- Falling Cannon": Room(8, [Transition("08- U Turn"), Transition("07B- OwO whats this??")]),
            "07B- OwO whats this??": Room(9, [], [Location(LocationType.STRAWBERRY, 1459)]),
            "08- U Turn": Room(10, [Transition("09- Fin")]),
            "09- Fin": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 29
    ),
    LevelName.AZURE_CAVERNS:
    Level(
        {
            "01": Room(0, [Transition("02")], [Location(LocationType.SILVER_BERRY, 797)], start_room=True),
            "02": Room(1, [Transition("03", [[ItemName.DASH_TRAFFIC_BLOCK]]), Transition("02b", [[ItemName.DASH_TRAFFIC_BLOCK]])]),
            "02b": Room(2, [Transition("02")], [Location(LocationType.STRAWBERRY, 289)]),
            "03": Room(3, [Transition("04", [[ItemName.DASH_CRYSTALS]])]),
            "04": Room(4, [Transition("05"), Transition("04b")]),
            "04b": Room(5, [Transition("04")], [Location(LocationType.STRAWBERRY, 313)]),
            "05": Room(6, [Transition("06")]),
            "06": Room(7, [Transition("07")]),
            "07": Room(8, [Transition("08")]),
            "08": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 30
    ),
    LevelName.CASSETTE_CLIFFS:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.BLUE_TRAFFIC_CASSETTE, ItemName.PINK_TRAFFIC_CASSETTE]])], [Location(LocationType.SILVER_BERRY, 1115, [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BLUE_TRAFFIC_CASSETTE, ItemName.PINK_TRAFFIC_CASSETTE, ItemName.YELLOW_TRAFFIC_CASSETTE]])], start_room=True),
            "2": Room(1, [Transition("3", [[ItemName.YELLOW_CASSETTE, ItemName.YELLOW_TRAFFIC_CASSETTE, ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE]])]),
            "3": Room(2, [Transition("6", [[getKeyDoorName(LevelName.CASSETTE_CLIFFS, "3", 10)]]), Transition("4", [[ItemName.DOUBLE_DASH_CRYSTALS]])], key_door_ids=[10]),
            "3-key": Room(100, [Transition("3")], [Location(LocationType.KEY, 154)], is_subregion_of="3"),
            "4": Room(3, [Transition("5", [[ItemName.TOUCH_SWITCH]]), Transition("ber4", [[ItemName.TOUCH_SWITCH]])]),
            "6": Room(4, [Transition("7", [[ItemName.DASH_CRYSTALS]])]),
            "7": Room(5, [Transition("10", [[getKeyDoorName(LevelName.CASSETTE_CLIFFS, "7", 494)]]), Transition("8")], [Location(LocationType.KEY, 1078)], key_door_ids=[494]),
            "8": Room(6, [Transition("10-berry"), Transition("7-middle", [[ItemName.TOUCH_SWITCH]])]),
            "7-top": Room(102, [], is_subregion_of="7"),
            "7-middle": Room(103, [Transition("9")], is_subregion_of="7"),
            "9": Room(7, [Transition("7-top", [[ItemName.CRUMBLING_PLATFORM]])]),
            "10": Room(8, [Transition("11-c", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "10-berry": Room(101, [Transition("8")], [Location(LocationType.STRAWBERRY, 761)], is_subregion_of="10"),
            "11-c": Room(9, [Transition("12", [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS]])]),
            "12": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "ber4": Room(12, [Transition("4")], [Location(LocationType.STRAWBERRY, 31)]),
            "5": Room(13, [Transition("3-key", [[ItemName.CRUMBLING_PLATFORM]])])
        }, LevelCategory.BEGINNER, 31
    ),
    LevelName.SOAP:
    Level(
        {
            "01": Room(0, [Transition("02", [[ItemName.SOAP_BUBBLE, ItemName.DASHLESS_SPRING]])], [Location(LocationType.SILVER_BERRY, 63, [[ItemName.SOAP_BUBBLE, ItemName.DASHLESS_SPRING, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.MOVING_BLOCK, ItemName.TOUCH_SWITCH]])], start_room=True),
            "02": Room(1, [Transition("03", [[ItemName.DASH_CRYSTALS]])]),
            "03": Room(2, [Transition("04", [[ItemName.TOUCH_SWITCH]])]),
            "04": Room(3, [Transition("05", [[ItemName.MOVING_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("04b", [[ItemName.MOVING_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "04b": Room(4, [Transition("04")], [Location(LocationType.STRAWBERRY, 3286)]),
            "05": Room(5, [Transition("06"), Transition("05b")]),
            "05b": Room(6, [Transition("05")], [Location(LocationType.STRAWBERRY, 1447)]),
            "06": Room(7, [Transition("07")]),
            "07": Room(8, [Transition("08"), Transition("07b")]),
            "07b": Room(9, [Transition("07")], [Location(LocationType.STRAWBERRY, 2593)]),
            "08": Room(10, [Transition("09")]),
            "09": Room(11, [Transition("10")]),
            "10": Room(12, [Transition("11"), Transition("10b")]),
            "10b": Room(13, [Transition("10")], [Location(LocationType.STRAWBERRY, 2898)]),
            "11": Room(14, [Transition("heart"), Transition("11b")]),
            "11b": Room(15, [Transition("11")]),
            "heart": Room(16, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 32
    ),
    LevelName.OVER_THE_CITY:
    Level(
        {
            "01": Room(0, [Transition("02", [[ItemName.SINGLE_JUMP_REFILL]])], [Location(LocationType.SILVER_BERRY, 555, [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.TRIPLE_JUMP_REFILL, ItemName.SINGLE_JUMP_REFILL]])], start_room=True),
            "02": Room(1, [Transition("03"), Transition("Berry1")]),
            "Berry1": Room(2, [Transition("02")], [Location(LocationType.STRAWBERRY, 821)]),
            "03": Room(3, [Transition("04")]),
            "04": Room(4, [Transition("05")]),
            "05": Room(5, [Transition("07"), Transition("06")]),
            "06": Room(6, [Transition("05")]),
            "07": Room(7, [Transition("08")]),
            "08": Room(8, [Transition("09")]),
            "09": Room(9, [Transition("10")]),
            "10": Room(10, [Transition("11")]),
            "11": Room(11, [Transition("12", [[ItemName.TOUCH_SWITCH]])]),
            "12": Room(12, [Transition("13"), Transition("Berry2")]),
            "Berry2": Room(13, [Transition("12")], [Location(LocationType.STRAWBERRY, 783)]),
            "13": Room(14, [Transition("14")]),
            "14": Room(15, [Transition("15")]),
            "15": Room(16, [Transition("16", [[ItemName.TRIPLE_JUMP_REFILL]])]),
            "16": Room(17, [Transition("17")]),
            "17": Room(18, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, [[ItemName.DASH_CRYSTALS]])]),
            "RouteB-1": Room(20, [Transition("RouteB-2"), Transition("RouteB-3"), Transition("RouteB-4")], [Location(LocationType.STRAWBERRY, 823)]),
            "RouteB-2": Room(21, [Transition("RouteB-1")]),
            "RouteB-3": Room(22, [Transition("RouteB-1")]),
            "RouteB-4": Room(23, [Transition("RouteB-1")]),
            "RouteA-2": Room(24, [Transition("RouteA-1"), Transition("RouteA-3")]),
            "RouteA-1": Room(25, [Transition("RouteA-2")]),
            "RouteA-3": Room(26, [Transition("RouteA-2")])
        }, LevelCategory.BEGINNER, 33
    ),
    LevelName.TROPHOSPHERE:
    Level(
        {
            "a_01": Room(0, [Transition("a_02", [[ItemName.DREAM_BLOCK, ItemName.CLOUDS, ItemName.DOUBLE_DASH_DREAM_BLOCK, ItemName.PINK_CLOUDS, ItemName.BADELINE_ORB]])], start_room=True),
            "a_02": Room(1, [Transition("a_03", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.FEATHER]])], [Location(LocationType.SILVER_BERRY, 162, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.FEATHER, ItemName.DREAM_BLOCK, ItemName.CLOUDS, ItemName.DOUBLE_DASH_DREAM_BLOCK, ItemName.PINK_CLOUDS, ItemName.BADELINE_ORB]])]),
            "a_03": Room(2, [Transition("b_01", [[ItemName.DASH_CRYSTALS]])]),
            "b_01": Room(3, [Transition("b_02")]),
            "b_02": Room(4, [Transition("b_03")]),
            "b_03": Room(5, [Transition("b_04")]),
            "b_04": Room(6, [Transition("b_05")]),
            "b_05": Room(7, [Transition("c_01")]),
            "c_01": Room(8, [Transition("c_02")]),
            "c_02": Room(9, [Transition("c_03_end")], [Location(LocationType.STRAWBERRY, 101)]),
            "c_03_end": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 34
    ),
    LevelName.CORESAKEN_CITY:
    Level(
        {
            "a_01": Room(0, [Transition("a_02", [[ItemName.CORE_BLOCK, ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.SILVER_BERRY, 160, [[ItemName.CORE_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.SPRINGS]])], start_room=True),
            "a_02": Room(1, [Transition("a_03", [[ItemName.SPRINGS]])]),
            "a_03": Room(2, [Transition("a_04", [[ItemName.TOUCH_SWITCH]])]),
            "a_04": Room(3, [Transition("a_05")]),
            "a_05": Room(4, [Transition("a_06", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a_06": Room(5, [Transition("a_07", [[ItemName.DASH_CRYSTALS]]), Transition("b-01")]),
            "b-01": Room(6, [Transition("a_06")], [Location(LocationType.STRAWBERRY, 112, [[ItemName.DASH_CRYSTALS]])]),
            "a_07": Room(7, [Transition("a_08")]),
            "a_08": Room(8, [Transition("a_09"), Transition("b-02")]),
            "b-02": Room(9, [Transition("a_08")], [Location(LocationType.STRAWBERRY, 71)]),
            "a_09": Room(10, [Transition("b-03")]),
            "b-03": Room(11, [Transition("b-04")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "b-04": Room(12, [], [Location(LocationType.STRAWBERRY, 458)])
        }, LevelCategory.BEGINNER, 35
    ),
    LevelName.THE_SQUEEZE:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.SILVER_BERRY, 467, [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])], start_room=True),
            "2": Room(1, [Transition("3")]),
            "3": Room(2, [Transition("4", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 415, [[ItemName.TOUCH_SWITCH]])]),
            "4": Room(3, [Transition("5", [[ItemName.TOUCH_SWITCH]])], [Location(LocationType.STRAWBERRY, 217)]),
            "5": Room(4, [Transition("6")]),
            "6": Room(5, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 36
    ),
    LevelName.THE_SQUEEZE:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.SILVER_BERRY, 467, [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])], start_room=True),
            "2": Room(1, [Transition("3")]),
            "3": Room(2, [Transition("4", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 415, [[ItemName.TOUCH_SWITCH]])]),
            "4": Room(3, [Transition("5", [[ItemName.TOUCH_SWITCH]])], [Location(LocationType.STRAWBERRY, 217)]),
            "5": Room(4, [Transition("6")]),
            "6": Room(5, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 36
    ),
    LevelName.SEEING_IS_BELIEVING:
    Level(
        {
            "a_01": Room(0, [Transition("a_02")], [Location(LocationType.SILVER_BERRY, 53, [[ItemName.DASH_CRYSTALS]])], start_room=True),
            "a_02": Room(1, [Transition("a_03")]),
            "a_03": Room(2, [Transition("a_04")]),
            "a_04": Room(3, [Transition("a_05"), Transition("a_10")]),
            "a_05": Room(4, [Transition("a_06")]),
            "a_10": Room(5, [Transition("a_04")], excluded=True),
            "a_06": Room(6, [Transition("a_07", [[ItemName.DASH_CRYSTALS]])]),
            "a_07": Room(7, [Transition("a_08")]),
            "a_08": Room(8, [Transition("a_09")]),
            "a_09": Room(9, [Transition("a_11")]),
            "a_11": Room(10, [Transition("a_12")], [Location(LocationType.STRAWBERRY, 312)]),
            "a_12": Room(11, [], excluded=True)
        }, LevelCategory.BEGINNER, 37
    )
}