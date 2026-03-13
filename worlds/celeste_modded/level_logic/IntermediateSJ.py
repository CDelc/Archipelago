from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType

ihs_golden_list = [[ItemName.SOAP_BUBBLE, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CORE_BLOCK, ItemName.SPRINGS, ItemName.VERTIGO_LINKED_TELEPORT, ItemName.PUSH_STATION_BLOCK, ItemName.PULL_STATION_BLOCK, ItemName.TRACK_SWITCH_BOX, ItemName.PURPLE_DASHLESS_BUBBLE, ItemName.BADELINE_ORB, ItemName.GREEN_BUBBLES, ItemName.PUSH_BLOCK, ItemName.HONEY_BUBBLES, getKeyDoorName(LevelName.RASPBERRY_ROOTS, "cp2-3-glowwoomii", 7656), ItemName.DREAM_BLOCK, ItemName.CRUMBLING_PLATFORM, ItemName.TRAFFIC_BLOCKS, ItemName.PINK_CLOUDS, ItemName.RED_BUBBLES, ItemName.NEON_BLUE_KEVIN, ItemName.NEON_PURPLE_KEVIN, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LINKED_TRAFFIC_BLOCK, ItemName.PURPLE_LINKED_TRAFFIC_BLOCK, ItemName.DASH_SPRING, ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.JELLYFISH, ItemName.BREAKER_BOX, ItemName.SINGLE_JUMP_REFILL, ItemName.CRYSTAL_BOMB]]
ihs_access = [[getLocationName(LevelName.SLEEPING_UNDER_STARS, "b_05", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SQUARE_THE_CIRCLE, "outro", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.FROSTED_FRAGMENTS, "end_but_for_real_this_time", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.DEEP_BLUE, "a_09", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.VERTIGO, "Evilleafy-10", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.EAT_GIRL, "A-09", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.HONEYZIP_INC, "endroom", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.TEMPLE_OF_A_THOUSAND_SKIES, "c-02", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.IN_FILTRATION, "gg", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SUPERNAUTICA, "LegS-7", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.FIFTH_DIMENSION, "A12", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.MIDNIGHT_MONSOON, "outro", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.LOW_G_BOTANY, "7", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.THE_TOWER, "lvl07", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.PUFFERFISH_TRANSPORTATION_CO, "RG2-End", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SEA_OF_SOUP, "soup-7", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.CONSTRUCTION_CONUNDRUM, "a-013", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.POINTLESS_MACHINES, "09", LocationType.LEVEL_CLEAR_MINI_HEART)]]

intermediate_levels_sj : dict[LevelName, Level] = {
    LevelName.SLEEPING_UNDER_STARS:
    Level(
        {
            "a_01": Room(0, [Transition("b_01", [[getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1858), getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1860), getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1862), getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1864)]]), Transition("a_02"), Transition("a_03", [[ItemName.DREAM_BLOCK, ItemName.JELLYFISH]]), Transition("a_04"), Transition("a_05")], [Location(LocationType.SILVER_BERRY, 373, [[ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS, getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1858), getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1860), getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1862), getKeyDoorName(LevelName.SLEEPING_UNDER_STARS, "a_01", 1864)]])], start_room=True, key_door_ids=[1858, 1860, 1862, 1864]),
            "a_02": Room(1, [Transition("a_01")], [Location(LocationType.KEY, 287, [[ItemName.DREAM_BLOCK, ItemName.JELLYFISH, ItemName.DASH_CRYSTALS]])]),
            "a_03": Room(2, [Transition("a_01")], [Location(LocationType.KEY, 141, [[ItemName.DREAM_BLOCK, ItemName.JELLYFISH, ItemName.SPRINGS]])]),
            "a_04": Room(3, [Transition("a_01")], [Location(LocationType.KEY, 1823, [[ItemName.TOUCH_SWITCH, ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.SPRINGS]])]),
            "a_05": Room(4, [Transition("a_01")], [Location(LocationType.KEY, 1912, [[ItemName.PUFFER_FISH, ItemName.DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "b_01": Room(5, [Transition("b_02")]),
            "b_02": Room(6, [Transition("b_03", [[ItemName.JELLYFISH, ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS]]), Transition("b_02b", [[ItemName.JELLYFISH, ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS]])]),
            "b_02b": Room(7, [Transition("b_02")], [Location(LocationType.STRAWBERRY, 214)]),
            "b_03": Room(8, [Transition("b_04", [[ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "b_04": Room(9, [Transition("b_05")]),
            "b_05": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])        
        }, LevelCategory.INTERMEDIATE, 49
    ),
    LevelName.SQUARE_THE_CIRCLE:
    Level(
        {
            "a_01": Room(0, [Transition("a-02", [[ItemName.RED_BUBBLES, ItemName.GREEN_BUBBLES, ItemName.NEON_BLUE_KEVIN]])], [Location(LocationType.SILVER_BERRY, 16, [[ItemName.NEON_BLUE_KEVIN, ItemName.NEON_PURPLE_KEVIN, ItemName.TOUCH_SWITCH, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES]])], start_room=True),
            "a-02": Room(1, [Transition("a_02.5", [[ItemName.NEON_PURPLE_KEVIN, ItemName.TOUCH_SWITCH]])], [Location(LocationType.STRAWBERRY, 1386)]),
            "a_02.5": Room(2, [Transition("a_03")]),
            "a_03": Room(3, [Transition("a_04"), Transition("b_01")]),
            "b_01": Room(4, [Transition("a_03")], [Location(LocationType.STRAWBERRY, 447)]),
            "a_04": Room(5, [Transition("a_05"), Transition("b_02")]),
            "b_02": Room(6, [Transition("a_04")], [Location(LocationType.STRAWBERRY, 566)]),
            "a_05": Room(7, [Transition("a_06")]),
            "a_06": Room(8, [Transition("a_07"), Transition("b_03")]),
            "b_03": Room(9, [Transition("a_06")], [Location(LocationType.STRAWBERRY, 1139)]),
            "a_07": Room(10, [Transition("a_08")]),
            "a_08": Room(11, [Transition("a_09"), Transition("b_04")]),
            "b_04": Room(12, [Transition("a_08")], [Location(LocationType.STRAWBERRY, 594)]),
            "a_09": Room(13, [Transition("a_10")]),
            "a_10": Room(14, [Transition("outro")]),
            "outro": Room(15, [Transition("hmmmm")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "hmmmm": Room(16, [Transition("uwu"), Transition("outro")], easter_egg=True),
            "uwu": Room(17, [Transition("hmmmm")], easter_egg=True)
        }, LevelCategory.INTERMEDIATE, 50
    ),
    LevelName.FROSTED_FRAGMENTS:
    Level(
        {
            "a1": Room(0, [Transition("a1.5v2", [[ItemName.PUSH_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 2398, [[ItemName.PUSH_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.SPRINGS, ItemName.MOVING_BLOCK, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "a1.5v2": Room(1, [Transition("a2v2", [[ItemName.SPRINGS]])]),
            "a2v2": Room(2, [Transition("a3v2")]),
            "a3v2": Room(3, [Transition("a4v2", [[ItemName.GREEN_BUBBLES]])]),
            "a4v2": Room(4, [Transition("a5_")]),
            "a5_": Room(5, [Transition("a6v2")]),
            "a6v2": Room(6, [Transition("pushupv2", [[ItemName.MOVING_BLOCK]]), Transition("r_00v2", [[ItemName.MOVING_BLOCK]])]),
            "r_00v2": Room(7, [Transition("a6v2")], [Location(LocationType.STRAWBERRY, 4230, [[ItemName.DASH_CRYSTALS]])]),
            "pushupv2": Room(8, [Transition("reboundv2")]),
            "reboundv2": Room(9, [Transition("a9v2")]),
            "a9v2": Room(10, [Transition("a_10v2", [[ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]])]),
            "a_10v2": Room(11, [Transition("downmoveblockv2"), Transition("r_01v2")]),
            "r_01v2": Room(12, [Transition("a_10v2")], [Location(LocationType.STRAWBERRY, 9666)]),
            "downmoveblockv2": Room(13, [Transition("end_but_for_real_this_time")]),
            "end_but_for_real_this_time": Room(14, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 51
    ),
    LevelName.DEEP_BLUE:
    Level(
        {
            "a_01": Room(0, [Transition("a_02")], [Location(LocationType.SILVER_BERRY, 19, [[ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.DREAM_BLOCK, ItemName.SPRINGS, ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH]])], start_room=True),
            "a_02": Room(1, [Transition("a_03", [[ItemName.DREAM_BLOCK, ItemName.SPRINGS, ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH]])]),
            "a_03": Room(2, [Transition("a_04", [[ItemName.JELLYFISH]])], [Location(LocationType.STRAWBERRY, 582, [[ItemName.JELLYFISH]])]),
            "a_04": Room(3, [Transition("a_05")], [Location(LocationType.STRAWBERRY, 1107, [[ItemName.DASH_CRYSTALS]])]),
            "a_05": Room(4, [Transition("a_06")], [Location(LocationType.STRAWBERRY, 585)]),
            "a_06": Room(5, [Transition("a_07", [[ItemName.DASH_CRYSTALS]])]),
            "a_07": Room(6, [Transition("a_08")]),
            "a_08": Room(7, [Transition("a_09")]),
            "a_09": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 52
    ),
    LevelName.VERTIGO:
    Level(
        {
            "Evilleafy-00": Room(0, [Transition("Evilleafy-01", [[ItemName.VERTIGO_LINKED_TELEPORT]])], [Location(LocationType.SILVER_BERRY, 292, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.VERTIGO_LINKED_TELEPORT]])], start_room=True),
            "Evilleafy-01": Room(1, [Transition("Evilleafy-02", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS]])]),
            "Evilleafy-02": Room(2, [Transition("Evilleafy-03a")]),
            "Evilleafy-03a": Room(3, [Transition("Evilleafy-04a")]),
            "Evilleafy-04a": Room(4, [Transition("Evilleafy-06")]),
            "Evilleafy-06": Room(5, [Transition("Evilleafy-07")]),
            "Evilleafy-07": Room(6, [Transition("Evilleafy-04")]),
            "Evilleafy-04": Room(7, [Transition("Evilleafy-08b")]),
            "Evilleafy-08b": Room(8, [Transition("Evilleafy-09")]),
            "Evilleafy-09": Room(9, [Transition("Evilleafy-10")]),
            "Evilleafy-10": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 53
    ),
    LevelName.EAT_GIRL:
    Level(
        {
            "A-01": Room(0, [Transition("A-02", [[ItemName.TOUCH_SWITCH]])], [Location(LocationType.SILVER_BERRY, 4, [[ItemName.TOUCH_SWITCH, ItemName.YELLOW_PORTAL, ItemName.BLUE_PORTAL, ItemName.TIMED_TOUCH_SWITCH, ItemName.PUSH_STATION_BLOCK, ItemName.TOGGLE_SWAP_BLOCK]])], start_room=True),
            "A-02": Room(1, [Transition("A-03", [[ItemName.YELLOW_PORTAL]])]),
            "A-03": Room(2, [Transition("A-04", [[ItemName.TIMED_TOUCH_SWITCH]])]),
            "A-04": Room(3, [Transition("A-05", [[ItemName.BLUE_PORTAL]])]),
            "A-05": Room(4, [Transition("A-06", [[ItemName.PUSH_STATION_BLOCK]]), Transition("A-05b", [[ItemName.PUSH_STATION_BLOCK]])]),
            "A-05b": Room(5, [Transition("A-05")], [Location(LocationType.STRAWBERRY, 120, [[ItemName.PURPLE_PORTAL]])]),
            "A-06": Room(6, [Transition("A-07", [[ItemName.TOGGLE_SWAP_BLOCK]])]),
            "A-07": Room(7, [Transition("A-08"), Transition("A-07b")]),
            "A-07b": Room(8, [Transition("A-07")], [Location(LocationType.STRAWBERRY, 328)]),
            "A-08": Room(9, [Transition("A-09")]),
            "A-09": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 54
    ),
    LevelName.HONEYZIP_INC:
    Level(
        {
            "startroom": Room(0, [Transition("r1", [[ItemName.ZIPLINE]])], [Location(LocationType.SILVER_BERRY, 408, [[ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.HONEY_BUBBLES, ItemName.SPRINGS, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, getKeyDoorName(LevelName.HONEYZIP_INC, "rhub", 225), getKeyDoorName(LevelName.HONEYZIP_INC, "rhub", 293), getKeyDoorName(LevelName.HONEYZIP_INC, "rhub", 292)]])], start_room=True),
            "r1": Room(1, [Transition("r2", [[ItemName.DASH_CRYSTALS, ItemName.HONEY_BUBBLES, ItemName.SPRINGS]])]),
            "r2": Room(2, [Transition("r3", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK]])]),
            "r3": Room(3, [Transition("rhub")]),
            "rhub": Room(4, [Transition("r9", [[getKeyDoorName(LevelName.HONEYZIP_INC, "rhub", 225), getKeyDoorName(LevelName.HONEYZIP_INC, "rhub", 293), getKeyDoorName(LevelName.HONEYZIP_INC, "rhub", 292)]]), Transition("r4"), Transition("r5"), Transition("r6"), Transition("r7"), Transition("r8")], key_door_ids=[225, 293, 292]),
            "r4": Room(5, [Transition("rhub")], [Location(LocationType.KEY, 522, [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK]])]),
            "r5": Room(6, [Transition("rhub")], [Location(LocationType.KEY, 384, [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.TOUCH_SWITCH, ItemName.SPRINGS]])]),
            "r6": Room(7, [Transition("rhub")], [Location(LocationType.KEY, 770, [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK]])]),
            "r6-right": Room(100, [Transition("r4"), Transition("r6sb")], is_subregion_of="r6"),
            "r7": Room(8, [Transition("rhub")], [Location(LocationType.KEY, 414)]),
            "r8": Room(9, [Transition("rhub"), Transition("r6-right")], [Location(LocationType.KEY, 949)]),
            "r9": Room(10, [Transition("endroom", [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.TOUCH_SWITCH]]), Transition("r9sb", [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.TOUCH_SWITCH]])], [Location(LocationType.STRAWBERRY, 500, [[getKeyDoorName(LevelName.HONEYZIP_INC, "r9", 498)]])], key_door_ids=[498]),
            "r9sb": Room(11, [Transition("endroom")], [Location(LocationType.STRAWBERRY, 1242)]),
            "endroom": Room(12, [Transition("endroomsecret")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "endroomsecret": Room(13, [], easter_egg=True, key_door_ids=[1350]),
            "r6sb": Room(15, [Transition("r6-right")], [Location(LocationType.STRAWBERRY, 141, [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.SPRINGS]])])
        }, LevelCategory.INTERMEDIATE, 55
    ),
    LevelName.TEMPLE_OF_A_THOUSAND_SKIES:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.GREEN_BUBBLES, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "a-02": Room(1, [Transition("a-03", [[ItemName.RED_BUBBLES]])], [Location(LocationType.SILVER_BERRY, 3607, [[ItemName.GREEN_BUBBLES, ItemName.CRUMBLING_PLATFORM, ItemName.RED_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.TRAFFIC_BLOCKS, ItemName.BADELINE_ORB, ItemName.DREAM_BLOCK]])]),
            "a-03": Room(2, [Transition("a-04", [[ItemName.CLOUDS]])]),
            "a-04": Room(3, [Transition("b-01", [[ItemName.DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS]])]),
            "b-01": Room(4, [Transition("c-01", [[ItemName.PINK_CLOUDS, ItemName.DREAM_BLOCK, ItemName.TOUCH_SWITCH]]), Transition("b-02"), Transition("b-05")]),
            "c-01": Room(5, [Transition("c-02", [[ItemName.BADELINE_ORB]])], [Location(LocationType.STRAWBERRY, 3054)]),
            "c-02": Room(6, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "b-05": Room(8, [Transition("b-06", [[ItemName.DREAM_BLOCK]]), Transition("b-07", [[ItemName.DREAM_BLOCK]])]),
            "b-06": Room(9, [Transition("b-05")], [Location(LocationType.STRAWBERRY, 2196, [[ItemName.PINK_CLOUDS]])]),
            "b-07": Room(10, [Transition("b-05")]),
            "b-02": Room(11, [Transition("b-03", [[ItemName.DREAM_BLOCK]]), Transition("b-04", [[ItemName.DREAM_BLOCK]])]),
            "b-03": Room(12, [Transition("b-02")], [Location(LocationType.STRAWBERRY, 3253, [[ItemName.PINK_CLOUDS]])]),
            "b-04": Room(13, [Transition("b-02")], [Location(LocationType.STRAWBERRY, 3261)])
        }, LevelCategory.INTERMEDIATE, 56
    ),
    LevelName.IN_FILTRATION:
    Level(
        {
            "btd-00": Room(0, [Transition("btd-02", [[ItemName.DASH_CRYSTALS, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK]])], [Location(LocationType.SILVER_BERRY, 2172, [[getKeyDoorName(LevelName.IN_FILTRATION, "btd-09", 578), ItemName.DASH_CRYSTALS, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.SPRINGS, ItemName.GREEN_LINKED_TRAFFIC_BLOCK, ItemName.TORQUOISE_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LASER, ItemName.YELLOW_LASER, ItemName.TORQUOISE_LASER, ItemName.TOUCH_SWITCH]])], start_room=True),
            "btd-02": Room(1, [Transition("btd-02a", [[ItemName.SPRINGS]]), Transition("btd-02b", [[ItemName.SPRINGS]]), Transition("btd-02c", [[ItemName.SPRINGS]])]),
            "btd-02b": Room(2, [Transition("btd-02")], [Location(LocationType.STRAWBERRY, 827)]),
            "btd-02c": Room(3, [Transition("btd-02", [[ItemName.GREEN_LINKED_TRAFFIC_BLOCK]])], [Location(LocationType.STRAWBERRY, 839)]),
            "btd-02a": Room(4, [Transition("btd-03")]),
            "btd-03": Room(5, [Transition("btd-04")]),
            "btd-04": Room(6, [Transition("btd-05"), Transition("btd-04a")]),
            "btd-04a": Room(7, [Transition("btd-04")], easter_egg=True),
            "btd-05": Room(8, [Transition("btd-06", [[ItemName.GREEN_LASER]]), Transition("btd-05a", [[ItemName.GREEN_LASER]])]),
            "btd-05a": Room(9, [Transition("btd-05")], [Location(LocationType.STRAWBERRY, 569)]),
            "btd-06": Room(10, [Transition("btd-07", [[ItemName.YELLOW_LASER]])]),
            "btd-07": Room(11, [Transition("btd-09", [[ItemName.TORQUOISE_LINKED_TRAFFIC_BLOCK, ItemName.TORQUOISE_LASER]])]),
            "btd-09": Room(12, [Transition("btd-20", [[getKeyDoorName(LevelName.IN_FILTRATION, "btd-09", 578)]]), Transition("btd-10")], key_door_ids=[578]),
            "btd-20": Room(13, [Transition("btd-21"), Transition("btd-20a")]),
            "btd-20a": Room(14, [Transition("btd-20")], [Location(LocationType.STRAWBERRY, 806)]),
            "btd-21": Room(15, [Transition("btd-30")]),
            "btd-30": Room(16, [Transition("btd-31")]),
            "btd-31": Room(17, [Transition("btd-33")]),
            "btd-33": Room(18, [Transition("btd-35")]),
            "btd-35": Room(19, [Transition("btd-42")], [Location(LocationType.STRAWBERRY, 755, [[ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.MAGENTA_LINKED_TRAFFIC_BLOCK]])]),
            "btd-42": Room(20, [Transition("gg", [[ItemName.TOUCH_SWITCH]])]),
            "gg": Room(21, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "btd-12": Room(23, [Transition("btd-13"), Transition("btd-11")]),
            "btd-13": Room(24, [Transition("btd-12")], [Location(LocationType.KEY, 1556, [[ItemName.TOUCH_SWITCH]])]),
            "btd-11": Room(25, [Transition("btd-12"), Transition("btd-10")]),
            "btd-10": Room(26, [Transition("btd-09"), Transition("btd-11")])
        }, LevelCategory.INTERMEDIATE, 57
    ),
    LevelName.SUPERNAUTICA:
    Level(
        {
            "LegS-0": Room(0, [Transition("LegS-1", [[ItemName.PIPES, ItemName.TOUCH_SWITCH, ItemName.JELLYFISH]])], [Location(LocationType.SILVER_BERRY, 96, [[ItemName.PIPES, ItemName.TOUCH_SWITCH, ItemName.JELLYFISH, ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS]])], start_room=True),
            "LegS-1": Room(1, [Transition("LegS-2", [[ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS]])]),
            "LegS-2": Room(2, [Transition("LegS-B1")]),
            "LegS-B1": Room(3, [Transition("LegS-3")], [Location(LocationType.STRAWBERRY, 1313)]),
            "LegS-3": Room(4, [Transition("LegS-4"), Transition("LegS-Intermediate")]),
            "LegS-Intermediate": Room(5, [Transition("LegS-4"), Transition("LegS-CR", [[ItemName.SWAP_BLOCK]])], easter_egg_difficult=True),
            "LegS-4": Room(6, [Transition("LegS-B2")]),
            "LegS-B2": Room(7, [Transition("LegS-5")], [Location(LocationType.STRAWBERRY, 795)]),
            "LegS-5": Room(8, [Transition("LegS-6")]),
            "LegS-6": Room(9, [Transition("LegS-7")]),
            "LegS-7": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "LegS-CR": Room(12, [], easter_egg_difficult=True)
        }, LevelCategory.INTERMEDIATE, 58
    ),
    LevelName.FIFTH_DIMENSION:
    Level(
        {
            "A00": Room(0, [Transition("A01")], [Location(LocationType.SILVER_BERRY, 1627, [[ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.SOAP_BUBBLE]])], start_room=True),
            "A01": Room(1, [Transition("A02", [[ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "A02": Room(2, [Transition("A03")]),
            "A03": Room(3, [Transition("A04", [[ItemName.SOAP_BUBBLE]])]),
            "A04": Room(4, [Transition("A05")]),
            "A05": Room(5, [Transition("A06")]),
            "A06": Room(6, [Transition("A07")]),
            "A07": Room(7, [Transition("A08")]),
            "A08": Room(8, [Transition("A09")]),
            "A09": Room(9, [Transition("A10")]),
            "A10": Room(10, [Transition("A11")]),
            "A11": Room(11, [Transition("A12")]),
            "A12": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 59
    ),
    LevelName.MIDNIGHT_MONSOON:
    Level(
        {
            "Intro": Room(0, [Transition("1", [[ItemName.SINGLE_JUMP_REFILL, ItemName.DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.TOUCH_SWITCH, ItemName.CRYSTAL_BOMB]])], start_room=True),
            "1": Room(1, [Transition("2", [[ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 2640, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.PUFFER_FISH, ItemName.RED_BUBBLES, ItemName.SPRINGS, ItemName.SINGLE_JUMP_REFILL, ItemName.DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.TOUCH_SWITCH, ItemName.CRYSTAL_BOMB]])]),
            "2": Room(2, [Transition("3", [[ItemName.PUFFER_FISH, ItemName.RED_BUBBLES, ItemName.SPRINGS]]), Transition("2b", [[ItemName.PUFFER_FISH, ItemName.RED_BUBBLES, ItemName.SPRINGS]])]),
            "2b": Room(3, [Transition("2")], [Location(LocationType.STRAWBERRY, 1285)]),
            "3": Room(4, [Transition("4")]),
            "4": Room(5, [Transition("5")]),
            "5": Room(6, [Transition("6"), Transition("5b")]),
            "5b": Room(7, [Transition("5")], [Location(LocationType.STRAWBERRY, 3776)]),
            "6": Room(8, [Transition("outro")]),
            "outro": Room(9, [Transition("outrob")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "outrob": Room(10, [], [Location(LocationType.STRAWBERRY, 29)])
        }, LevelCategory.INTERMEDIATE, 60
    ),
    LevelName.LOW_G_BOTANY:
    Level(
        {
            "1": Room(0, [Transition("2")], [Location(LocationType.SILVER_BERRY, 385, [[ItemName.DASH_SWITCH, ItemName.CLOUDS, ItemName.SPRINGS, ItemName.PINK_CLOUDS, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BREAKER_BOX]])], start_room=True),
            "2": Room(1, [Transition("3", [[ItemName.DASH_SWITCH]])]),
            "3": Room(2, [Transition("4", [[ItemName.CLOUDS, ItemName.SPRINGS, ItemName.PINK_CLOUDS]])]),
            "4": Room(3, [Transition("5", [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 1837, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "5": Room(4, [Transition("5b", [[ItemName.BREAKER_BOX]])]),
            "5b": Room(5, [Transition("6")], [Location(LocationType.STRAWBERRY, 3631)]),
            "6": Room(6, [Transition("7")], [Location(LocationType.STRAWBERRY, 2324)]),
            "7": Room(7, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 61
    ),
    LevelName.THE_TOWER:
    Level(
        {
            "lvl00": Room(0, [Transition("lvl01", [[ItemName.CORE_BLOCK, ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 1175, [[ItemName.DASH_CRYSTALS, ItemName.CORE_BLOCK, ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS]])], start_room=True),
            "lvl01": Room(1, [Transition("lvl02")], [Location(LocationType.STRAWBERRY, 164)]),
            "lvl02": Room(2, [Transition("lvl03", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.STRAWBERRY, 476)]),
            "lvl03": Room(3, [Transition("lvl04")]),
            "lvl04": Room(4, [Transition("lvl05")], [Location(LocationType.STRAWBERRY, 574)]),
            "lvl05": Room(5, [Transition("lvl06")]),
            "lvl06": Room(6, [Transition("lvl07")]),
            "lvl07": Room(7, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]) 
        }, LevelCategory.INTERMEDIATE, 62
    ),
    LevelName.PUFFERFISH_TRANSPORTATION_CO:
    Level(
        {
            "RG2-0": Room(0, [Transition("RG2-1")], [Location(LocationType.SILVER_BERRY, 2535, [[ItemName.BOWL_PUFFER, ItemName.PIPES, ItemName.DASH_CRYSTALS, ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH, ItemName.SPRINGS, ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LINKED_TRAFFIC_BLOCK, ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK]])], start_room=True),
            "RG2-1": Room(1, [Transition("RG2-2", [[ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH, ItemName.SPRINGS]])]),
            "RG2-2": Room(2, [Transition("RG2-3")]),
            "RG2-3": Room(3, [Transition("RG2-4", [[ItemName.DASH_CRYSTALS]])]),
            "RG2-4": Room(4, [Transition("RG2-5", [[ItemName.PIPES]]), Transition("RG2-4-S1", [[ItemName.PIPES]]), Transition("RG2-4-S2", [[ItemName.PIPES]])]),
            "RG2-4-S1": Room(5, [Transition("RG2-4")], [Location(LocationType.STRAWBERRY, 383, [[ItemName.FEATHER]])]),
            "RG2-4-S2": Room(6, [Transition("RG2-4")], [Location(LocationType.STRAWBERRY, 1000)]),
            "RG2-5": Room(7, [Transition("RG2-6", [[ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LINKED_TRAFFIC_BLOCK, ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK]]), Transition("RG2-5-S", [[ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LINKED_TRAFFIC_BLOCK]])]),
            "RG2-5-S": Room(8, [Transition("RG2-5"), Transition("RG2-huh")], [Location(LocationType.STRAWBERRY, 1796)]),
            "RG2-6": Room(9, [Transition("RG2-7")]),
            "RG2-7": Room(10, [Transition("RG2-8")], [Location(LocationType.STRAWBERRY, 722)]),
            "RG2-8": Room(11, [Transition("RG2-9")]),
            "RG2-9": Room(12, [Transition("RG2-End")]),
            "RG2-End": Room(13, [], [Location(LocationType.STRAWBERRY, 2223, [[ItemName.BOWL_PUFFER]]), Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.BOWL_PUFFER]])]),
            "RG2-huh": Room(15, [Transition("RG2-5-S")])
        }, LevelCategory.INTERMEDIATE, 63
    ),
    LevelName.SEA_OF_SOUP:
    Level(
        {
            "soup-1": Room(0, [Transition("soup-2", [[ItemName.PURPLE_DASHLESS_BUBBLE]])], start_room=True),
            "soup-2": Room(1, [Transition("soup-3", [[ItemName.SOAP_BUBBLE, ItemName.BADELINE_ORB]])], [Location(LocationType.SILVER_BERRY, 1912, [[ItemName.SOAP_BUBBLE, ItemName.PURPLE_DASHLESS_BUBBLE, ItemName.BADELINE_ORB]])]),
            "soup-3": Room(2, [Transition("soup-4")], [Location(LocationType.STRAWBERRY, 139)]),
            "soup-4": Room(3, [Transition("soup-5"), Transition("soup-4b")]),
            "soup-4b": Room(4, [Transition("soup-4")], [Location(LocationType.STRAWBERRY, 2022, [[ItemName.TOUCH_SWITCH]])]),
            "soup-5": Room(5, [Transition("soup-6"), Transition("soup-5b")]),
            "soup-5b": Room(6, [Transition("soup-5")], [Location(LocationType.STRAWBERRY, 879, [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS]])]),
            "soup-6": Room(7, [Transition("soup-7"), Transition("soup-6b")]),
            "soup-6b": Room(8, [Transition("soup-6")], [Location(LocationType.STRAWBERRY, 878)]),
            "soup-7": Room(9, [], [Location(LocationType.STRAWBERRY, 2312, [[ItemName.SOAP_BUBBLE, ItemName.PURPLE_DASHLESS_BUBBLE, ItemName.BADELINE_ORB]]), Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.INTERMEDIATE, 64
    ),
    LevelName.CONSTRUCTION_CONUNDRUM:
    Level(
        {
            "a-001": Room(0, [Transition("a-002", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.PULL_STATION_BLOCK, ItemName.PUSH_STATION_BLOCK, ItemName.BREAKER_BOX]]), Transition("a-000")], [Location(LocationType.SILVER_BERRY, 895, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.PULL_STATION_BLOCK, ItemName.PUSH_STATION_BLOCK, ItemName.BREAKER_BOX, ItemName.SINGLE_JUMP_REFILL, ItemName.SPRINGS]])], start_room=True),
            "a-000": Room(1, [Transition("a-001"), Transition("a-000S")], [Location(LocationType.STRAWBERRY, 1410, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.BREAKER_BOX, ItemName.PUSH_STATION_BLOCK]])]),
            "a-002": Room(2, [Transition("a-003", [[ItemName.SINGLE_JUMP_REFILL]])]),
            "a-003": Room(3, [Transition("a-004")]),
            "a-004": Room(4, [Transition("a-005", [[ItemName.SPRINGS]])]),
            "a-005": Room(5, [Transition("a-006")]),
            "a-006": Room(6, [Transition("a-007")]),
            "a-007": Room(7, [Transition("a-008")]),
            "a-008": Room(8, [Transition("a-009")]),
            "a-009": Room(9, [Transition("a-010"), Transition("a-011")]),
            "a-011": Room(10, [Transition("a-009")], [Location(LocationType.STRAWBERRY, 1912)]),
            "a-010": Room(11, [Transition("a-012")]),
            "a-012": Room(12, [Transition("a-013")]),
            "a-013": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a-000S": Room(15, [Transition("a-001")])  
        }, LevelCategory.INTERMEDIATE, 65
    ),
    LevelName.POINTLESS_MACHINES:
    Level(
        {
            "01": Room(0, [Transition("02", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 12, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_SPRING, ItemName.TOUCH_SWITCH, ItemName.BREAKER_BOX]])], start_room=True),
            "02": Room(1, [Transition("03", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "03": Room(2, [Transition("04", [[ItemName.DASH_SPRING]]), Transition("03-berry", [[ItemName.DASH_SPRING]])]),
            "03-berry": Room(3, [Transition("03")], [Location(LocationType.STRAWBERRY, 248, [[ItemName.TOUCH_SWITCH]])]),
            "04": Room(4, [Transition("05")]),
            "05": Room(5, [Transition("06", [[ItemName.BREAKER_BOX]])]),
            "06": Room(6, [Transition("07"), Transition("06-berry")]),
            "06-berry": Room(7, [Transition("06")], [Location(LocationType.STRAWBERRY, 557)]),
            "07": Room(8, [Transition("08")]),
            "08": Room(9, [Transition("09")]),
            "09": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])      
        }, LevelCategory.INTERMEDIATE, 66
    ),
    LevelName.RASPBERRY_ROOTS:
    Level(
        {
            "cp1-0-intro": Room(0, [Transition("cp1-1-liero")], [Location(LocationType.GOLDEN_BERRY, 8554, ihs_golden_list)], start_room=True),
            "cp1-1-liero": Room(1, [Transition("cp1-2-pixelator", [[ItemName.SOAP_BUBBLE, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "cp1-2-pixelator": Room(2, [Transition("cp1-3-Evilleafy", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CORE_BLOCK, ItemName.SPRINGS]])]),
            "cp1-3-Evilleafy": Room(3, [Transition("cp1-4-ezel", [[ItemName.VERTIGO_LINKED_TELEPORT]])]),
            "cp1-4-ezel": Room(4, [Transition("cp2-0-Cp", [[ItemName.PUSH_STATION_BLOCK, ItemName.PULL_STATION_BLOCK, ItemName.TRACK_SWITCH_BOX]])]),
            "cp2-0-Cp": Room(5, [Transition("cp2-1-SpoopySoup")], checkpoint="Phloem"),
            "cp2-1-SpoopySoup": Room(6, [Transition("cp2-2-dooshii", [[ItemName.SOAP_BUBBLE, ItemName.PURPLE_DASHLESS_BUBBLE, ItemName.SPRINGS, ItemName.BADELINE_ORB]])]),
            "cp2-2-dooshii": Room(7, [Transition("cp2-3-glowwoomii", [[ItemName.GREEN_BUBBLES, ItemName.PUSH_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS]])]),
            "cp2-3-glowwoomii": Room(8, [Transition("cp2-4-ice", [[ItemName.HONEY_BUBBLES, getKeyDoorName(LevelName.RASPBERRY_ROOTS, "cp2-3-glowwoomii", 7656)]])], [Location(LocationType.KEY, 1589, [[ItemName.HONEY_BUBBLES, ItemName.ZIPLINE, ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.ORANGE_LINKED_TRAFFIC_BLOCK]])], key_door_ids=[7656]),
            "cp2-4-ice": Room(9, [Transition("cp2-5-bryse0n", [[ItemName.DREAM_BLOCK, ItemName.CRUMBLING_PLATFORM, ItemName.TRAFFIC_BLOCKS, ItemName.PINK_CLOUDS, ItemName.TOUCH_SWITCH, ItemName.RED_BUBBLES]])]),
            "cp2-5-bryse0n": Room(10, [Transition("cp3-0-Cp", [[ItemName.NEON_BLUE_KEVIN, ItemName.NEON_PURPLE_KEVIN]])]),
            "cp3-0-Cp": Room(11, [Transition("cp3-1-Arphimigon")], checkpoint="Mycelium"),
            "cp3-1-Arphimigon": Room(12, [Transition("cp3-2-LegS", [[ItemName.JELLYFISH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK, ItemName.BREAKER_BOX, ItemName.PUFFER_FISH]])]),
            "cp3-2-LegS": Room(13, [Transition("cp3-3-Jems", [[ItemName.CRUMBLING_PLATFORM, ItemName.PIPES, ItemName.SPRINGS]])]),
            "cp3-3-Jems": Room(14, [Transition("cp3-4-vitellary", [[ItemName.YELLOW_LINKED_TRAFFIC_BLOCK, ItemName.GREEN_LINKED_TRAFFIC_BLOCK, ItemName.PURPLE_LINKED_TRAFFIC_BLOCK]])]),
            "cp3-4-vitellary": Room(15, [Transition("cp3-5-RG2", [[ItemName.DASH_CRYSTALS, ItemName.DASH_SPRING]])]),
            "cp3-5-RG2": Room(16, [Transition("cp4-0-Cp", [[ItemName.RED_LINKED_TRAFFIC_BLOCK]])]),
            "cp4-0-Cp": Room(17, [Transition("cp4-1-Emik")], checkpoint="Petrichor"),
            "cp4-1-Emik": Room(18, [Transition("cp4-2-thebreadstick1", [[ItemName.DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.TRAFFIC_BLOCKS, ItemName.SPRINGS, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK]])]),
            "cp4-2-thebreadstick1": Room(19, [Transition("cp4-3-Luma", [[ItemName.PUSH_STATION_BLOCK, ItemName.PULL_STATION_BLOCK, ItemName.BREAKER_BOX, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SINGLE_JUMP_REFILL]])]),
            "cp4-3-Luma": Room(20, [Transition("cp4-4-Marlin", [[ItemName.CRYSTAL_BOMB, ItemName.RED_BUBBLES]])]),
            "cp4-4-Marlin": Room(21, [Transition("cp4-5-Heart", [[ItemName.PINK_CLOUDS]])]),
            "cp4-5-Heart": Room(22, [], [Location(LocationType.CRYSTAL_HEART)])
        }, LevelCategory.INTERMEDIATE_HEARTSIDE, 67, ihs_access
    )
}