from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType

ehs_golden_list = [[ItemName.SPEED_MUSHROOM_WALL, ItemName.WHITE_DREAM_BLOCK, ItemName.DREAM_BLOCK, ItemName.SPEED_MUSHROOMS, ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.DASH_BOOST_FIELD, ItemName.FORCE_JUMP_CRYSTAL, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.BREAKER_BOX, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_REFILL_WALL, ItemName.RED_SPEED_MOSS, ItemName.BLUE_BOUNCE_MOSS, ItemName.WHITE_LINKED_TRAFFIC_BLOCK, ItemName.RED_PORTAL, ItemName.YELLOW_PORTAL, ItemName.BLUE_PORTAL, ItemName.GREEN_PORTAL, ItemName.SKY_LANTERN, ItemName.CRUMBLING_PLATFORM, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.INFINITE_DASH_MOSAIC_CRYSTAL, ItemName.KEVIN, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.BLUE_STOPWATCH, ItemName.GREEN_STOPWATCH, ItemName.GRAY_STOPWATCH, ItemName.SWAP_BLOCK, ItemName.TRAFFIC_BLOCKS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.NO_STAMINA_DASH_CRYSTAL, ItemName.CRUMBLING_PLATFORM, ItemName.WHITE_DREAM_BLOCK, ItemName.SPRINGS, ItemName.RED_PROPELLER_BLOCK, ItemName.YELLOW_PROPELLER_BLOCK, ItemName.PIPES, ItemName.JELLY_CRYSTAL, ItemName.DASH_REFILL_WALL, ItemName.TOUCH_SWITCH, ItemName.CLOUD_CRYSTAL, ItemName.JELLYFISH, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS, ItemName.DASH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.SPRINGS, ItemName.BLUE_FLOATING_FIELDS, ItemName.BLUE_FLIP_SWITCH, ItemName.GREEN_FLIP_SWITCH, ItemName.PURPLE_FLIP_SWITCH, ItemName.BADELINE_ORB, ItemName.BIRD, ItemName.PUFFER_FISH, ItemName.PURPLE_REBOUND_BUBBLE, ItemName.GREEN_BUBBLES, ItemName.BATTERY, ItemName.STOPWATCH_CRYSTAL, ItemName.DASH_CRYSTALS, ItemName.TOGGLE_SWAP_BLOCK, ItemName.SWAP_BLOCK, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.FEATHER, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS, ItemName.BUBBLE_EMITTER, ItemName.THEO_CRYSTAL, ItemName.CRUMBLING_PLATFORM, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BOWL_PUFFER, ItemName.DASH_SWITCH, ItemName.SWAP_BLOCK, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.CORE_SWITCH, ItemName.CORE_BLOCK, ItemName.SPRINGS, ItemName.CURVED_TRAFFIC_BLOCK, ItemName.PUFFER_FISH, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.MOVE_BLOCK_ACCELERATOR_FIELD, ItemName.MOVE_BLOCK_DECELERATOR_FIELD, ItemName.MOVE_BLOCK_DELETE_FIELD, ItemName.MOVE_BLOCK_REDIRECT_FIELD, ItemName.MOVING_BLOCK, ItemName.DREAM_MOVE_BLOCK, ItemName.SQUARE_BUMPER, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK]]
ehs_access_reqs = [[
    getLocationName(LevelName.A_CHANGE_IN_DIRECTION, "Agent_07", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.FLYING_BATTERY, "a-08", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SKYLINE_USURPER, "a08outro", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.CHROMATIC_COMPLEX, "a-13", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.FORTRESS_FALL, "99-end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.THE_CORE_PROBLEM, "a-11", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.PSYCHOKINETIC, "a-end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.GARDEN_OF_KHUTARA, "DanTKO_Outro", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.OVERGROWN_LINN, "a-10-end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.CLOCKWORK, "a-09", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.PLASMA_REACTOR, "a9", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.NARROW_HOLLOW, "10", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.HYDROSHOCK, "a15", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.FLOATING_POINT, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.STORM_RUNNER, "a-09", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SUMMIT_DOWNSIDE, "1", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.TIME_TROUBLE, "a-08", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SUBWAY_NEON, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.HYPNAGOGIA, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.MEANINGLESS_CONTRAPTIONS, "a-8", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.ETHEREAL_ASCENSION, "a-09", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.VINCULUM, "a-12", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.GOLDEN_ALLEYWAY, "b_05", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.MOSAIC_GARDEN, "outro", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SYSTEM_INVALIDMAPEXCEPTION, "a-end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.LUNAR_PAGODA, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.CAPER_CAVORTION, "s9", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.MADELINE_THE_BUBBLE, "Vina-End", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.POLARIS, "a8", LocationType.LEVEL_CLEAR_MINI_HEART)
]]

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
            "a-08": Room(7, [Transition("a-07"), Transition("a-08b")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
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
            "05-hub-right": Room(100, [Transition("07"), Transition("07-berry-2", [[ItemName.TOUCH_SWITCH]])], is_subregion_of="05-hub"),
            "06-crossroad": Room(5, [Transition("05-hub-right"), Transition("06-berry")]),
            "06-berry": Room(6, [Transition("06-crossroad")], [Location(LocationType.STRAWBERRY, 1635)]),
            "07": Room(7, [Transition("08", [[ItemName.TOUCH_SWITCH]]), Transition("07-berry")]),
            "07-berry": Room(8, [Transition("07")], [Location(LocationType.STRAWBERRY, 125, [[ItemName.RED_BUBBLES]])]),
            "08": Room(9, [Transition("09")]),
            "09": Room(10, [Transition("11")]),
            "11": Room(11, [Transition("99-end")]),
            "99-end": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "07-berry-2": Room(14, [Transition("06-crossroad")], [Location(LocationType.STRAWBERRY, 2055)]) 
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
            "DanTKO_01": Room(3, [Transition("DanTKO_02", [[ItemName.BLUE_BOUNCE_MOSS, ItemName.WHITE_LINKED_TRAFFIC_BLOCK, ItemName.PURPLE_PORTAL]])]),
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
            "a-00a": Room(1, [Transition("a-00-start"), Transition("a-00b")]),
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
    ),
    LevelName.FLOATING_POINT:
    Level(
        {
            "a00": Room(0, [Transition("a01"), Transition("left"), Transition("a00s")], [Location(LocationType.SILVER_BERRY, 1458, [[ItemName.CRUMBLING_PLATFORM, ItemName.BLUE_FLOATING_FIELDS, ItemName.BLUE_FLIP_SWITCH, ItemName.PURPLE_FLIP_SWITCH, ItemName.GREEN_FLIP_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.GREEN_BUBBLES]])], start_room=True),
            "left": Room(1, [Transition("a00")]),
            "a00s": Room(2, [Transition("a01")], [Location(LocationType.STRAWBERRY, 648, [[ItemName.CRUMBLING_PLATFORM, ItemName.RED_FLOATING_FIELDS]])]),
            "a01": Room(3, [Transition("a02", [[ItemName.BLUE_FLOATING_FIELDS, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a02": Room(4, [Transition("a03")]),
            "a03": Room(5, [Transition("a03b"), Transition("a03s")]),
            "a03s": Room(6, [Transition("a03b")], [Location(LocationType.STRAWBERRY, 1545, [[ItemName.CRUMBLING_PLATFORM, ItemName.RED_FLOATING_FIELDS]])]),
            "a03b": Room(7, [Transition("a04", [[ItemName.BLUE_FLIP_SWITCH, ItemName.GREEN_BUBBLES]])]),
            "a04": Room(8, [Transition("a05")]),
            "a05": Room(9, [Transition("a06"), Transition("a05?"), Transition("a05s")]),
            "a05?": Room(10, [Transition("a05")]),
            "a05s": Room(11, [Transition("a06")], [Location(LocationType.STRAWBERRY, 1868, [[ItemName.RED_BUBBLES, ItemName.RED_FLIP_SWITCH, ItemName.RED_FLOATING_FIELDS]])]),
            "a06": Room(12, [Transition("a06b", [[ItemName.GREEN_FLIP_SWITCH]])]),
            "a06b": Room(13, [Transition("a07")]),
            "a07": Room(14, [Transition("a08", [[ItemName.PURPLE_FLIP_SWITCH]])]),
            "a08": Room(15, [Transition("a09"), Transition("a08s")]),
            "a08s": Room(16, [Transition("a09")], [Location(LocationType.STRAWBERRY, 1653, [[ItemName.RED_BUBBLES, ItemName.RED_FLIP_SWITCH, ItemName.PINK_FLIP_SWITCH, ItemName.RED_FLOATING_FIELDS]])]),
            "a09": Room(17, [Transition("a09b", [[ItemName.TOUCH_SWITCH, ItemName.RED_BUBBLES, ItemName.RED_FLIP_SWITCH, ItemName.PINK_FLIP_SWITCH, ItemName.RED_FLOATING_FIELDS]]), Transition("end")]),
            "end": Room(18, [Transition("a09")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a09b": Room(19, [Transition("a10", [[ItemName.PURPLE_FLOATING_FIELDS]]), Transition("a08s")]),
            "a10": Room(20, [Transition("trueend", [[ItemName.PINK_SWITCH_BLOCK, ItemName.PURPLE_SWITCH_BLOCK, ItemName.RED_SWITCH_BLOCK]])], [Location(LocationType.STRAWBERRY, 2260, [[ItemName.PINK_SWITCH_BLOCK, ItemName.PURPLE_SWITCH_BLOCK, ItemName.RED_SWITCH_BLOCK]])]),
            "trueend": Room(21, [])
        }, LevelCategory.EXPERT, 107
    ),
    LevelName.STORM_RUNNER:
    Level(
        {
            "a-00": Room(0, [Transition("a-02", [[ItemName.CLOUDS, ItemName.CLOUD_CRYSTAL]]), Transition("a-01", [[ItemName.CLOUDS]])], [Location(LocationType.SILVER_BERRY, 302, [[ItemName.CLOUDS, ItemName.CLOUD_CRYSTAL, ItemName.JELLY_CRYSTAL, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.TOUCH_SWITCH]])], start_room=True),
            "a-01": Room(1, [Transition("a-00")], [Location(LocationType.STRAWBERRY, 1230, [[ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.PINK_CLOUDS, ItemName.CLOUD_CRYSTAL]])]),
            "a-02": Room(2, [Transition("a-04", [[ItemName.JELLY_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.SPRINGS]]), Transition("a-03", [[ItemName.JELLY_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.SPRINGS]])]),
            "a-03": Room(3, [Transition("a-02")], [Location(LocationType.STRAWBERRY, 623, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-04": Room(4, [Transition("a-05", [[ItemName.DASH_CRYSTALS]])]),
            "a-05": Room(5, [Transition("a-06")]),
            "a-06": Room(6, [Transition("a-07", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]])]),
            "a-07": Room(7, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 1308)]),
            "a-08": Room(8, [Transition("a-09")]),
            "a-09": Room(9, [Transition("a-10")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-10": Room(10, [], [Location(LocationType.STRAWBERRY, 3226, [[ItemName.JELLYFISH, ItemName.PINK_CLOUDS]])])
        }, LevelCategory.EXPERT, 108
    ),
    LevelName.SUMMIT_DOWNSIDE:
    Level(
        {
            "1": Room(0, [], [Location(LocationType.SILVER_BERRY, 99, [[ItemName.SPRINGS, ItemName.WHITE_DREAM_BLOCK]]), Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.SPRINGS, ItemName.WHITE_DREAM_BLOCK]]), Location(LocationType.STRAWBERRY, 103, [[ItemName.BADELINE_ORB, ItemName.SPRINGS, ItemName.WHITE_DREAM_BLOCK]])], start_room=True)
        }, LevelCategory.EXPERT, 109
    ),
    LevelName.TIME_TROUBLE:
    Level(
        {
            "a-00": Room(0, [Transition("a-01", [[ItemName.DASH_CRYSTALS, ItemName.STOPWATCH_CRYSTAL, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])], start_room=True),
            "a-01": Room(1, [Transition("a-02")], [Location(LocationType.SILVER_BERRY, 1243)]),
            "a-02": Room(2, [Transition("a-03")]),
            "a-03": Room(3, [Transition("a-04")]),
            "a-04": Room(4, [Transition("a-05")]),
            "a-05": Room(5, [Transition("a-06")]),
            "a-06": Room(6, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 767)]),
            "a-07": Room(7, [Transition("a-08"), Transition("a-07-b")]),
            "a-07-b": Room(8, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 814)]),
            "a-08": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 110
    ),
    LevelName.SUBWAY_NEON:
    Level(
        {
            "start": Room(0, [Transition("tutorial1"), Transition("cablog")], start_room=True),
            "cablog": Room(1, [Transition("start")], easter_egg=True),
            "tutorial1": Room(2, [Transition("a-01", [[ItemName.CURVED_TRAFFIC_BLOCK]])], [Location(LocationType.SILVER_BERRY, 2597, [[ItemName.CURVED_TRAFFIC_BLOCK, ItemName.TOUCH_SWITCH, ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.PUFFER_FISH]])]),
            "a-01": Room(3, [Transition("a-02", [[ItemName.TOUCH_SWITCH]])]),
            "a-02": Room(4, [Transition("a-03", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS]])]),
            "a-03": Room(5, [Transition("a-04", [[ItemName.PUFFER_FISH]])]),
            "a-04": Room(6, [Transition("a-05")]),
            "a-05": Room(7, [Transition("a-06"), Transition("berry")]),
            "berry": Room(8, [Transition("a-05")], [Location(LocationType.STRAWBERRY, 2061)]),
            "a-06": Room(9, [Transition("a-07")]),
            "a-07": Room(10, [Transition("end")]),
            "end": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 111
    ),
    LevelName.HYPNAGOGIA:
    Level(
        {
            "a-00": Room(0, [Transition("a-01", [[ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS]]), Transition("balls", [[ItemName.DREAM_BLOCK]])], [Location(LocationType.SILVER_BERRY, 1389, [[ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS]])], start_room=True),
            "balls": Room(1, [Transition("a-00")], easter_egg=True),
            "a-01": Room(2, [Transition("a-02")]),
            "a-02": Room(3, [Transition("a-03", [[ItemName.SPRINGS]])]),
            "a-03": Room(4, [Transition("b-01", [[ItemName.CRUMBLING_PLATFORM]]), Transition("BEWWY", [[ItemName.CRUMBLING_PLATFORM]])]),
            "BEWWY": Room(5, [Transition("a-03")], [Location(LocationType.STRAWBERRY, 2973)]),
            "b-01": Room(6, [Transition("b-02"), Transition("funny")]),
            "funny": Room(7, [Transition("b-01")], easter_egg=True),
            "b-02": Room(8, [Transition("b-03")]),
            "b-03": Room(9, [Transition("end")]),
            "end": Room(10, [Transition("space ruins")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "space ruins": Room(11, [Transition("end")], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 112
    ),
    LevelName.MEANINGLESS_CONTRAPTIONS:
    Level(
        {
            "a-1": Room(0, [Transition("a-2", [[ItemName.TOUCH_SWITCH, ItemName.BOWL_PUFFER, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_SWITCH, ItemName.SPRINGS, ItemName.PUFFER_FISH]])], start_room=True),
            "a-2": Room(1, [Transition("a-3", [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SWAP_BLOCK]])], [Location(LocationType.SILVER_BERRY, 4234, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SWAP_BLOCK]]), Location(LocationType.STRAWBERRY, 1994, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SWAP_BLOCK]])]),
            "a-3": Room(2, [Transition("a-4")]),
            "a-4": Room(3, [Transition("a-5")]),
            "a-5": Room(4, [Transition("a-5-b")]),
            "a-5-b": Room(5, [Transition("a-6"), Transition("a-5-berry"), Transition("cabob")]),
            "a-5-berry": Room(6, [Transition("a-5-b")], [Location(LocationType.STRAWBERRY, 2883)]),
            "cabob": Room(7, [Transition("a-5-b")], easter_egg=True),
            "a-6": Room(8, [Transition("a-7"), Transition("a-6-berry")]),
            "a-6-berry": Room(9, [Transition("a-6")], [Location(LocationType.STRAWBERRY, 6528)]),
            "a-7": Room(10, [Transition("a-8"), Transition("Hi Ru")]),
            "Hi Ru": Room(11, [Transition("a-7")]),
            "a-8": Room(12, [Transition("ema-1")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "ema-1": Room(13, [Transition("a-8")], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 113
    ),
    LevelName.ETHEREAL_ASCENSION:
    Level(
        {
            "a-000": Room(0, [Transition("a-00", [[ItemName.SKY_LANTERN]])], start_room=True),
            "a-00": Room(1, [Transition("a-01", [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])]),
            "a-01": Room(2, [Transition("a-02", [[ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 3844, [[ItemName.DOUBLE_DASH_CRYSTALS]]), Location(LocationType.SILVER_BERRY, 10204, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS]])]),
            "a-02": Room(3, [Transition("a-03", [[ItemName.CRUMBLING_PLATFORM]])]),
            "a-03": Room(4, [Transition("a-04", [[ItemName.SPRINGS]])]),
            "a-04": Room(5, [Transition("a-05"), Transition("a-04b")]),
            "a-04b": Room(6, [Transition("a-04")], [Location(LocationType.STRAWBERRY, 4662)]),
            "a-05": Room(7, [Transition("a-06"), Transition("a-05b")]),
            "a-05b": Room(8, [Transition("a-05")], [Location(LocationType.STRAWBERRY, 911)]),
            "a-06": Room(9, [Transition("a-08")]),
            "a-08": Room(10, [Transition("a-07")]),
            "a-07": Room(11, [Transition("a-09"), Transition("a-07bb")]),
            "a-07bb": Room(12, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 2773)]),
            "a-09": Room(13, [Transition("a-08b")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-08b": Room(14, [Transition("a-09")], [Location(LocationType.STRAWBERRY, 3960)])
        }, LevelCategory.EXPERT, 114
    ),
    LevelName.VINCULUM:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.GREEN_BUBBLES, ItemName.TOUCH_SWITCH, ItemName.JELLYFISH]]), Transition("berry1", [[ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.GREEN_BUBBLES]])], [Location(LocationType.SILVER_BERRY, 1134, [[getKeyDoorName(LevelName.VINCULUM, "a-06", 443), ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.GREEN_BUBBLES, ItemName.TOUCH_SWITCH, ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.DREAM_BLOCK, ItemName.DASH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS]])], start_room=True),
            "berry1": Room(1, [Transition("a-01")], [Location(LocationType.STRAWBERRY, 1148, [[ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "a-02": Room(2, [Transition("a-03", [[ItemName.DASH_CRYSTALS, ItemName.DREAM_BLOCK, ItemName.DASH_SWITCH]]), Transition("secret4")]),
            "secret4": Room(3, [Transition("a-02")], easter_egg=True),
            "a-03": Room(4, [Transition("a-04"), Transition("berry2", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "berry2": Room(5, [Transition("a-03")], [Location(LocationType.STRAWBERRY, 4951)]),
            "a-04": Room(6, [Transition("a-05"), Transition("secret3")]),
            "secret3": Room(7, [Transition("a-04")], easter_egg=True),
            "a-05": Room(8, [Transition("a-06")]),
            "a-06": Room(9, [Transition("a-08", [[getKeyDoorName(LevelName.VINCULUM, "a-06", 443)]]), Transition("a-07")], key_door_ids=[443]),
            "a-07": Room(10, [Transition("a-06")], [Location(LocationType.KEY, 722, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-08": Room(11, [Transition("a-09", [[ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("berry3")]),
            "berry3": Room(12, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 1696, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-09": Room(13, [Transition("a-10"), Transition("secret5")]),
            "secret5": Room(14, [Transition("a-09")], easter_egg=True),
            "a-10": Room(15, [Transition("a-11"), Transition("berry4")]),
            "berry4": Room(16, [Transition("a-10")], [Location(LocationType.STRAWBERRY, 2892)]),
            "a-11": Room(17, [Transition("secret1"), Transition("a-12")]),
            "a-12": Room(18, [Transition("a-11")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.BIRD]])]),
            "secret1": Room(19, [Transition("secret2", [[ItemName.BIRD]])], easter_egg=True),
            "secret2": Room(20, [], easter_egg_difficult=True)
        }, LevelCategory.EXPERT, 115
    ),
    LevelName.GOLDEN_ALLEYWAY:
    Level(
        {
            "a_01": Room(0, [Transition("a_02", [[ItemName.TOGGLE_SWAP_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.SWAP_BLOCK]])], [Location(LocationType.SILVER_BERRY, 3742, [[ItemName.FEATHER, ItemName.TOUCH_SWITCH, ItemName.SPRINGS, ItemName.TOGGLE_SWAP_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.SWAP_BLOCK]])], start_room=True),
            "a_02": Room(1, [Transition("a_04", [[ItemName.DASH_CRYSTALS]]), Transition("a_03")]),
            "a_03": Room(2, [Transition("a_02")], [Location(LocationType.STRAWBERRY, 1, [[ItemName.DASH_CRYSTALS]])]),
            "a_04": Room(3, [Transition("a_05", [[ItemName.TOUCH_SWITCH, ItemName.SPRINGS]])]),
            "a_05": Room(4, [Transition("a_06")]),
            "a_06": Room(5, [Transition("b_01"), Transition("a_07")]),
            "a_07": Room(6, [Transition("a_06")], [Location(LocationType.STRAWBERRY, 1443)]),
            "b_01": Room(7, [Transition("b_02", [[ItemName.FEATHER]])]),
            "b_02": Room(8, [Transition("b_03")]),
            "b_03": Room(9, [Transition("b_04")]),
            "b_04": Room(10, [Transition("b_05")]),
            "b_05": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 116
    ),
    LevelName.MOSAIC_GARDEN:
    Level(
        {
            "intro": Room(0, [Transition("a-01", [[ItemName.INFINITE_DASH_MOSAIC_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.KEVIN]])], [Location(LocationType.SILVER_BERRY, 1030, [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.INFINITE_DASH_MOSAIC_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.KEVIN]])], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS]]), Transition("a-01-01", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS]])]),
            "a-01-01": Room(2, [Transition("a-01")], [Location(LocationType.STRAWBERRY, 694)]),
            "a-02": Room(3, [Transition("a-03")]),
            "a-03": Room(4, [Transition("outro"), Transition("secret"), Transition("a-03-01")]),
            "secret": Room(5, [Transition("a-03")], easter_egg=True),
            "a-03-01": Room(6, [Transition("a-03")], [Location(LocationType.STRAWBERRY, 1120)]),
            "outro": Room(7, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 117
    ),
    LevelName.SYSTEM_INVALIDMAPEXCEPTION:
    Level(
        {
            "a-0": Room(0, [Transition("a-1")], start_room=True),
            "a-1": Room(1, [Transition("a-2"), Transition("ldm")]),
            "ldm": Room(2, [Transition("a-1")]),
            "a-2": Room(3, [Transition("a-3", [[ItemName.DREAM_BLOCK]])], [Location(LocationType.SILVER_BERRY, 1545, [[ItemName.DASH_CRYSTALS, ItemName.DREAM_BLOCK]]), Location(LocationType.STRAWBERRY, 46, [[ItemName.DREAM_BLOCK]])]),
            "a-3": Room(4, [Transition("a-4", [[ItemName.DASH_CRYSTALS]])]),
            "a-4": Room(5, [Transition("a-5")], [Location(LocationType.STRAWBERRY, 312)]),
            "a-5": Room(6, [Transition("a-6")]),
            "a-6": Room(7, [Transition("a-7")], [Location(LocationType.STRAWBERRY, 2093)]),
            "a-7": Room(8, [Transition("a-8")]),
            "a-8": Room(9, [Transition("a-end"), Transition("a-b1")]),
            "a-b1": Room(10, [Transition("a-8")], [Location(LocationType.STRAWBERRY, 1490)]),
            "a-end": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 118
    ),
    LevelName.LUNAR_PAGODA:
    Level(
        {
            "0": Room(0, [Transition("1-1", [[ItemName.BLUE_STOPWATCH]])], [Location(LocationType.SILVER_BERRY, 2777, [[ItemName.BLUE_STOPWATCH]])], start_room=True),
            "1-1": Room(1, [Transition("1-2", [[ItemName.MOVING_PLATFORM]])]),
            "1-2": Room(2, [Transition("2", [[ItemName.MOVING_BLOCK, ItemName.KEVIN, ItemName.CRUMBLING_PLATFORM]])]),
            "2": Room(3, [Transition("2-2", [[ItemName.SWAP_BLOCK, ItemName.GRAY_STOPWATCH]])]),
            "2-2": Room(4, [Transition("3-1", [[ItemName.DASH_CRYSTALS]])]),
            "3-1": Room(5, [Transition("3-2", [[ItemName.TRAFFIC_BLOCKS]])]),
            "3-2": Room(6, [Transition("5", [[ItemName.TOUCH_SWITCH, ItemName.GREEN_STOPWATCH, ItemName.SPRINGS]])]),
            "5": Room(7, [Transition("6"), Transition("5-1")]),
            "5-1": Room(8, [Transition("5")], [Location(LocationType.STRAWBERRY, 64)]),
            "6": Room(9, [Transition("7")]),
            "7": Room(10, [Transition("8", [[ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("7-1")]),
            "7-1": Room(11, [Transition("7")], [Location(LocationType.STRAWBERRY, 1425)]),
            "8": Room(12, [Transition("end")]),
            "end": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 119
    ),
    LevelName.CAPER_CAVORTION:
    Level(
        {
            "s1": Room(0, [Transition("s2", [[ItemName.TRAFFIC_BLOCKS]]), Transition("s2b", [[ItemName.TRAFFIC_BLOCKS]]), Transition("s1a", [[ItemName.TRAFFIC_BLOCKS]])], start_room=True),
            "s2b": Room(1, [Transition("s1")], [Location(LocationType.STRAWBERRY, 1452, [[ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DASH_SPRING]])]),
            "s2b-right": Room(100, [Transition("s3")], [Location(LocationType.STRAWBERRY, 1826)], is_subregion_of="s2b"),
            "s1a": Room(2, [Transition("s1")]),
            "s2": Room(3, [Transition("s3", [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 144, [[ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DASH_CRYSTALS]])]),
            "s3": Room(4, [Transition("s4"), Transition("s2b-right")]),
            "s4": Room(5, [Transition("s5")]),
            "s5": Room(6, [Transition("s6"), Transition("s5b")]),
            "s5b": Room(7, [Transition("s5")], [Location(LocationType.STRAWBERRY, 876)]),
            "s6": Room(8, [Transition("s7")]),
            "s7": Room(9, [Transition("s8")]),
            "s8": Room(10, [Transition("s9"), Transition("s8b")]),
            "s8b": Room(11, [Transition("s8")], [Location(LocationType.STRAWBERRY, 562, [[ItemName.MOMENTUM_SPRING]])]),
            "s9": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 120
    ),
    LevelName.MADELINE_THE_BUBBLE:
    Level(
        {
            "Vina-00": Room(0, [Transition("Vina-01", [[ItemName.BUBBLE_EMITTER, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 7208, [[ItemName.THEO_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.PUFFER_FISH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.BUBBLE_EMITTER, ItemName.DASH_CRYSTALS]])], start_room=True),
            "Vina-01": Room(1, [Transition("Vina-02", [[ItemName.PUFFER_FISH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM]])]),
            "Vina-02": Room(2, [Transition("Vina-03", [[ItemName.TOUCH_SWITCH]])]),
            "Vina-03": Room(3, [Transition("Vina-04")]),
            "Vina-04": Room(4, [Transition("Vina-05")]),
            "Vina-05": Room(5, [Transition("Vina-06"), Transition("Vina-05~b")]),
            "Vina-05~b": Room(6, [Transition("Vina-05")], [Location(LocationType.STRAWBERRY, 2315)]),
            "Vina-06": Room(7, [Transition("Vina-07")]),
            "Vina-07": Room(8, [Transition("Vina-08")]),
            "Vina-08": Room(9, [Transition("Vina-09", [[ItemName.THEO_CRYSTAL]]), Transition("Vina-08~b", [[ItemName.THEO_CRYSTAL]])]),
            "Vina-08~b": Room(10, [Transition("Vina-08")], [Location(LocationType.STRAWBERRY, 10784)]),
            "Vina-09": Room(11, [Transition("Vina-End")]),
            "Vina-End": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 121
    ),
    LevelName.POLARIS:
    Level(
        {
            "a0": Room(0, [Transition("a1", [[ItemName.PUFFER_FISH, ItemName.BOWL_PUFFER, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS]])], start_room=True),
            "a1": Room(1, [Transition("a2", [[ItemName.SPRINGS]])], [Location(LocationType.SILVER_BERRY, 2057, [[ItemName.TOUCH_SWITCH, ItemName.JELLYFISH, ItemName.GREEN_BUBBLES, ItemName.SPRINGS]])]),
            "a2": Room(2, [Transition("a3", [[ItemName.JELLYFISH, ItemName.GREEN_BUBBLES]])]),
            "a3": Room(3, [Transition("a4")]),
            "a4": Room(4, [Transition("a6"), Transition("a4b")]),
            "a4b": Room(5, [Transition("a4")], [Location(LocationType.STRAWBERRY, 4076)]),
            "a6": Room(6, [Transition("a7", [[ItemName.TOUCH_SWITCH]])]),
            "a7": Room(7, [Transition("a8"), Transition("a7b")]),
            "a7b": Room(8, [Transition("a7")], [Location(LocationType.STRAWBERRY, 2044)]),
            "a8": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.EXPERT, 122
    ),
    LevelName.STARFRUIT_SUPERNOVA:
    Level(
        {
            "a00_intro1": Room(0, [Transition("a00_intro2")], start_room=True),
            "a00_intro2": Room(1, [Transition("a01_jackal")]),
            "a01_jackal": Room(2, [Transition("a02_skunkynator", [[ItemName.SQUARE_BUMPER, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK]])], [Location(LocationType.GOLDEN_BERRY, 1628, ehs_golden_list)]),
            "a02_skunkynator": Room(3, [Transition("a03_pansear", [[ItemName.DASH_CRYSTALS]])]),
            "a03_pansear": Room(4, [Transition("a04_agent")]),
            "a04_agent": Room(5, [Transition("a05_flamecrafter", [[ItemName.MOVE_BLOCK_ACCELERATOR_FIELD, ItemName.MOVE_BLOCK_DECELERATOR_FIELD, ItemName.MOVE_BLOCK_DELETE_FIELD, ItemName.MOVE_BLOCK_REDIRECT_FIELD, ItemName.MOVING_BLOCK, ItemName.DREAM_MOVE_BLOCK]])]),
            "a05_flamecrafter": Room(6, [Transition("b00_intro", [[ItemName.CRUMBLING_PLATFORM, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "b00_intro": Room(7, [Transition("b01_stotch")], checkpoint="Expunge"),
            "b01_stotch": Room(8, [Transition("b02_alt_alt", [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DASH_SPRING]])]),
            "b02_alt_alt": Room(9, [Transition("b02_nyan")]),
            "b02_nyan": Room(10, [Transition("b02_alt", [[ItemName.CURVED_TRAFFIC_BLOCK, ItemName.PUFFER_FISH]])]),
            "b02_alt": Room(11, [Transition("b03_banana")]),
            "b03_banana": Room(12, [Transition("b04_powerav", [[ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.CORE_SWITCH, ItemName.CORE_BLOCK, ItemName.SPRINGS]])]),
            "b04_powerav": Room(13, [Transition("b05_vina", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BOWL_PUFFER, ItemName.DASH_SWITCH, ItemName.SWAP_BLOCK]])]),
            "b05_vina": Room(14, [Transition("b06_transition", [[ItemName.BUBBLE_EMITTER, ItemName.THEO_CRYSTAL, ItemName.CRUMBLING_PLATFORM]])]),
            "b06_transition": Room(15, [Transition("c00_intro")]),
            "c00_intro": Room(16, [Transition("c01_redboule")], checkpoint="Atomize"),
            "c01_redboule": Room(17, [Transition("c02_moladan", [[ItemName.TOGGLE_SWAP_BLOCK, ItemName.SWAP_BLOCK, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.FEATHER, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS]])]),
            "c02_moladan": Room(18, [Transition("c03_alice", [[ItemName.STOPWATCH_CRYSTAL, ItemName.DASH_CRYSTALS]])]),
            "c03_alice": Room(19, [Transition("c04_fonda", [[ItemName.PURPLE_REBOUND_BUBBLE, ItemName.GREEN_BUBBLES, ItemName.BATTERY]])]),
            "c04_fonda": Room(20, [Transition("c05_kaerra", [[ItemName.BADELINE_ORB, ItemName.BIRD, ItemName.PUFFER_FISH]])]),
            "c05_kaerra": Room(21, [Transition("c06_fall", [[ItemName.BLUE_FLOATING_FIELDS, ItemName.BLUE_FLIP_SWITCH, ItemName.GREEN_FLIP_SWITCH, ItemName.PURPLE_FLIP_SWITCH]])]),
            "c06_fall": Room(22, [Transition("d00_intro")]),
            "d00_intro": Room(23, [Transition("d01_ru"), Transition("c06_fall"), Transition("d000_eeva")], checkpoint="Extinguish"),
            "d000_eeva": Room(24, [Transition("d00_intro")], easter_egg=True),
            "d01_ru": Room(25, [Transition("d02_lethargicdoggo", [[ItemName.JELLYFISH, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS, ItemName.DASH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.SPRINGS]])]),
            "d02_lethargicdoggo": Room(26, [Transition("d03_appels", [[ItemName.JELLY_CRYSTAL, ItemName.DASH_REFILL_WALL, ItemName.TOUCH_SWITCH, ItemName.CLOUD_CRYSTAL]])]),
            "d03_appels": Room(27, [Transition("d04_yoshachobi7", [[ItemName.RED_PROPELLER_BLOCK, ItemName.YELLOW_PROPELLER_BLOCK, ItemName.PIPES]])]),
            "d04_yoshachobi7": Room(28, [Transition("d05_warp", [[ItemName.BOWL_PUFFER]])]),
            "d05_warp": Room(29, [Transition("e00_intro")]),
            "e00_intro": Room(30, [Transition("e01_linj"), Transition("d05_warp")], checkpoint="Demolish"),
            "e01_linj": Room(31, [Transition("e02_aspar", [[ItemName.WHITE_DREAM_BLOCK, ItemName.SPRINGS]])]),
            "e02_aspar": Room(32, [Transition("e03_spirialis", [[ItemName.NO_STAMINA_DASH_CRYSTAL, ItemName.CRUMBLING_PLATFORM]])]),
            "e03_spirialis": Room(33, [Transition("e04_scroogle", [[ItemName.BLUE_STOPWATCH, ItemName.GREEN_STOPWATCH, ItemName.GRAY_STOPWATCH, ItemName.SWAP_BLOCK, ItemName.TRAFFIC_BLOCKS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "e04_scroogle": Room(34, [Transition("e05_itsabrody", [[ItemName.INFINITE_DASH_MOSAIC_CRYSTAL, ItemName.KEVIN, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])]),
            "e05_itsabrody": Room(35, [Transition("e06_transition")]),
            "e06_transition": Room(36, [Transition("f00_intro")]),
            "f00_intro": Room(37, [Transition("f01_quantumspaceman")], checkpoint="Obliterate"),
            "f01_quantumspaceman": Room(38, [Transition("f02_dantko", [[ItemName.SKY_LANTERN, ItemName.CRUMBLING_PLATFORM, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "f02_dantko": Room(39, [Transition("f02.5_xolimono", [[ItemName.RED_SPEED_MOSS, ItemName.BLUE_BOUNCE_MOSS, ItemName.WHITE_LINKED_TRAFFIC_BLOCK, ItemName.RED_PORTAL, ItemName.YELLOW_PORTAL, ItemName.BLUE_PORTAL, ItemName.GREEN_PORTAL]])]),
            "f02.5_xolimono": Room(40, [Transition("f03_hivemindsrule")]),
            "f03_hivemindsrule": Room(41, [Transition("f04_alt", [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_REFILL_WALL]])]),
            "f04_alt": Room(42, [Transition("f04_archra", [[ItemName.BREAKER_BOX]])]),
            "f04_archra": Room(43, [Transition("f04_alt_2", [[ItemName.DASH_BOOST_FIELD, ItemName.FORCE_JUMP_CRYSTAL, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "f04_alt_2": Room(44, [Transition("f05_cabob")]),
            "f05_cabob": Room(45, [Transition("f06_cabob", [[ItemName.DREAM_BLOCK, ItemName.SPEED_MUSHROOMS, ItemName.RED_LINKED_TRAFFIC_BLOCK]])]),
            "f06_cabob": Room(46, [Transition("f07_butcherberries", [[ItemName.SPEED_MUSHROOM_WALL, ItemName.WHITE_DREAM_BLOCK]])]),
            "f07_butcherberries": Room(47, [Transition("f07_xplosives")]),
            "f07_xplosives": Room(48, [Transition("f07_legs")]),
            "f07_legs": Room(49, [Transition("f07_and_you")]),
            "f07_and_you": Room(50, [], [Location(LocationType.CRYSTAL_HEART)])
        }, LevelCategory.EXPERT, 123, ehs_access_reqs, heartside = True
    )
}