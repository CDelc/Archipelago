from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType

bhs_golden = [[ItemName.BIG_YELLOW_BUTTON, ItemName.BLUE_TRAFFIC_CASSETTE, ItemName.PINK_TRAFFIC_CASSETTE, ItemName.BLUE_CASSETTE, ItemName.PUZZLE_KEVIN, ItemName.SOAP_BUBBLE, ItemName.DASHLESS_SPRING, ItemName.GREEN_SWITCH_BLOCK, ItemName.ORANGE_SWITCH_BLOCK, ItemName.SWITCH_BLOCK_SWITCH, ItemName.TRIPLE_JUMP_REFILL, ItemName.SINGLE_JUMP_REFILL, ItemName.CORE_BLOCK, ItemName.TRIPLE_BOOST_FLOWER, ItemName.PIPES, ItemName.STRAWBERRY_JAM, ItemName.DASH_CRYSTAL_SHARDS, ItemName.MOVING_BLOCK, ItemName.BLUE_TIME_CRYSTAL, ItemName.PINK_CLOUDS, ItemName.LOOP_BLOCK, ItemName.BOUNCE_DREAM_BLOCK, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK, ItemName.DREAM_DASH_CRYSTAL, ItemName.CRUMBLING_PLATFORM, ItemName.GRAVITY_FIELD, ItemName.DREAM_BLOCK, ItemName.DOUBLE_DASH_DREAM_BLOCK, ItemName.FEATHER, ItemName.BADELINE_ORB, ItemName.DASH_TRAFFIC_BLOCK, ItemName.DASH_CRYSTALS, ItemName.SWAP_BLOCK, ItemName.TOUCH_SWITCH, ItemName.TRAFFIC_BLOCKS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.INTRO_CRUSHER, ItemName.SPRINGS]]
bhs_access = [[getLocationName(LevelName.LOOPY_LAGOON, "c-17", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.FOREST_PATH, "a-20", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.DRIVEWAY_DID_YOU_IN, "09- Fin", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.AZURE_CAVERNS, "08", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.CASSETTE_CLIFFS, "12", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SOAP, "heart", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.OVER_THE_CITY, "17", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.TROPHOSPHERE, "c_03_end", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.CORESAKEN_CITY, "b-03", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.THE_SQUEEZE, "6", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SEEING_IS_BELIEVING, "a_09", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SWITCHTUBE_VISTA, "a14_Outro", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.POTENTIAL_FOR_ANYTHING, "HEART", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.A_GIFT_FROM_THE_STARS, "End Cabin", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.COLLAPSING_SKYLINE, "a-07", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.STRAWBERRY_ORCHARD, "a-13z", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.MIDNIGHT_SPIRE, "a_07", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.PAINT, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.DROPZLE, "10 - Downfall", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.ROSE_GARDEN, "q09", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.TREEHIVE, "skeleton_outro", LocationType.LEVEL_CLEAR_MINI_HEART)]]

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
            "04- Head Trauma": Room(5, [Transition("05- Boing")], [Location(LocationType.STRAWBERRY, 717)]),
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
            "11b": Room(15, [Transition("11")], [Location(LocationType.STRAWBERRY, 3857)]),
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
            "16": Room(17, [Transition("17"), Transition("RouteA-3"), Transition("RouteB-1")]),
            "17": Room(18, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.DASH_CRYSTALS]])]),
            "RouteB-1": Room(20, [Transition("RouteB-2"), Transition("RouteB-3"), Transition("RouteB-4")], [Location(LocationType.STRAWBERRY, 823)]),
            "RouteB-2": Room(21, [Transition("RouteB-1")]),
            "RouteB-3": Room(22, [Transition("RouteB-1")]),
            "RouteB-4": Room(23, [Transition("RouteB-1"), Transition("16")]),
            "RouteA-2": Room(24, [Transition("RouteA-1"), Transition("RouteA-3")]),
            "RouteA-1": Room(25, [Transition("RouteA-2"), Transition("16")]),
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
    LevelName.SEEING_IS_BELIEVING:
    Level(
        {
            "a_01": Room(0, [Transition("a_02")], [Location(LocationType.SILVER_BERRY, 53, [[ItemName.DASH_CRYSTALS]])], start_room=True),
            "a_02": Room(1, [Transition("a_03")]),
            "a_03": Room(2, [Transition("a_04")]),
            "a_04": Room(3, [Transition("a_05"), Transition("a_10")]),
            "a_05": Room(4, [Transition("a_06")]),
            "a_10": Room(5, [Transition("a_04")], easter_egg=True),
            "a_06": Room(6, [Transition("a_07", [[ItemName.DASH_CRYSTALS]])]),
            "a_07": Room(7, [Transition("a_08")]),
            "a_08": Room(8, [Transition("a_09")]),
            "a_09": Room(9, [Transition("a_11")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a_11": Room(10, [Transition("a_12")], [Location(LocationType.STRAWBERRY, 312)]),
            "a_12": Room(11, [], easter_egg=True)
        }, LevelCategory.BEGINNER, 37
    ),
    LevelName.SWITCHTUBE_VISTA:
    Level(
        {
            "a01": Room(0, [Transition("a02", [[ItemName.PIPES]])], [Location(LocationType.SILVER_BERRY, 252, [[ItemName.PIPES, ItemName.ORANGE_SWITCH_BLOCK, ItemName.SWITCH_BLOCK_SWITCH, ItemName.GREEN_SWITCH_BLOCK]])], start_room=True),
            "a02": Room(1, [Transition("a02_b", [[ItemName.ORANGE_SWITCH_BLOCK, ItemName.SWITCH_BLOCK_SWITCH]])]),
            "a02_b": Room(2, [Transition("a03", [[ItemName.GREEN_SWITCH_BLOCK]])]),
            "a03": Room(3, [Transition("a04", [[ItemName.DASH_CRYSTALS]]), Transition("a03_s")]),
            "a03_s": Room(4, [Transition("a03")], [Location(LocationType.STRAWBERRY, 253, [[ItemName.DASH_CRYSTALS]])]),
            "a04": Room(5, [Transition("a05")]),
            "a05": Room(6, [Transition("a06")]),
            "a06": Room(7, [Transition("a07"), Transition("a06_s")]),
            "a06_s": Room(8, [Transition("a06")], [Location(LocationType.STRAWBERRY, 739)]),
            "a07": Room(9, [Transition("a08")]),
            "a08": Room(10, [Transition("a09-enter")]),
            "a09": Room(11, [Transition("a10"), Transition("a09_s")]),
            "a09-enter": Room(100, [Transition("a09_b")], is_subregion_of="a09"),
            "a09_s": Room(12, [Transition("a09")], [Location(LocationType.STRAWBERRY, 387)]),
            "a09_b": Room(13, [Transition("a09_b_s"), Transition("a09")]),
            "a09_b_s": Room(14, [Transition("a09_b")], [Location(LocationType.STRAWBERRY, 388)]),
            "a10": Room(15, [Transition("a11")]),
            "a11": Room(16, [Transition("a12")]),
            "a-11-orange": Room(101, [Transition("a14_Outro")], is_subregion_of="a11"),
            "a12": Room(17, [Transition("a13-top"), Transition("a12_s")]),
            "a12_s": Room(18, [Transition("a12")], [Location(LocationType.STRAWBERRY, 984)]),
            "a13": Room(19, [Transition("a-11-orange")]),
            "a13-top": Room(102, [Transition("a13_b")], is_subregion_of="a13"),
            "a13_b": Room(20, [Transition("a13")]),
            "a14_Outro": Room(21, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 38
    ),
    LevelName.POTENTIAL_FOR_ANYTHING:
    Level(
        {
            "SS2-0": Room(0, [Transition("SS2-1", [[ItemName.GRAVITY_FIELD]])], [Location(LocationType.SILVER_BERRY, 786, [[ItemName.GRAVITY_FIELD, ItemName.DASH_CRYSTALS, ItemName.MOVING_PLATFORM, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "SS2-1": Room(1, [Transition("SS2-2", [[ItemName.DASH_CRYSTALS]])]),
            "SS2-2": Room(2, [Transition("SS2-3")]),
            "SS2-3": Room(3, [Transition("SS2-4")]),
            "SS2-4": Room(4, [Transition("SS2-5b", [[ItemName.CRUMBLING_PLATFORM, ItemName.MOVING_PLATFORM]])]),
            "SS2-5b": Room(5, [Transition("SS2-7", [[ItemName.TOUCH_SWITCH]]), Transition("SS2-6")]),
            "SS2-6": Room(6, [Transition("SS2-5b")], [Location(LocationType.STRAWBERRY, 754)]),
            "SS2-7": Room(7, [Transition("HUB")]),
            "HUB": Room(8, [Transition("FinalChallenge"), Transition("WZ-0"), Transition("Lab-0")]),
            "FinalChallenge": Room(9, [Transition("ESCAPE")]),
            "ESCAPE": Room(10, [Transition("HEART")]),
            "HEART": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "WZ-0": Room(13, [Transition("WZ-1")]),
            "WZ-1": Room(14, [Transition("WZ-2")]),
            "WZ-2": Room(15, [Transition("WZ-3a")]),
            "WZ-3a": Room(16, [Transition("WZ-4")]),
            "WZ-4": Room(17, [Transition("WZ-5a")], [Location(LocationType.STRAWBERRY, 339)]),
            "WZ-5a": Room(18, [Transition("WZ-Tele")]),
            "WZ-Tele": Room(19, [Transition("HUB")]),
            "Lab-0": Room(20, [Transition("Lab-1")]),
            "Lab-1": Room(21, [Transition("Lab-2")]),
            "Lab-2": Room(22, [Transition("Lab-3")]),
            "Lab-3": Room(23, [Transition("Lab-4")]),
            "Lab-4": Room(24, [Transition("Lab-5")]),
            "Lab-5": Room(25, [Transition("Lab-6"), Transition("Lab-5berry")]),
            "Lab-6": Room(26, [Transition("Lab-secret"), Transition("Lab-7")]),
            "Lab-7": Room(27, [Transition("Lab-Tele")]),
            "Lab-Tele": Room(28, [Transition("HUB")]),
            "Lab-5berry": Room(29, [Transition("Lab-3")], [Location(LocationType.STRAWBERRY, 731)]),
            "Lab-secret": Room(30, [Transition("Lab-6")], easter_egg=True)
        }, LevelCategory.BEGINNER, 39
    ),
    LevelName.A_GIFT_FROM_THE_STARS:
    Level(
        {
            "Intro A": Room(0, [Transition("Intro B")], start_room=True),
            "Intro B": Room(1, [Transition("Double Vision", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 99, [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS]]), Location(LocationType.SILVER_BERRY, 278, [[ItemName.MOVING_BLOCK, ItemName.TOUCH_SWITCH, ItemName.BLUE_TIME_CRYSTAL, ItemName.DASH_CRYSTAL_SHARDS, ItemName.DASH_CRYSTALS, ItemName.SPRINGS, getKeyDoorName(LevelName.A_GIFT_FROM_THE_STARS, "Timestop Intro", 237)]])]),
            "Double Vision": Room(2, [Transition("Waiting Room", [[ItemName.DASH_CRYSTAL_SHARDS]])], [Location(LocationType.KEY, 947, [[ItemName.TOUCH_SWITCH]])]),
            "Waiting Room": Room(3, [Transition("Timestop Intro")], [Location(LocationType.STRAWBERRY, 633, [[ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.A_GIFT_FROM_THE_STARS, "Timestop Intro", 237)]])]),
            "Timestop Intro": Room(4, [Transition("Timestop Intro Again", [[ItemName.BLUE_TIME_CRYSTAL, ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.A_GIFT_FROM_THE_STARS, "Timestop Intro", 237)]]), Transition("Shuffle", [[ItemName.TOUCH_SWITCH]])], key_door_ids=[237]),
            "Timestop Intro Again": Room(5, [Transition("Stepping Stone", [[ItemName.MOVING_BLOCK]])]),
            "Stepping Stone": Room(6, [Transition("Fork")]),
            "Fork": Room(7, [Transition("Seeded Berry")]),
            "Seeded Berry": Room(8, [Transition("Staircase"), Transition("Easter Egg Puzzle")], [Location(LocationType.STRAWBERRY, 1072)]),
            "Easter Egg Puzzle": Room(9, [Transition("Seeded Berry")], [Location(LocationType.KEY, 103)], easter_egg=True),
            "Staircase": Room(10, [Transition("End")]),
            "End": Room(11, [Transition("End Cabin")], key_door_ids=[1090]),
            "End Cabin": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "Shuffle": Room(14, [Transition("Feedback Loop"), Transition("Double Vision")], [Location(LocationType.STRAWBERRY, 1223)]),
            "Feedback Loop": Room(15, [], [Location(LocationType.STRAWBERRY, 899)])
        }, LevelCategory.BEGINNER, 40
    ),
    LevelName.COLLAPSING_SKYLINE:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.SWAP_BLOCK]])], [Location(LocationType.SILVER_BERRY, 235, [[ItemName.TOUCH_SWITCH, ItemName.SWAP_BLOCK]])], start_room=True),
            "a-02": Room(1, [Transition("a-04"), Transition("a-02-b")]),
            "a-02-b": Room(2, [Transition("a-02")], [Location(LocationType.STRAWBERRY, 170)]),
            "a-04": Room(3, [Transition("a-03"), Transition("a-05b")]),
            "a-05b": Room(4, [Transition("a-04")]),
            "a-03": Room(5, [Transition("a-05")]),
            "a-05": Room(6, [Transition("a-06", [[ItemName.TOUCH_SWITCH]]), Transition("a-05s")]),
            "a-05s": Room(7, [Transition("a-05")], easter_egg=True),
            "a-06": Room(8, [Transition("a-07")]),
            "a-07": Room(9, [Transition("a-08")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART), Location(LocationType.STRAWBERRY, 999)]),
            "a-08": Room(10, [Transition("a-08s")], [Location(LocationType.STRAWBERRY, 862)]),
            "a-08s": Room(11, [Transition("a-08")], easter_egg=True)
        }, LevelCategory.BEGINNER, 41
    ),
    LevelName.STRAWBERRY_ORCHARD:
    Level(
        {
            "a-00": Room(0, [Transition("a-01z", [[ItemName.PIPES, ItemName.STRAWBERRY_JAM]])], [Location(LocationType.SILVER_BERRY, 1045, [[ItemName.PIPES, ItemName.STRAWBERRY_JAM, ItemName.SPRINGS]])], start_room=True),
            "a-01z": Room(1, [Transition("a-02y")]),
            "a-02y": Room(2, [Transition("a-03y", [[ItemName.SPRINGS]])], [Location(LocationType.STRAWBERRY, 822, [[ItemName.SPRINGS]])]),
            "a-03y": Room(3, [Transition("a-04z")]),
            "a-04z": Room(4, [Transition("a-05z")]),
            "a-05z": Room(5, [Transition("a-07z"), Transition("a-06z")]),
            "a-06z": Room(6, [Transition("a-05z")], [Location(LocationType.STRAWBERRY, 1737)]),
            "a-07z": Room(7, [Transition("a-08z")], [Location(LocationType.STRAWBERRY, 447)]),
            "a-08z": Room(8, [Transition("a-09z")]),
            "a-09z": Room(9, [Transition("a-11z")]),
            "a-11z": Room(10, [Transition("a-12z"), Transition("a-10z")]),
            "a-10z": Room(11, [Transition("a-11z")], [Location(LocationType.STRAWBERRY, 794)]),
            "a-12z": Room(12, [Transition("a-13z")], [Location(LocationType.STRAWBERRY, 431)]),
            "a-13z": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 42
    ),
    LevelName.MIDNIGHT_SPIRE:
    Level(
        {
            "a_00": Room(0, [Transition("a_01")], start_room=True),
            "a_01": Room(1, [Transition("a_02", [[ItemName.CLOUDS, ItemName.GREEN_BUBBLES]])], [Location(LocationType.STRAWBERRY, 80, [[ItemName.CLOUDS, ItemName.GREEN_BUBBLES, ItemName.PINK_CLOUDS]]), Location(LocationType.SILVER_BERRY, 1462, [[ItemName.GREEN_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.SPRINGS]])]),
            "a_02": Room(2, [Transition("a_03")]),
            "a_03": Room(3, [Transition("a_04", [[ItemName.SPRINGS]])], [Location(LocationType.STRAWBERRY, 521)]),
            "a_04": Room(4, [Transition("a_05")], [Location(LocationType.STRAWBERRY, 624)]),
            "a_05": Room(5, [Transition("a_06", [[ItemName.PINK_CLOUDS]])]),
            "a_06": Room(6, [Transition("a_07")]),
            "a_07": Room(7, [], [Location(LocationType.STRAWBERRY, 1474), Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 43
    ),
    LevelName.PAINT:
    Level(
        {
            "intro": Room(0, [Transition("a-00", [[ItemName.BIG_YELLOW_BUTTON]])], [Location(LocationType.SILVER_BERRY, 2544, [[ItemName.BIG_YELLOW_BUTTON, ItemName.BADELINE_ORB, ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "a-00": Room(1, [Transition("a-01")]),
            "a-01": Room(2, [Transition("a-02")]),
            "a-02": Room(3, [Transition("a-03")]),
            "a-03": Room(4, [Transition("a-04b"), Transition("a-03b"), Transition("a-04a")]),
            "a-03b": Room(5, [Transition("a-03")], easter_egg=True),
            "a-04a": Room(6, [Transition("a-05")]),
            "a-04b": Room(7, [Transition("a-05", [[ItemName.SPRINGS]])]),
            "a-05": Room(8, [Transition("a-06a"), Transition("a-06b")]),
            "a-06b": Room(9, [Transition("a-07b", [[ItemName.CRUMBLING_PLATFORM]])]),
            "a-06a": Room(10, [Transition("a-07a"), Transition("a-06c")]),
            "a-06c": Room(11, [Transition("a-06a")], easter_egg=True),
            "a-07a": Room(12, [Transition("a-08")]),
            "a-08": Room(13, [Transition("a-09"), Transition("gay")]),
            "a-07b": Room(14, [Transition("a-08")]),
            "gay": Room(15, [Transition("a-08")], easter_egg=True),
            "a-09": Room(16, [Transition("a-10")]),
            "a-10": Room(17, [Transition("b-00")]),
            "b-00": Room(18, [Transition("b-01"), Transition("b-berry00")]),
            "b-berry00": Room(19, [Transition("b-00")], [Location(LocationType.STRAWBERRY, 2675)]),
            "b-01": Room(20, [Transition("b-02")]),
            "b-02": Room(21, [Transition("b-03")]),
            "b-03": Room(22, [Transition("b-04"), Transition("b-berry1")]),
            "b-berry1": Room(23, [Transition("b-03"), Transition("b-tribute", [[getKeyDoorName(LevelName.PAINT, "b-berry1", 4235)]])], [Location(LocationType.STRAWBERRY, 471)], key_door_ids=[4235]),
            "b-berry1-subroom": Room(100, [Transition("b-05")], [Location(LocationType.KEY, 4429)], is_subregion_of="b-berry1", easter_egg=True),
            "b-04": Room(24, [Transition("b-05"), Transition("b-berry2")]),
            "b-berry2": Room(25, [Transition("b-04")], [Location(LocationType.STRAWBERRY, 1172)]),
            "b-05": Room(26, [Transition("b-06"), Transition("b-berry3"), Transition("b-berry1-subroom")]),
            "b-berry3": Room(27, [Transition("b-05")], [Location(LocationType.STRAWBERRY, 1163)]),
            "b-06": Room(28, [Transition("b-07"), Transition("b-06b")]),
            "b-06b": Room(29, [Transition("b-06")], easter_egg=True),
            "b-07": Room(30, [Transition("b-08")]),
            "b-08": Room(31, [Transition("b-09")]),
            "b-09": Room(32, [Transition("b-10", [[ItemName.SPRINGS]])]),
            "b-10": Room(33, [Transition("b-11", [[ItemName.BADELINE_ORB]])]),
            "b-11": Room(34, [Transition("bus")]),
            "bus": Room(35, [Transition("c-intro")]),
            "c-intro": Room(36, [Transition("c-00")]),
            "c-00": Room(37, [Transition("c-01", [[ItemName.CRUMBLING_PLATFORM]])]),
            "c-01": Room(38, [Transition("c-02")]),
            "c-02": Room(39, [Transition("c-03")]),
            "c-03": Room(40, [Transition("c-04")]),
            "c-04": Room(41, [Transition("c-05")]),
            "c-05": Room(42, [Transition("c-06")]),
            "c-06": Room(43, [Transition("end")]),
            "end": Room(44, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "b-tribute": Room(46, [Transition("b-berry1")])
        }, LevelCategory.BEGINNER, 44
    ),
    LevelName.DROPZLE:
    Level(
        {
            "00 - Overpass": Room(0, [Transition("01 - Lockdown", [[ItemName.PUZZLE_KEVIN, ItemName.TOUCH_SWITCH]])], [Location(LocationType.SILVER_BERRY, 187, [[ItemName.PUZZLE_KEVIN, ItemName.TOUCH_SWITCH]])], start_room=True),
            "01 - Lockdown": Room(1, [Transition("02 - Breadth")]),
            "02 - Breadth": Room(2, [Transition("03 - Labyrinth")]),
            "03 - Labyrinth": Room(3, [Transition("04 - Widdershins"), Transition("03a - Portcullis")]),
            "03a - Portcullis": Room(4, [Transition("03 - Labyrinth")], [Location(LocationType.STRAWBERRY, 989)]),
            "04 - Widdershins": Room(5, [Transition("05 - Symmetry"), Transition("04a - Correlation")]),
            "04a - Correlation": Room(6, [Transition("04 - Widdershins"), Transition("04b - Alcove")], [Location(LocationType.STRAWBERRY, 10)]),
            "05 - Symmetry": Room(7, [Transition("06 - Socket"), Transition("06a - Shackle")]),
            "06a - Shackle": Room(8, [Transition("06 - Socket")], [Location(LocationType.STRAWBERRY, 821)]),
            "06 - Socket": Room(9, [Transition("07 - Ferry")]),
            "07 - Ferry": Room(10, [Transition("08 - Daedalus")]),
            "08 - Daedalus": Room(11, [Transition("09 - Perpendicular"), Transition("08a - Reunion")]),
            "08a - Reunion": Room(12, [Transition("08 - Daedalus")], [Location(LocationType.STRAWBERRY, 1383)]),
            "09 - Perpendicular": Room(13, [Transition("10 - Downfall")]),
            "10 - Downfall": Room(14, [Transition("secret")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "secret": Room(15, [Transition("10 - Downfall")], easter_egg=True),
            "04b - Alcove": Room(17, [Transition("04a - Correlation")], [Location(LocationType.STRAWBERRY, 330)])
        }, LevelCategory.BEGINNER, 45
    ),
    LevelName.ROSE_GARDEN:
    Level(
        {
            "q00": Room(0, [Transition("q01")], [Location(LocationType.SILVER_BERRY, 1786, [[ItemName.TRIPLE_BOOST_FLOWER, ItemName.SPRINGS]])], start_room=True),
            "q01": Room(1, [Transition("q02", [[ItemName.TRIPLE_BOOST_FLOWER]])]),
            "q02": Room(2, [Transition("q06", [[ItemName.SPRINGS]])]),
            "q03": Room(3, [Transition("q07")]),
            "q04": Room(4, [Transition("q05")]),
            "q05": Room(5, [Transition("q03")]),
            "q06": Room(6, [Transition("q04")]),
            "q07": Room(7, [Transition("q08")]),
            "q08": Room(8, [Transition("q09")]),
            "q09": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 46
    ),
    LevelName.TREEHIVE:
    Level(
        {
            "skeleton_00": Room(0, [Transition("skeleton_01", [[ItemName.TOUCH_SWITCH, ItemName.BOUNCE_DREAM_BLOCK, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK]])], start_room=True),
            "skeleton_01": Room(1, [Transition("skeleton_02")], [Location(LocationType.SILVER_BERRY, 1109, [[ItemName.TOUCH_SWITCH, ItemName.BOUNCE_DREAM_BLOCK, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK, ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LINKED_TRAFFIC_BLOCK, ItemName.DASH_CRYSTALS]])]),
            "skeleton_02": Room(2, [Transition("skeleton_03", [[ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.DASH_CRYSTALS]]), Transition("skeleton_02_berry", [[ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.DASH_CRYSTALS]])]),
            "skeleton_02_berry": Room(3, [Transition("skeleton_02")], [Location(LocationType.STRAWBERRY, 591, [[ItemName.TOGGLE_SWAP_BLOCK]])]),
            "skeleton_03": Room(4, [Transition("skeleton_04")]),
            "skeleton_04": Room(5, [Transition("skeleton_05", [[ItemName.GREEN_LINKED_TRAFFIC_BLOCK]])], [Location(LocationType.STRAWBERRY, 159)]),
            "skeleton_05": Room(6, [Transition("skeleton_outro")]),
            "skeleton_outro": Room(7, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.BEGINNER, 47
    ),
    LevelName.BLUEBERRY_BAY:
    Level(
        {
            "cp1_heartside_intro": Room(0, [Transition("cp1_21_heartside_Bing_Over_Google")], start_room=True),
            "cp1_21_heartside_Bing_Over_Google": Room(1, [Transition("cp1_20_heartside_hyperlife", [[ItemName.TRAFFIC_BLOCKS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.INTRO_CRUSHER, ItemName.SPRINGS]])], [Location(LocationType.GOLDEN_BERRY, 5338, bhs_golden)]),
            "cp1_20_heartside_hyperlife": Room(2, [Transition("cp1_19_heartside_cellularAutomaton", [[ItemName.SWAP_BLOCK, ItemName.TOUCH_SWITCH]])]),
            "cp1_19_heartside_cellularAutomaton": Room(3, [Transition("cp1_18_heartside_Eclipse", [[ItemName.DASH_TRAFFIC_BLOCK, ItemName.DASH_CRYSTALS]])]),
            "cp1_18_heartside_Eclipse": Room(4, [Transition("cp2_checkpoint", [[ItemName.DREAM_BLOCK, ItemName.DOUBLE_DASH_DREAM_BLOCK, ItemName.FEATHER, ItemName.BADELINE_ORB]])]),
            "cp2_checkpoint": Room(5, [Transition("cp2-17-heartside_NotYourBadeline")], checkpoint="Basin"),
            "cp2-17-heartside_NotYourBadeline": Room(6, [Transition("cp2-16-heartside_snas", [[ItemName.DASH_CRYSTALS, ItemName.SWAP_BLOCK]])]),
            "cp2-16-heartside_snas": Room(7, [Transition("cp2_15_heartside_frozenflygone_a", [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH]])]),
            "cp2_15_heartside_frozenflygone_a": Room(8, [Transition("cp2_15_heartside_frozenflygone_b", [[ItemName.GRAVITY_FIELD]])]),
            "cp2_15_heartside_frozenflygone_b": Room(9, [Transition("cp2_15_heartside_frozenflygone_c")]),
            "cp2_15_heartside_frozenflygone_c": Room(10, [Transition("cp2_15_heartside_frozenflygone_d")]),
            "cp2_15_heartside_frozenflygone_d": Room(11, [Transition("cp3_checkpoint", [[ItemName.CRUMBLING_PLATFORM]])]),
            "cp3_checkpoint": Room(12, [Transition("cp3_14_heartside_asterisk")], checkpoint="Tranquility"),
            "cp3_14_heartside_asterisk": Room(13, [Transition("cp3_13_heartside_skeleton", [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.DREAM_DASH_CRYSTAL]])]),
            "cp3_13_heartside_skeleton": Room(14, [Transition("cp3_12_heartside_coffe", [[ItemName.BOUNCE_DREAM_BLOCK, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK, ItemName.TOUCH_SWITCH]])]),
            "cp3_12_heartside_coffe": Room(15, [Transition("cp3_11_heartside_joltik", [[ItemName.LOOP_BLOCK, ItemName.GREEN_BUBBLES]])]),
            "cp3_11_heartside_joltik": Room(16, [Transition("cp4_checkpoint", [[ItemName.PINK_CLOUDS]])]),
            "cp4_checkpoint": Room(17, [Transition("cp4_10_heartside_Hanky")], checkpoint="Jade"),
            "cp4_10_heartside_Hanky": Room(18, [Transition("cp4_09_heartside_jadeturtle", [[ItemName.DASH_CRYSTAL_SHARDS, ItemName.MOVING_BLOCK, ItemName.BLUE_TIME_CRYSTAL, ItemName.TOUCH_SWITCH]])]),
            "cp4_09_heartside_jadeturtle": Room(19, [Transition("cp4_08_heartside_quinnigan", [[ItemName.STRAWBERRY_JAM, ItemName.SPRINGS, ItemName.PIPES]])]),
            "cp4_08_heartside_quinnigan": Room(20, [Transition("cp5_checkpoint", [[ItemName.TRIPLE_BOOST_FLOWER, ItemName.DASH_CRYSTALS]])]),
            "cp5_checkpoint": Room(21, [Transition("cp5_07_heartside_voliver9")], checkpoint="Overgrowth"),
            "cp5_07_heartside_voliver9": Room(22, [Transition("cp5_06_heartside_CoupCritik1", [[ItemName.CORE_BLOCK, ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH]])]),
            "cp5_06_heartside_CoupCritik1": Room(23, [Transition("cp5_06_heartside_CoupCritik2", [[ItemName.SINGLE_JUMP_REFILL]])]),
            "cp5_06_heartside_CoupCritik2": Room(24, [Transition("cp5_06_heartside_CoupCritik3", [[ItemName.TRIPLE_JUMP_REFILL]])]),
            "cp5_06_heartside_CoupCritik3": Room(25, [Transition("cp5_05_Flagpole1up_Heartside")]),
            "cp5_05_Flagpole1up_Heartside": Room(26, [Transition("cp5_04_heartside_circumplex", [[ItemName.PIPES, ItemName.GREEN_SWITCH_BLOCK, ItemName.ORANGE_SWITCH_BLOCK, ItemName.SWITCH_BLOCK_SWITCH, ItemName.DASH_CRYSTALS]])]),
            "cp5_04_heartside_circumplex": Room(27, [Transition("cp6_checkpoint", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SOAP_BUBBLE, ItemName.TOUCH_SWITCH, ItemName.MOVING_BLOCK, ItemName.DASHLESS_SPRING]])]),
            "cp6_checkpoint": Room(28, [Transition("cp6_03_heartside_awheyaway")], checkpoint="Harbor"),
            "cp6_03_heartside_awheyaway": Room(29, [Transition("cp6_02_heartside_Ceph", [[ItemName.PUZZLE_KEVIN, ItemName.TOUCH_SWITCH]])]),
            "cp6_02_heartside_Ceph": Room(30, [Transition("cp6_03_heartside_Moss_1", [[ItemName.BLUE_TRAFFIC_CASSETTE, ItemName.PINK_TRAFFIC_CASSETTE, ItemName.BLUE_CASSETTE, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS]])]),
            "cp6_03_heartside_Moss_1": Room(31, [Transition("cp6_03_heartside_Moss_2", [[ItemName.BADELINE_ORB, ItemName.BIG_YELLOW_BUTTON]])]),
            "cp6_03_heartside_Moss_2": Room(32, [Transition("heartside_outro")]),
            "heartside_outro": Room(33, [], [Location(LocationType.CRYSTAL_HEART)])
        }, LevelCategory.BEGINNER, 48, bhs_access, heartside = True
    )
}