from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType

expert_levels_sj : dict[LevelName, Level] = {
    LevelName.A_CHANGE_IN_DIRECTION:
    Level(
        {
            "Ru_and_AV_and_Zucchini_Are_Cool": Room(0, [Transition("Agent_00")], easter_egg=True),
            "Agent_00": Room(1, [Transition("Agent_00a", [[ItemName.MOVING_BLOCK, ItemName.MOVE_BLOCK_ACCELERATOR_FIELD, ItemName.DASH_CRYSTALS, ItemName.MOVE_BLOCK_DELETE_FIELD, ItemName.TOUCH_SWITCH, ItemName.MOVE_BLOCK_DECELERATOR_FIELD]]), Transition("Ru_and_AV_and_Zucchini_Are_Cool")], start_room=True),
            "Agent_00a": Room(2, [Transition("Agent_01")], [Location(LocationType.SILVER_BERRY, 537, [[ItemName.DREAM_MOVE_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.MOVE_BLOCK_REDIRECT_FIELD, ItemName.MOVING_BLOCK, ItemName.MOVE_BLOCK_ACCELERATOR_FIELD, ItemName.DASH_CRYSTALS, ItemName.MOVE_BLOCK_DELETE_FIELD, ItemName.TOUCH_SWITCH, ItemName.MOVE_BLOCK_DECELERATOR_FIELD]])]),
            "Agent_01": Room(3, [Transition("Agent_02", [[ItemName.MOVE_BLOCK_REDIRECT_FIELD]])]),
            "Agent_02": Room(4, [Transition("Agent_03")]),
            "Agent_03": Room(5, [Transition("Agent_04", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Agent_04": Room(6, [Transition("Agent_05", [[ItemName.DREAM_MOVE_BLOCK]]), Transition("Agent_04b", [[ItemName.DREAM_MOVE_BLOCK]])]),
            "Agent_04b": Room(7, [Transition("Agent_04")], [Location(LocationType.STRAWBERRY, 383)]),
            "Agent_05": Room(8, [Transition("Agent_06")]),
            "Agent_06": Room(9, [Transition("Agent_07")]),
            "Agent_07": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 94
    ),
    LevelName.FLYING_BATTERY:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.BATTERY, ItemName.GREEN_BUBBLES, ItemName.PURPLE_REBOUND_BUBBLE, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])], start_room=True),
            "a-02": Room(1, [Transition("a-03", [[ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 2001, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "a-03": Room(2, [Transition("a-04")]),
            "a-04": Room(3, [Transition("a-05")]),
            "a-05": Room(4, [Transition("a-06", [[ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "a-06": Room(5, [Transition("a-07")]),
            "a-07": Room(6, [Transition("a-08")]),
            "a-08": Room(7, [Transition("a-07")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-08b": Room(8, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 2295)])
        }, LevelCategory.EXPERT, 95
    ),
    LevelName.SKYLINE_USURPER:
    Level(
        {
            "INTRO1": Room(0, [Transition("INTRO2", [[ItemName.PIPES, ItemName.TOUCH_SWITCH]])], start_room=True),
            "INTRO2": Room(1, [Transition("a01", [[ItemName.RED_PROPELLER_BLOCK, ItemName.YELLOW_PROPELLER_BLOCK, ItemName.BADELINE_ORB, ItemName.DASH_CRYSTALS]])]),
            "a01": Room(2, [Transition("a01b")], [Location(LocationType.SILVER_BERRY, 1856, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a01b": Room(3, [Transition("a02")]),
            "a02": Room(4, [Transition("a03")]),
            "a03": Room(5, [Transition("a04")]),
            "a04": Room(6, [Transition("a05", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a05": Room(7, [Transition("a06new")]),
            "a06new": Room(8, [Transition("a07")]),
            "a07": Room(9, [Transition("a08outro"), Transition("a07b")]),
            "a07b": Room(10, [Transition("a07")], [Location(LocationType.STRAWBERRY, 2070)]),
            "a08outro": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 96
    ),
    LevelName.CHROMATIC_COMPLEX:
    Level(
        {
            "a-00": Room(0, [Transition("a-01", [[ItemName.DASH_BOOST_FIELD, ItemName.FORCE_JUMP_CRYSTAL]])], start_room=True),
            "a-01": Room(1, [Transition("a-02")], [Location(LocationType.SILVER_BERRY, 241)]),
            "a-02": Room(2, [Transition("a-03")], [Location(LocationType.STRAWBERRY, 3506)]),
            "a-03": Room(3, [Transition("a-04")]),
            "a-04": Room(4, [Transition("a-05", [[ItemName.DASH_CRYSTALS]])]),
            "a-05": Room(5, [Transition("a-06", [[ItemName.TRAFFIC_BLOCKS]])]),
            "a-06": Room(6, [Transition("a-07", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "a-07": Room(7, [Transition("a-08")]),
            "a-08": Room(8, [Transition("a-09")]),
            "a-09": Room(9, [Transition("a-10")]),
            "a-10": Room(10, [Transition("a-11")]),
            "a-11": Room(11, [Transition("a-12", [[ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "a-12": Room(12, [Transition("a-13", [[ItemName.DASH_REFILL_WALL]])]),
            "a-13": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART), Location(LocationType.STRAWBERRY, 1052)])
        }, LevelCategory.EXPERT, 97
    ),
    LevelName.FORTRESS_FALL:
    Level(
        {
            "00-intro": Room(0, [Transition("00-intro-cutscene", [[ItemName.NO_STAMINA_DASH_CRYSTAL, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "00-intro-cutscene": Room(1, [Transition("01")], [Location(LocationType.SILVER_BERRY, 1235, [[ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "01": Room(2, [Transition("03", [[ItemName.DASH_CRYSTALS]])]),
            "03": Room(3, [Transition("05-hub")]),
            "05-hub": Room(4, [Transition("06-crossroad")]),
            "05-hub-right": Room(5, [Transition("07"), Transition("07-berry-2", [[ItemName.TOUCH_SWITCH]])], is_subregion_of="05-hub"),
            "06-crossroad": Room(5, [Transition("05-hub-right"), Transition("06-berry")]),
            "06-berry": Room(6, [Transition("06-crossroad")], [Location(LocationType.STRAWBERRY, 1635)]),
            "07": Room(7, [Transition("08", [[ItemName.TOUCH_SWITCH]]), Transition("07-berry")]),
            "07-berry": Room(8, [Transition("07")], [Location(LocationType.STRAWBERRY, 125, [[ItemName.RED_BUBBLES]])]),
            "08": Room(9, [Transition("09")]),
            "09": Room(10, [Transition("11")]),
            "11": Room(11, [Transition("99-end")]),
            "99-end": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "07-berry-2": Room(14, [Transition("06")], [Location(LocationType.STRAWBERRY, 2055)]) 
        }, LevelCategory.EXPERT, 98
    ),
    LevelName.THE_CORE_PROBLEM:
    Level(
        {
            "a-01": Room(0, [Transition("a-02")], [Location(LocationType.SILVER_BERRY, 4416, [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.CORE_SWITCH]])], start_room=True),
            "a-02": Room(1, [Transition("a-03", [[ItemName.DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.CORE_SWITCH]])]),
            "a-03": Room(2, [Transition("a-04")]),
            "a-04": Room(3, [Transition("a-05"), Transition("a-04b")]),
            "a-04b": Room(4, [Transition("a-04")], [Location(LocationType.STRAWBERRY, 980, [[ItemName.CORE_BLOCK, ItemName.SPRINGS]])]),
            "a-05": Room(5, [Transition("a-06", [[ItemName.TRAFFIC_BLOCKS]])]),
            "a-06": Room(6, [Transition("a-07", [[ItemName.TOUCH_SWITCH]]), Transition("a-06b", [[ItemName.TOUCH_SWITCH]])]),
            "a-06b": Room(7, [Transition("a-06")], [Location(LocationType.STRAWBERRY, 1664, [[ItemName.CORE_BLOCK]])]),
            "a-07": Room(8, [Transition("a-08", [[ItemName.SPRINGS]])]),
            "a-08": Room(9, [Transition("a-09")]),
            "a-09": Room(10, [Transition("a-10"), Transition("a-09b")]),
            "a-09b": Room(11, [Transition("a-09")], [Location(LocationType.STRAWBERRY, 2912, [[ItemName.CORE_BLOCK]])]),
            "a-10": Room(12, [Transition("a-11")]),
            "a-11": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 99
    ),
    LevelName.PSYCHOKINETIC:
    Level(
        {
            "a-start": Room(0, [Transition("a-00"), Transition("s-Path of Plane")], [Location(LocationType.SILVER_BERRY, 2403, [[ItemName.SPEED_MUSHROOM_WALL, ItemName.SPEED_MUSHROOM_WALL, ItemName.DREAM_BLOCK, ItemName.WHITE_DREAM_BLOCK, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])], start_room=True),
            "s-Path of Plane": Room(1, [Transition("a-start")], easter_egg_difficult=True),
            "a-00": Room(2, [Transition("a-01", [[ItemName.SPEED_MUSHROOMS, ItemName.DREAM_BLOCK]])]),
            "a-01": Room(3, [Transition("a-02", [[ItemName.TOUCH_SWITCH]])]),
            "a-02": Room(4, [Transition("a-03", [[ItemName.SPEED_MUSHROOM_WALL, ItemName.DASH_CRYSTALS]]), Transition("s-Flushed Down")]),
            "s-Flushed Down": Room(5, [Transition("a-02"), Transition("s-Water Splash")], easter_egg=True),
            "a-03": Room(6, [Transition("a-04"), Transition("a-03x")]),
            "a-03x": Room(7, [Transition("a-03")], [Location(LocationType.STRAWBERRY, 570)]),
            "a-04": Room(8, [Transition("a-05", [[ItemName.WHITE_DREAM_BLOCK]])]),
            "a-05": Room(9, [Transition("a-06")]),
            "a-06": Room(10, [Transition("a-07"), Transition("s-Swamp Ascent")]),
            "s-Swamp Ascent": Room(11, [Transition("a-06"), Transition("s-Shrek Swamp")], easter_egg_difficult=True),
            "a-07": Room(12, [Transition("a-08")]),
            "a-08": Room(13, [Transition("a-09"), Transition("a-08x")]),
            "a-08x": Room(14, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 1876)]),
            "a-09": Room(15, [Transition("a-10")]),
            "a-10": Room(16, [Transition("a-end"), Transition("a-10x")]),
            "a-10x": Room(17, [Transition("a-10")], [Location(LocationType.STRAWBERRY, 2917, [[ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.PURPLE_LINKED_TRAFFIC_BLOCK]])]),
            "a-end": Room(18, [Transition("a-end2")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-end2": Room(19, [Transition("s-True Ending")], easter_egg_difficult=True),
            "s-True Ending": Room(20, [Transition("s-Graveyard")], easter_egg_difficult=True),
            "s-Graveyard": Room(21, [], easter_egg_difficult=True),
            "s-Water Splash": Room(23, [], easter_egg=True),
            "s-Shrek Swamp": Room(24, [], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 100
    ),
    LevelName.GARDEN_OF_KHUTARA:
    Level(
        {
            "DanTKO_Intro": Room(0, [Transition("DanTKO_01"), Transition("DanTKO_Monolith_1"), Transition("DanTKO_Plane")], start_room=True),
            "DanTKO_Monolith_1": Room(1, [Transition("DanTKO_Intro"), Transition("Aperture_Mountain Relic")], easter_egg=True),
            "DanTKO_Plane": Room(2, [Transition("DanTKO_Intro")], easter_egg=True),
            "DanTKO_01": Room(3, [Transition("DanTKO_02", [[ItemName.BLUE_BOUNCE_MOSS, ItemName.TAN_LINKED_TRAFFIC_BLOCK, ItemName.PURPLE_PORTAL]])]),
            "DanTKO_02": Room(4, [Transition("DanTKO_blueTutorial_2", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.YELLOW_PORTAL, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 2536, [[ItemName.RED_PORTAL, ItemName.TOUCH_SWITCH, ItemName.RED_SPEED_MOSS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.YELLOW_PORTAL, ItemName.DASH_CRYSTALS]])]),
            "DanTKO_blueTutorial_2": Room(5, [Transition("DanTKO_03")]),
            "DanTKO_03": Room(6, [Transition("DanTKO_04", [[ItemName.TOUCH_SWITCH]])]),
            "DanTKO_04": Room(7, [Transition("DanTKO_05", [[ItemName.RED_SPEED_MOSS]])]),
            "DanTKO_05": Room(8, [Transition("DanTKO_06")]),
            "DanTKO_06": Room(9, [Transition("DanTKO_06b")]),
            "DanTKO_06b": Room(10, [Transition("DanTKO_07"), Transition("DanTKO_Berry01")]),
            "DanTKO_Berry01": Room(11, [Transition("DanTKO_06b")], [Location(LocationType.STRAWBERRY, 2078)]),
            "DanTKO_07": Room(12, [Transition("DanTKO_08")]),
            "DanTKO_08": Room(13, [Transition("DanTKO_09")]),
            "DanTKO_09": Room(14, [Transition("DanTKO_Outro", [[ItemName.RED_PORTAL]]), Transition("DanTKO_Berry02")]),
            "DanTKO_Berry02": Room(15, [Transition("DanTKO_09")], [Location(LocationType.STRAWBERRY, 331)]),
            "DanTKO_Outro": Room(16, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "Aperture_Mountain Relic": Room(18, [Transition("Aperture_Mountain Relic_EXIT")], easter_egg_difficult=True),
            "Aperture_Mountain Relic_EXIT": Room(19, [Transition("DanTKO_Intro")], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 101
    ),
    LevelName.OVERGROWN_LINN:
    Level(
        {
            "a-00-start": Room(0, [Transition("a-01"), Transition("a-00a")], [Location(LocationType.SILVER_BERRY, 965, [[ItemName.CRUMBLING_PLATFORM, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.MOVING_BLOCK]])], start_room=True),
            "a-00a": Room(1, [Transition("a-00-start"), Transition("a-00-b")]),
            "a-01": Room(2, [Transition("a-02", [[ItemName.CRUMBLING_PLATFORM, ItemName.DREAM_BLOCK]]), Transition("a-01_berry", [[ItemName.CRUMBLING_PLATFORM, ItemName.DREAM_BLOCK]])]),
            "a-01_berry": Room(3, [Transition("a-01")], [Location(LocationType.STRAWBERRY, 1575, [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])]),
            "a-02": Room(4, [Transition("a-03", [[ItemName.DASH_CRYSTALS]])]),
            "a-03": Room(5, [Transition("a-04", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-04": Room(6, [Transition("a-05", [[ItemName.MOVING_BLOCK]])]),
            "a-05": Room(7, [Transition("a-06")]),
            "a-06": Room(8, [Transition("a-07")]),
            "a-07": Room(9, [Transition("a-08"), Transition("a-07_berry")]),
            "a-07_berry": Room(10, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 2751)]),
            "a-08": Room(11, [Transition("a-09"), Transition("a-08_berry")]),
            "a-08_berry": Room(12, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 3479)]),
            "a-09": Room(13, [Transition("a-10-end")], [Location(LocationType.STRAWBERRY, 1524)]),
            "a-10-end": Room(14, [Transition("a-10_berry")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-10_berry": Room(15, [Transition("a-10a")], [Location(LocationType.STRAWBERRY, 3513)]),
            "a-10a": Room(16, [], easter_egg=True),
            "a-00c": Room(18, [Transition("a-00b"), Transition("a-00y")], easter_egg_difficult=True),
            "a-00b": Room(19, [Transition("a-00c")], easter_egg_difficult=True),
            "a-00y": Room(20, [Transition("a-00c")], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 102
    ),
    LevelName.CLOCKWORK:
    Level(
        {
            "a-00": Room(0, [Transition("a-01", [[ItemName.TOUCH_SWITCH]])], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 12888, [[ItemName.PUFFER_FISH, ItemName.DASH_SWITCH, ItemName.BADELINE_ORB, ItemName.BIRD, ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-02": Room(2, [Transition("a-03", [[ItemName.BADELINE_ORB, ItemName.BIRD]])]),
            "a-03": Room(3, [Transition("a-04")]),
            "a-04": Room(4, [Transition("a-05", [[ItemName.DASH_SWITCH]])]),
            "a-05": Room(5, [Transition("a-06"), Transition("a-05b")]),
            "a-05b": Room(6, [Transition("a-05")], [Location(LocationType.STRAWBERRY, 2707, [[ItemName.JELLYFISH]])]),
            "a-06": Room(7, [Transition("a-07", [[ItemName.PUFFER_FISH]])]),
            "a-07": Room(8, [Transition("a-08"), Transition("a-07b"), Transition("secret")]),
            "a-07b": Room(9, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 2134)]),
            "secret": Room(10, [Transition("a-07")], easter_egg=True),
            "a-08": Room(11, [Transition("a-09")]),
            "a-09": Room(12, [Transition("a-09b")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-09b": Room(13, [Transition("a-09")], [Location(LocationType.STRAWBERRY, 13047)])
        }, LevelCategory.EXPERT, 103
    ),
    LevelName.PLASMA_REACTOR:
    Level(
        {
            "a1": Room(0, [Transition("a2", [[ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.SILVER_BERRY, 1193, [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.DASH_CRYSTALS, ItemName.DASH_REFILL_WALL]])], start_room=True),
            "a2": Room(1, [Transition("a3", [[ItemName.DASH_CRYSTALS, ItemName.DASH_REFILL_WALL]])]),
            "a3": Room(2, [Transition("a4")]),
            "a4": Room(3, [Transition("a5")]),
            "a5": Room(4, [Transition("a6")]),
            "a6": Room(5, [Transition("a7", [[ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "a7": Room(6, [Transition("a8")]),
            "a8": Room(7, [Transition("b1"), Transition("a9")]),
            "a9": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "b1": Room(9, [Transition("bones_room"), Transition("a8")], [Location(LocationType.STRAWBERRY, 2100)]),
            "bones_room": Room(10, [Transition("b1")], easter_egg=True)
        }, LevelCategory.EXPERT, 104
    ),
    LevelName.NARROW_HOLLOW:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.KEVIN]])], [Location(LocationType.SILVER_BERRY, 2340, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.KEVIN, ItemName.TOUCH_SWITCH, ItemName.DASH_SWITCH, ItemName.SPRINGS]])], start_room=True),
            "2": Room(1, [Transition("3", [[ItemName.TOUCH_SWITCH]])], [Location(LocationType.STRAWBERRY, 235)]),
            "3": Room(2, [Transition("4", [[ItemName.DASH_CRYSTALS]])]),
            "4": Room(3, [Transition("5")]),
            "5": Room(4, [Transition("6")]),
            "6": Room(5, [Transition("7"), Transition("berry")], [Location(LocationType.STRAWBERRY, 334, [[getKeyDoorName(LevelName.NARROW_HOLLOW, "6", 333)]])], key_door_ids=[333]),
            "berry": Room(6, [Transition("6")], [Location(LocationType.KEY, 317)]),
            "7": Room(7, [Transition("8")]),
            "8": Room(8, [Transition("9")]),
            "9": Room(9, [Transition("10", [[ItemName.SPRINGS]])]),
            "10": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 105
    ),
    LevelName.HYDROSHOCK:
    Level(
        {
            "a01": Room(0, [Transition("a04"), Transition("a02", [[ItemName.SQUARE_BUMPER]])], [Location(LocationType.SILVER_BERRY, 2489, [[ItemName.SQUARE_BUMPER, ItemName.TOUCH_SWITCH]])], start_room=True),
            "a02": Room(1, [Transition("a01"), Transition("a03")], easter_egg=True),
            "a04": Room(2, [Transition("a05", [[ItemName.SQUARE_BUMPER]])]),
            "a05": Room(3, [Transition("a06")]),
            "a06": Room(4, [Transition("a07", [[ItemName.TOUCH_SWITCH]])]),
            "a07": Room(5, [Transition("a08")], [Location(LocationType.STRAWBERRY, 181)]),
            "a08": Room(6, [Transition("a09")]),
            "a09": Room(7, [Transition("a10")]),
            "a10": Room(8, [Transition("a12"), Transition("a10b")]),
            "a10b": Room(9, [Transition("a10")], [Location(LocationType.STRAWBERRY, 1187)]),
            "a12": Room(10, [Transition("a14"), Transition("a12b")]),
            "a12b": Room(11, [Transition("a12")], [Location(LocationType.STRAWBERRY, 129)]),
            "a14": Room(12, [Transition("a15")]),
            "a15": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a03": Room(15, [], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 106
    )
}