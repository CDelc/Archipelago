from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType

heartside_golden = [[ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.HONEY_BUBBLES, ItemName.PURPLE_REBOUND_BUBBLE, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.RED_BUBBLES, ItemName.SOAP_BUBBLE, ItemName.GRAY_BUBBLES, ItemName.SPRINGS, ItemName.GREEN_BUBBLES, ItemName.BOUNCY_SPIKES, ItemName.MOMENTUM_SPRING, ItemName.SPRINGS, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.RED_CASSETTE_SWAP_BLOCK, ItemName.YELLOW_MOVING_CASSETTE_BLOCK, ItemName.GREEN_CASSETTE, ItemName.ORANGE_CASSETTE_BLOCK, ItemName.BLUE_CASSETTE, ItemName.PINK_TRAFFIC_CASSETTE, ItemName.PURPLE_CASSETTE_BLOCK, ItemName.DREAM_TRAFFIC_BLOCK, ItemName.FAKE_CRYSTAL_HEART, ItemName.CRUMBLING_PLATFORM, ItemName.MOVING_BLOCK, ItemName.PUFFER_FISH, ItemName.JELLYFISH, ItemName.CRYSTAL_BOMB, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BLUE_TIME_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.KEVIN, ItemName.GRAY_TIME_CRYSTAL, ItemName.MOVING_PLATFORM, ItemName.GROWTH_POTION, ItemName.DASH_SWITCH, ItemName.PURPLE_JELLYFISH, ItemName.SPRINGS, ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.CRUMBLING_PLATFORM, ItemName.GRAVITY_FIELD, ItemName.JELLYFISH, ItemName.MOVING_TOUCH_SWITCH, ItemName.CORE_BLOCK, ItemName.DREAM_BLOCK, ItemName.PUFFER_FISH, ItemName.DASH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.THROW_BOX, ItemName.RED_PORTAL, ItemName.BLUE_PORTAL, ItemName.PURPLE_PORTAL, ItemName.GREEN_PORTAL, ItemName.YELLOW_PORTAL, ItemName.MOVING_PLATFORM, ItemName.SWAP_BLOCK, ItemName.RED_LINKED_TRAFFIC_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASHLESS_SPRING, ItemName.DREAM_DASH_CRYSTAL, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS, ItemName.TOGGLE_SWAP_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.MOVING_BLOCK, ItemName.WORMHOLE_BUBBLE, ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_SWITCH, ItemName.SPRINGS, ItemName.PULL_STATION_BLOCK, ItemName.SWITCH_CRATE, ItemName.PUSH_STATION_BLOCK, ItemName.RED_BUBBLES, ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL]]
heartside_access = [[
    getLocationName(LevelName.SANDS_OF_TIME, "mini-hearth", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.JELLYFISH_SANCTUM, "outro", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.TOGGLE_THEORY, "heart", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SLIME_TIME, "heart_room", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SUPERSTRUCTURE, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.LETHAL_LASER_LABORATORY, "a_07", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.STARRY_RUINS, "9", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.THE_TOWER_XVI, "7", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.STARLIGHT_STATION, "brys4", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.TECTONIC_TRENCHES, "a-06", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.GOLDEN_DAWN, "A7", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.DUSK_CITY, "a-10", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.FOREST_RUSH, "a10", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.SYNAPSE, "c1", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.UNDERGROWTH, "08-a", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.LOST_WOODS, "oppen_intro", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.ATTACK_OF_THE_CLONE, "BR-Outro", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.THE_LAB, "end_HideInMap", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.BELATED_VALENTINES_DAY, "2-secret :D", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.THINKING_WITH_PORTALS, "a-13", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.BEE_BERSERK, "mini_heart_room", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.JAVAS_CRYPT, "6", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.RIGHTSIDE_DOWN_CAVERN, "Vamp_Final", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.CALL_OF_THE_VOID, "vivEnd", LocationType.LEVEL_CLEAR_MINI_HEART),
    getLocationName(LevelName.RAINDROPS_ON_ROSES, "8", LocationType.LEVEL_CLEAR_MINI_HEART)
]]

advanced_levels_sj : dict[LevelName, Level] = {
    LevelName.SANDS_OF_TIME:
    Level(
        {
            "a-00": Room(0, [Transition("a-01", [[ItemName.KEVIN, ItemName.GRAY_TIME_CRYSTAL, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 1141, [[ItemName.BLUE_TIME_CRYSTAL, ItemName.KEVIN, ItemName.GRAY_TIME_CRYSTAL, ItemName.DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS, ItemName.CRUMBLING_PLATFORM, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS]])], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.TRAFFIC_BLOCKS, ItemName.CRUMBLING_PLATFORM, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-02": Room(2, [Transition("a-03", [[ItemName.BLUE_TIME_CRYSTAL]])]),
            "a-03": Room(3, [Transition("a-04-bis")]),
            "a-04-bis": Room(4, [Transition("a-05")]),
            "a-05": Room(5, [Transition("a-06")]),
            "a-06": Room(6, [Transition("b-01"), Transition("a-strawberry")]),
            "a-strawberry": Room(7, [Transition("a-06")], [Location(LocationType.STRAWBERRY, 510)]),
            "b-01": Room(8, [Transition("b-02"), Transition("b-01-view")], [Location(LocationType.STRAWBERRY, 195)]),
            "b-01-view": Room(9, [Transition("b-01")]),
            "b-02": Room(10, [Transition("b-03")]),
            "b-03": Room(11, [Transition("mini-hearth")]),
            "mini-hearth": Room(12, [Transition("b-strawberry")], [Location(LocationType.STRAWBERRY, 4028), Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "b-strawberry": Room(13, [Transition("mini-hearth")])
        }, LevelCategory.ADVANCED, 68
    ),
    LevelName.JELLYFISH_SANCTUM:
    Level(
        {
            "intro": Room(0, [Transition("1", [[ItemName.PURPLE_JELLYFISH]])], [Location(LocationType.SILVER_BERRY, 199, [[ItemName.PURPLE_JELLYFISH, ItemName.SWAP_BLOCK, ItemName.SPRINGS, ItemName.JELLYFISH, ItemName.DASH_SWITCH, ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "1": Room(1, [Transition("2", [[ItemName.SWAP_BLOCK, ItemName.SPRINGS]])]),
            "2": Room(2, [Transition("3", [[ItemName.JELLYFISH, ItemName.DASH_SWITCH]])]),
            "3": Room(3, [Transition("reverseTutorial"), Transition("berry1")]),
            "berry1": Room(4, [Transition("3")], [Location(LocationType.STRAWBERRY, 92)]),
            "reverseTutorial": Room(5, [Transition("4")]),
            "4": Room(6, [Transition("5", [[ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "5": Room(7, [Transition("outro", [[ItemName.CRUMBLING_PLATFORM]])]),
            "outro": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 69
    ),
    LevelName.TOGGLE_THEORY:
    Level(
        {
            "intro": Room(0, [Transition("a-1", [[ItemName.TOGGLE_SWAP_BLOCK]])], [Location(LocationType.SILVER_BERRY, 1045, [[ItemName.TOGGLE_SWAP_BLOCK, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])], start_room=True),
            "a-1": Room(1, [Transition("a-2", [[ItemName.DASH_CRYSTALS]])]),
            "a-2": Room(2, [Transition("a-3"), Transition("berry0")]),
            "berry0": Room(3, [Transition("a-2")], [Location(LocationType.STRAWBERRY, 3160)]),
            "a-3": Room(4, [Transition("a-4", [[ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("berry1", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "berry1": Room(5, [Transition("a-3")], [Location(LocationType.STRAWBERRY, 623)]),
            "a-4": Room(6, [Transition("bhop")]),
            "bhop": Room(7, [Transition("a-5")]),
            "a-5": Room(8, [Transition("a-6"), Transition("berry2")]),
            "berry2": Room(9, [Transition("a-5")], [Location(LocationType.STRAWBERRY, 1110, [[ItemName.GREEN_BUBBLES]])]),
            "a-6": Room(10, [Transition("epilogue")]),
            "epilogue": Room(11, [Transition("heart")]),
            "heart": Room(12, [Transition("outlook")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "outlook": Room(13, [Transition("heart")], easter_egg=True)
        }, LevelCategory.ADVANCED, 70
    ),
    LevelName.SLIME_TIME:
    Level(
        {
           "a_00-Worldwaker2": Room(0, [Transition("a_01-Gala", [[ItemName.RED_BUBBLES]])], start_room=True),
            "a_01-Gala": Room(1, [Transition("a_02-Gala", [[ItemName.GREEN_BUBBLES, ItemName.DASH_CRYSTALS, ItemName.SOAP_BUBBLE, ItemName.GRAY_BUBBLES, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]])], [Location(LocationType.SILVER_BERRY, 778, [[ItemName.BIRD, ItemName.CLOUDS, ItemName.TOUCH_SWITCH, ItemName.RED_BUBBLES, ItemName.GREEN_BUBBLES, ItemName.DASH_CRYSTALS, ItemName.SOAP_BUBBLE, ItemName.GRAY_BUBBLES, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]])]),
            "a_02-Gala": Room(2, [Transition("a_03-Oppen_heimer", [[ItemName.CLOUDS, ItemName.TOUCH_SWITCH]])]),
            "a_03-Oppen_heimer": Room(3, [Transition("a_04-Gala")], [Location(LocationType.STRAWBERRY, 986)]),
            "a_04-Gala": Room(4, [Transition("a_05-TiltTheStars"), Transition("berry-01-Oppen")]),
            "berry-01-Oppen": Room(5, [Transition("a_04-Gala")], [Location(LocationType.STRAWBERRY, 2567)]),
            "a_05-TiltTheStars": Room(6, [Transition("a_06-TiltTheStars")]),
            "a_06-TiltTheStars": Room(7, [Transition("a_07-TiltTheStars")]),
            "a_07-TiltTheStars": Room(8, [Transition("a_08-TiltTheStars")], [Location(LocationType.STRAWBERRY, 2684)]),
            "a_08-TiltTheStars": Room(9, [Transition("heart_room", [[ItemName.BIRD]])]),
            "heart_room": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 71
    ),
    LevelName.SUPERSTRUCTURE:
    Level(
        {
            "start": Room(0, [Transition("tutorial-1")], start_room=True),
            "tutorial-1": Room(1, [Transition("goldian-1", [[ItemName.SWITCH_CRATE]])], [Location(LocationType.SILVER_BERRY, 1896, [[ItemName.SWITCH_CRATE, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.PUSH_STATION_BLOCK, ItemName.PULL_STATION_BLOCK, ItemName.SPRINGS]])]),
            "goldian-1": Room(2, [Transition("aiden-2", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS]])]),
            "aiden-2": Room(3, [Transition("goldian-3")]),
            "goldian-3": Room(4, [Transition("goldian-4", [[ItemName.TOUCH_SWITCH]])]),
            "goldian-4": Room(5, [Transition("tutorial-2")]),
            "tutorial-2": Room(6, [Transition("goldian-5", [[ItemName.PUSH_STATION_BLOCK, ItemName.PULL_STATION_BLOCK]])]),
            "goldian-5": Room(7, [Transition("goldian-6", [[ItemName.SPRINGS]]), Transition("goldian-berry", [[ItemName.SPRINGS]])]),
            "goldian-berry": Room(8, [Transition("goldian-5")], [Location(LocationType.STRAWBERRY, 2200)]),
            "goldian-6": Room(9, [Transition("goldian-7")]),
            "goldian-7": Room(10, [Transition("end")]),
            "end": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 72
    ),
    LevelName.LETHAL_LASER_LABORATORY:
    Level(
        {
            "a_01": Room(0, [Transition("a_02", [[ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 454, [[ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS, ItemName.MOVING_BLOCK, ItemName.MOVING_PLATFORM, ItemName.SWAP_BLOCK, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "a_02": Room(1, [Transition("a_03", [[ItemName.MOVING_BLOCK]])]),
            "a_03": Room(2, [Transition("a_04", [[ItemName.MOVING_PLATFORM]])]),
            "a_04": Room(3, [Transition("a_05", [[ItemName.SWAP_BLOCK, ItemName.CRUMBLING_PLATFORM]])]),
            "a_05": Room(4, [Transition("a_06", [[ItemName.TOUCH_SWITCH]])]),
            "a_06": Room(5, [Transition("a_07", [[ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("a_06b")]),
            "a_06b": Room(6, [Transition("a_06")], [Location(LocationType.STRAWBERRY, 991)]),
            "a_07": Room(7, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 73
    ),
    LevelName.STARRY_RUINS:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.BLUE_PORTAL]])], [Location(LocationType.SILVER_BERRY, 1643)], start_room=True),
            "2": Room(1, [Transition("3")]),
            "3": Room(2, [Transition("4", [[ItemName.GREEN_PORTAL, ItemName.RED_PORTAL]])]),
            "4": Room(3, [Transition("5", [[ItemName.DASH_CRYSTALS]])]),
            "5": Room(4, [Transition("6")]),
            "6": Room(5, [Transition("7", [[ItemName.RED_LINKED_TRAFFIC_BLOCK]])]),
            "7": Room(6, [Transition("8")]),
            "8": Room(7, [Transition("9")]),
            "9": Room(8, [Transition("10", [[ItemName.YELLOW_PORTAL]])]),
            "10": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.PURPLE_PORTAL]])])
        }, LevelCategory.ADVANCED, 74
    ),
    LevelName.THE_TOWER_XVI:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.DREAM_BLOCK]])], [Location(LocationType.SILVER_BERRY, 234, [[ItemName.DREAM_DASH_CRYSTAL, ItemName.DREAM_BLOCK]])], start_room=True),
            "2": Room(1, [Transition("3")]),
            "3": Room(2, [Transition("4")]),
            "4": Room(3, [Transition("5", [[ItemName.DREAM_DASH_CRYSTAL]])]),
            "5": Room(4, [Transition("6")]),
            "6": Room(5, [Transition("7")]),
            "7": Room(6, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 75
    ),
    LevelName.STARLIGHT_STATION:
    Level(
        {
            "a0": Room(0, [Transition("a1", [[ItemName.TRAFFIC_BLOCKS]]), Transition("a-secret", [[ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.SILVER_BERRY, 4872, [[ItemName.SPRINGS, ItemName.TRAFFIC_BLOCKS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.RED_BUBBLES]])], start_room=True),
            "a-secret": Room(1, [Transition("a0")], easter_egg=True),
            "a1": Room(2, [Transition("a2", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a2": Room(3, [Transition("a3", [[ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.RED_BUBBLES]]), Transition("a-berry")]),
            "a-berry": Room(4, [Transition("a2")], [Location(LocationType.STRAWBERRY, 4332)]),
            "a3": Room(5, [Transition("b1", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS]])]),
            "b1": Room(6, [Transition("b2")]),
            "b2": Room(7, [Transition("b3")]),
            "b3": Room(8, [Transition("b4")]),
            "b4": Room(9, [Transition("b5"), Transition("b-berry")]),
            "b-berry": Room(10, [Transition("b4")], [Location(LocationType.STRAWBERRY, 7539, [[ItemName.DASH_SWITCH]])]),
            "b5": Room(11, [Transition("65")]),
            "65": Room(12, [Transition("b7")]),
            "b7": Room(13, [Transition("brys1")]),
            "brys1": Room(14, [Transition("brys2")]),
            "brys2": Room(15, [Transition("brys3")]),
            "brys3": Room(16, [Transition("brys4")]),
            "brys4": Room(17, [Transition("brys-berry")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "brys-berry": Room(18, [Transition("brys4")], [Location(LocationType.STRAWBERRY, 7540)])
        }, LevelCategory.ADVANCED, 76
    ),
    LevelName.TECTONIC_TRENCHES:
    Level(
        {
            "a-01": Room(0, [Transition("a-02")], start_room=True),
            "a-02": Room(1, [Transition("a-03", [[ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.MOVING_TOUCH_SWITCH, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM]])], [Location(LocationType.SILVER_BERRY, 399, [[ItemName.DREAM_BLOCK, ItemName.CORE_BLOCK, ItemName.PUFFER_FISH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.MOVING_TOUCH_SWITCH, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM]])]),
            "a-03": Room(2, [Transition("a-04", [[ItemName.PUFFER_FISH, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-04": Room(3, [Transition("a-05intro", [[ItemName.CORE_BLOCK]])], [Location(LocationType.STRAWBERRY, 1114)]),
            "a-05intro": Room(4, [Transition("a-05"), Transition("transition")]),
            "transition": Room(5, [Transition("a-05intro"), Transition("Berry 1")]),
            "a-05": Room(6, [Transition("a-07", [[ItemName.DREAM_BLOCK]])]),
            "a-07": Room(7, [Transition("a-06")]),
            "a-06": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "Berry 1": Room(10, [Transition("transition")], [Location(LocationType.STRAWBERRY, 895)])
        }, LevelCategory.ADVANCED, 77
    ),
    LevelName.GOLDEN_DAWN:
    Level(
        {
            "A0": Room(0, [Transition("A2", [[ItemName.MOVING_BLOCK, ItemName.JELLYFISH, ItemName.TOUCH_SWITCH, ItemName.PUFFER_FISH]])], start_room=True),
            "A2": Room(1, [Transition("A4", [[ItemName.DASH_CRYSTALS]]), Transition("A2_v2")]),
            "A2_v2": Room(2, [Transition("A2")], [Location(LocationType.STRAWBERRY, 3574, [[ItemName.SPRINGS]])]),
            "A4": Room(3, [Transition("A5")]),
            "A5": Room(4, [Transition("Brys2-2-2"), Transition("A5_v2")]),
            "A5_v2": Room(5, [Transition("A5")], [Location(LocationType.STRAWBERRY, 239, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Brys2-2-2": Room(6, [Transition("A6", [[ItemName.SPRINGS]]), Transition("A6_v2-flip-2", [[ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "A6_v2-flip-2": Room(7, [Transition("Brys2-2-2"), Transition("A6")], [Location(LocationType.STRAWBERRY, 4103)]),
            "A6": Room(8, [Transition("A7")]),
            "A7": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 78
    ),
    LevelName.DUSK_CITY:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.TRAFFIC_BLOCKS, ItemName.DREAM_TRAFFIC_BLOCK]]), Transition("b-01", [[ItemName.TRAFFIC_BLOCKS, ItemName.DREAM_TRAFFIC_BLOCK]])], [Location(LocationType.SILVER_BERRY, 1676, [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.TRAFFIC_BLOCKS, ItemName.DREAM_TRAFFIC_BLOCK]])], start_room=True),
            "b-01": Room(1, [Transition("a-01")], easter_egg_difficult=True),
            "a-02": Room(2, [Transition("a-03", [[ItemName.DASH_CRYSTALS]])]),
            "a-03": Room(3, [Transition("a-04")]),
            "a-04": Room(4, [Transition("a-05")]),
            "a-05": Room(5, [Transition("a-06", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]])]),
            "a-06": Room(6, [Transition("a-07", [[ItemName.TOUCH_SWITCH]])]),
            "a-07": Room(7, [Transition("a-08")]),
            "a-08": Room(8, [Transition("a-09")]),
            "a-09": Room(9, [Transition("a-10")]),
            "a-10": Room(10, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 79
    ),
    LevelName.FOREST_RUSH:
    Level(
        {
            "a00": Room(0, [Transition("a01")], start_room=True),
            "a01": Room(1, [Transition("a02", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 11, [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.BOUNCY_SPIKES, ItemName.MOMENTUM_SPRING]])]),
            "a02": Room(2, [Transition("a03", [[ItemName.BOUNCY_SPIKES, ItemName.MOMENTUM_SPRING]])]),
            "a03": Room(3, [Transition("a04", [[ItemName.TOUCH_SWITCH]])]),
            "a04": Room(4, [Transition("a05")]),
            "a05": Room(5, [Transition("a06")], [Location(LocationType.STRAWBERRY, 740)]),
            "a06": Room(6, [Transition("a07")]),
            "a07": Room(7, [Transition("a08"), Transition("a07b")]),
            "a07b": Room(8, [Transition("a07")], [Location(LocationType.STRAWBERRY, 908)]),
            "a08": Room(9, [Transition("a09")]),
            "a09": Room(10, [Transition("a10")]),
            "a10": Room(11, [Transition("a10b")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "a10b": Room(12, [Transition("a10")], [Location(LocationType.STRAWBERRY, 555)])
        }, LevelCategory.ADVANCED, 80
    ),
    LevelName.SYNAPSE:
    Level(
        {
            "intro_fall": Room(0, [Transition("intro_a1")], start_room=True),
            "intro_a1": Room(1, [Transition("a1")]),
            "a1": Room(2, [Transition("a2", [[ItemName.RED_CASSETTE_BLOCK, ItemName.ORANGE_CASSETTE_BLOCK]])], [Location(LocationType.SILVER_BERRY, 6159, [[ItemName.GREEN_CASSETTE_SWAP_BLOCK, ItemName.YELLOW_CASSETTE_SWAP_BLOCK, ItemName.PINK_MOVING_CASSETTE_BLOCK, ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.RED_CASSETTE_TRAFFIC_BLOCK, ItemName.GREEN_MOVING_CASSETTE_BLOCK, ItemName.RED_CASSETTE_SWAP_BLOCK, ItemName.ORANGE_MOVING_CASSETTE_BLOCK, ItemName.YELLOW_TRAFFIC_CASSETTE, ItemName.PURPLE_CASSETTE_SWAP_BLOCK, ItemName.PINK_CASSETTE_SWAP_BLOCK, ItemName.PINK_CASSETTE, ItemName.BLUE_MOVING_CASSETTE_BLOCK, ItemName.PURPLE_MOVING_CASSETTE_BLOCK, ItemName.GREEN_CASSETTE_TRAFFIC_BLOCK, ItemName.BLUE_TRAFFIC_CASSETTE, ItemName.DASH_CRYSTALS, ItemName.YELLOW_CASSETTE, ItemName.GREEN_CASSETTE, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.SPRINGS, ItemName.RED_CASSETTE_BLOCK, ItemName.ORANGE_CASSETTE_BLOCK]])]),
            "a2": Room(3, [Transition("a3", [[ItemName.YELLOW_CASSETTE, ItemName.GREEN_CASSETTE, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.SPRINGS]])]),
            "a3": Room(4, [Transition("a4", [[ItemName.GREEN_CASSETTE_TRAFFIC_BLOCK, ItemName.BLUE_TRAFFIC_CASSETTE, ItemName.DASH_CRYSTALS]])]),
            "a4": Room(5, [Transition("a5", [[ItemName.BLUE_MOVING_CASSETTE_BLOCK, ItemName.PURPLE_MOVING_CASSETTE_BLOCK]])]),
            "a5": Room(6, [Transition("b1", [[ItemName.PURPLE_CASSETTE_SWAP_BLOCK, ItemName.PINK_CASSETTE_SWAP_BLOCK, ItemName.PINK_CASSETTE]])]),
            "b1": Room(7, [Transition("b2", [[ItemName.RED_CASSETTE_SWAP_BLOCK, ItemName.ORANGE_MOVING_CASSETTE_BLOCK, ItemName.YELLOW_TRAFFIC_CASSETTE]]), Transition("b1_b", [[ItemName.RED_CASSETTE_SWAP_BLOCK]])]),
            "b1_b": Room(8, [Transition("b1")], [Location(LocationType.STRAWBERRY, 3951, [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.RED_CASSETTE_BLOCK, ItemName.GREEN_CASSETTE, ItemName.FEATHER]])]),
            "b2": Room(9, [Transition("b3", [[ItemName.GREEN_MOVING_CASSETTE_BLOCK]])]),
            "b3": Room(10, [Transition("c1", [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.RED_CASSETTE_TRAFFIC_BLOCK]])]),
            "c1": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.GREEN_CASSETTE_SWAP_BLOCK, ItemName.YELLOW_CASSETTE_SWAP_BLOCK, ItemName.PINK_MOVING_CASSETTE_BLOCK]])])
        }, LevelCategory.ADVANCED, 81
    ),
    LevelName.UNDERGROWTH:
    Level(
        {
            "01-a": Room(0, [Transition("02-a", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 4190, [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASHLESS_SPRING, ItemName.CRUMBLING_PLATFORM]])], start_room=True),
            "02-a": Room(1, [Transition("03-a", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "03-a": Room(2, [Transition("05-a", [[getKeyDoorName(LevelName.UNDERGROWTH, "03-a", 776)]]), Transition("04-a")], [Location(LocationType.STRAWBERRY, 879, [[ItemName.CRUMBLING_PLATFORM]])], key_door_ids=[776]),
            "05-a": Room(3, [Transition("06-a")], [Location(LocationType.STRAWBERRY, 2573)]),
            "06-a": Room(4, [Transition("07-a", [[ItemName.DASHLESS_SPRING, ItemName.CRUMBLING_PLATFORM]]), Transition("06-s1", [[ItemName.DASHLESS_SPRING, ItemName.CRUMBLING_PLATFORM]]), Transition("06-b", [[ItemName.DASHLESS_SPRING, ItemName.CRUMBLING_PLATFORM]])], [Location(LocationType.STRAWBERRY, 2886, [[ItemName.DASHLESS_SPRING, ItemName.CRUMBLING_PLATFORM]])], key_door_ids=[2912]),
            "06-s1": Room(5, [Transition("06-a")], easter_egg=True),
            "06-b": Room(6, [Transition("06-a")], [Location(LocationType.STRAWBERRY, 3377), Location(LocationType.KEY, 134)]),
            "07-a": Room(7, [Transition("08-a")]),
            "08-a": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "04-a": Room(10, [Transition("04-s1", [[ItemName.CRUMBLING_PLATFORM, ItemName.DASHLESS_SPRING, ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.UNDERGROWTH, "03-a", 776)]]), Transition("03-a")], [Location(LocationType.KEY, 843)]),
            "04-s1": Room(11, [Transition("04-a")], [Location(LocationType.STRAWBERRY, 1659, [[ItemName.DASHLESS_SPRING]])])
        }, LevelCategory.ADVANCED, 82
    ),
    LevelName.LOST_WOODS:
    Level(
        {
            "oppen_intro": Room(0, [Transition("oppen_1a")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[getKeyDoorName(LevelName.LOST_WOODS, "oppen_intro", 0), getKeyDoorName(LevelName.LOST_WOODS, "oppen_intro", 1), getKeyDoorName(LevelName.LOST_WOODS, "oppen_intro", 2)]]), Location(LocationType.SILVER_BERRY, 90, [[getKeyDoorName(LevelName.LOST_WOODS, "oppen_intro", 0), getKeyDoorName(LevelName.LOST_WOODS, "oppen_intro", 1), getKeyDoorName(LevelName.LOST_WOODS, "oppen_intro", 2)]])], start_room=True, key_door_ids=[0, 1, 2]),
            "oppen_1a": Room(1, [Transition("oppen_1b"), Transition("oppen_1c"), Transition("oppen_berry", [[ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM]]), Transition("oppen_intro")], [Location(LocationType.KEY, 3183)]),
            "oppen_berry": Room(2, [Transition("oppen_1a")], [Location(LocationType.STRAWBERRY, 647)]),
            "oppen_1b": Room(3, [Transition("oppen_1a"), Transition("oppen_1c")], [Location(LocationType.KEY, 1765)]),
            "oppen_1c": Room(4, [Transition("oppen_1a"), Transition("oppen_1b")], [Location(LocationType.KEY, 3647)])
        }, LevelCategory.ADVANCED, 83
    ),
    LevelName.ATTACK_OF_THE_CLONE:
    Level(
        {
            "BR-00": Room(0, [Transition("BR-02", [[ItemName.SEEKERS, ItemName.PUFFER_FISH, ItemName.CRYSTAL_BOMB]])], [Location(LocationType.SILVER_BERRY, 929, [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.KEVIN, ItemName.SWAP_BLOCK, ItemName.SEEKERS, ItemName.PUFFER_FISH, ItemName.CRYSTAL_BOMB]])], start_room=True),
            "BR-02": Room(1, [Transition("BR-01", [[ItemName.DASH_CRYSTALS]])]),
            "BR-01": Room(2, [Transition("BR-08")]),
            "BR-08": Room(3, [Transition("BR-03", [[ItemName.BLUE_LINKED_TRAFFIC_BLOCK, ItemName.KEVIN, ItemName.SWAP_BLOCK]])]),
            "BR-03": Room(4, [Transition("BR-04")]),
            "BR-04": Room(5, [Transition("BR-07", [[ItemName.SPRINGS]])]),
            "BR-07": Room(6, [Transition("BR-05")]),
            "BR-05": Room(7, [Transition("BR-Outro")]),
            "BR-Outro": Room(8, [Transition("BR-Extra")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "BR-Extra": Room(9, [Transition("BR-Outro")], [Location(LocationType.STRAWBERRY, 866)])
        }, LevelCategory.ADVANCED, 84
    ),
    LevelName.THE_LAB:
    Level(
        {
            "start-01-Radley": Room(0, [Transition("start-02-Radley", [[ItemName.WORMHOLE_BUBBLE]])], start_room=True),
            "start-02-Radley": Room(1, [Transition("start-03-Radley/Worldwaker2")]),
            "start-03-Radley/Worldwaker2": Room(2, [Transition("start-04-Radley")], [Location(LocationType.SILVER_BERRY, 986, [[ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_SWITCH, ItemName.MOVING_BLOCK, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.TRAFFIC_BLOCKS, ItemName.WORMHOLE_BUBBLE, getKeyDoorName(LevelName.THE_LAB, "hub", 487), getKeyDoorName(LevelName.THE_LAB, "hub", 488), getKeyDoorName(LevelName.THE_LAB, "hub", 489)]])]),
            "start-04-Radley": Room(3, [Transition("start-05-TiltTheStars", [[ItemName.TRAFFIC_BLOCKS]])]),
            "start-05-TiltTheStars": Room(4, [Transition("hub", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "hub": Room(5, [Transition("cross-01-Worldwaker2"), Transition("evade-01-Quantum"), Transition("move-01-TiltTheStars"), Transition("escape-01-Worldwaker2", [[getKeyDoorName(LevelName.THE_LAB, "hub", 487), getKeyDoorName(LevelName.THE_LAB, "hub", 488), getKeyDoorName(LevelName.THE_LAB, "hub", 489)]])], key_door_ids=[487, 488, 489]),
            "cross-01-Worldwaker2": Room(6, [Transition("cross-02-TiltTheStars", [[ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS, ItemName.DASH_CRYSTALS]])]),
            "cross-02-TiltTheStars": Room(7, [Transition("cross-03-TiltTheStars")], [Location(LocationType.KEY, 962)]),
            "cross-03-TiltTheStars": Room(8, [Transition("hub")], [Location(LocationType.STRAWBERRY, 86, [[ItemName.DASH_SWITCH]])]),
            "evade-01-Quantum": Room(9, [Transition("evade-02b-Quantum")]),
            "evade-02b-Quantum": Room(10, [Transition("evade-02-TiltTheStars")], [Location(LocationType.STRAWBERRY, 87)]),
            "evade-02-TiltTheStars": Room(11, [Transition("evade-03-Worldwaker2", [[ItemName.SPRINGS]])], [Location(LocationType.KEY, 1326, [[ItemName.SPRINGS]])]),
            "evade-03-Worldwaker2": Room(12, [Transition("hub")]),
            "move-01-TiltTheStars": Room(13, [Transition("move-02-Worldwaker2", [[ItemName.SPRINGS, ItemName.MOVING_BLOCK, ItemName.DASH_SWITCH, ItemName.CRUMBLING_PLATFORM]])]),
            "move-02-Worldwaker2": Room(14, [Transition("move-02b-Quantum"), Transition("hub", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.KEY, 629)]),
            "move-02b-Quantum": Room(15, [Transition("move-02-Worldwaker2")], [Location(LocationType.STRAWBERRY, 90, [[ItemName.DASH_CRYSTALS]])]),
            "escape-01-Worldwaker2": Room(16, [Transition("escape-02-Worldwaker2", [[ItemName.SPRINGS, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_SWITCH, ItemName.MOVING_BLOCK, ItemName.DASH_CRYSTALS]])]),
            "escape-02-Worldwaker2": Room(17, [Transition("escape-03-Worldwaker2")]),
            "escape-03-Worldwaker2": Room(18, [Transition("start-00-Radley")]),
            "start-00-Radley": Room(19, [Transition("end_HideInMap")]),
            "end_HideInMap": Room(20, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 85
    ),
    LevelName.BELATED_VALENTINES_DAY:
    Level(
        {
            "1-intro": Room(0, [Transition("1-a", [[ItemName.FAKE_CRYSTAL_HEART]])], [Location(LocationType.SILVER_BERRY, 2312, [[ItemName.CRUMBLING_PLATFORM, ItemName.FAKE_CRYSTAL_HEART, ItemName.MINI_FAKE_CRYSTAL_HEART]])], start_room=True),
            "1-a": Room(1, [Transition("1-b", [[ItemName.CRUMBLING_PLATFORM]])]),
            "1-b": Room(2, [Transition("1-c")]),
            "1-c": Room(3, [Transition("1-e")]),
            "1-e": Room(4, [Transition("1-f")]),
            "1-f": Room(5, [Transition("1-g"), Transition("1-d")]),
            "1-d": Room(6, [Transition("1-f")], [Location(LocationType.STRAWBERRY, 249)]),
            "1-g": Room(7, [Transition("1-h")]),
            "1-h": Room(8, [Transition("2-a", [[ItemName.MINI_FAKE_CRYSTAL_HEART]])]),
            "2-a": Room(9, [Transition("2-b")]),
            "2-b": Room(10, [Transition("2-c")], [Location(LocationType.STRAWBERRY, 1086)]),
            "2-c": Room(11, [Transition("2-d")]),
            "2-d": Room(12, [Transition("2-secret :D")]),
            "2-secret :D": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 86
    ),
    LevelName.THINKING_WITH_PORTALS:
    Level(
        {
            "a-01": Room(0, [Transition("a-02", [[ItemName.DASH_SWITCH, ItemName.THROW_BOX, ItemName.PURPLE_PORTAL, ItemName.BLUE_PORTAL]])], [Location(LocationType.SILVER_BERRY, 41, [[ItemName.BREAKER_BOX, ItemName.RED_PORTAL, ItemName.CRUMBLING_PLATFORM, ItemName.YELLOW_PORTAL, ItemName.GREEN_PORTAL, ItemName.DASH_CRYSTALS, ItemName.DASH_SWITCH, ItemName.THROW_BOX, ItemName.PURPLE_PORTAL, ItemName.BLUE_PORTAL]])], start_room=True),
            "a-02": Room(1, [Transition("a-04", [[ItemName.YELLOW_PORTAL, ItemName.GREEN_PORTAL, ItemName.DASH_CRYSTALS]])]),
            "a-04": Room(2, [Transition("a-05", [[ItemName.CRUMBLING_PLATFORM]])]),
            "a-05": Room(3, [Transition("a-06", [[ItemName.RED_PORTAL]])]),
            "a-06": Room(4, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 1384)]),
            "a-07": Room(5, [Transition("a-08")]),
            "a-08": Room(6, [Transition("a-09"), Transition("a-10")]),
            "a-10": Room(7, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 401)]),
            "a-09": Room(8, [Transition("a-11")]),
            "a-11": Room(9, [Transition("a-13"), Transition("a-12")]),
            "a-12": Room(10, [Transition("a-11")], [Location(LocationType.STRAWBERRY, 723, [[ItemName.TOUCH_SWITCH]])]),
            "a-13": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.BREAKER_BOX]])])
        }, LevelCategory.ADVANCED, 87
    ),
    LevelName.BEE_BERSERK:
    Level(
        {
            "intro_v1": Room(0, [Transition("intro_v2")], start_room=True),
            "intro_v2": Room(1, [Transition("a-01", [[ItemName.PURPLE_REBOUND_BUBBLE, ItemName.CRUMBLING_PLATFORM]])]),
            "a-01": Room(2, [Transition("a-02", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 1035, [[ItemName.MOVING_BLOCK, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.PURPLE_REBOUND_BUBBLE, ItemName.CRUMBLING_PLATFORM]])]),
            "a-02": Room(3, [Transition("a-03", [[ItemName.TOUCH_SWITCH]])]),
            "a-03": Room(4, [Transition("a-04", [[ItemName.MOVING_BLOCK]])]),
            "a-04": Room(5, [Transition("a-05")]),
            "a-05": Room(6, [Transition("a-06")]),
            "a-06": Room(7, [Transition("a-07"), Transition("secret-02")]),
            "secret-01": Room(8, [Transition("a-06"), Transition("secret-02")]),
            "a-07": Room(9, [Transition("a-08")]),
            "a-08": Room(10, [Transition("badeline_v2")]),
            "badeline_v2": Room(11, [Transition("mini_heart_room")]),
            "mini_heart_room": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "secret-02": Room(14, [Transition("secret-01")], [Location(LocationType.STRAWBERRY, 1027)])
        }, LevelCategory.ADVANCED, 88
    ),
    LevelName.JAVAS_CRYPT:
    Level(
        {
            "0b": Room(0, [Transition("0")], start_room=True),
            "0": Room(1, [Transition("1", [[ItemName.GROWTH_POTION]])], [Location(LocationType.SILVER_BERRY, 275, [[ItemName.DASH_CRYSTALS, ItemName.GROWTH_POTION, ItemName.DASH_SWITCH, ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.JAVAS_CRYPT, "3", 35), getKeyDoorName(LevelName.JAVAS_CRYPT, "4", 297), getKeyDoorName(LevelName.JAVAS_CRYPT, "5", 759)]]), Location(LocationType.STRAWBERRY, 674)]),
            "1": Room(2, [Transition("2"), Transition("1b")]),
            "1b": Room(3, [Transition("1")]),
            "2": Room(4, [Transition("3", [[ItemName.DASH_CRYSTALS, ItemName.DASH_SWITCH]]), Transition("2b")], [Location(LocationType.STRAWBERRY, 100)]),
            "2b": Room(5, [Transition("2")]),
            "3": Room(6, [Transition("3b", [[ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.JAVAS_CRYPT, "3", 35)]]), Transition("4", [[ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.JAVAS_CRYPT, "3", 35)]])], [Location(LocationType.KEY, 132), Location(LocationType.STRAWBERRY, 276, [[ItemName.TOUCH_SWITCH, getKeyDoorName(LevelName.JAVAS_CRYPT, "3", 35)]])], key_door_ids=[35]),
            "3b": Room(7, [Transition("3")], [Location(LocationType.STRAWBERRY, 629)]),
            "4": Room(8, [Transition("4b"), Transition("5", [[getKeyDoorName(LevelName.JAVAS_CRYPT, "4", 297)]])], [Location(LocationType.KEY, 226)], key_door_ids=[297]),
            "4b": Room(9, [Transition("4")]),
            "5": Room(10, [Transition("6", [[getKeyDoorName(LevelName.JAVAS_CRYPT, "5", 759)]])], [Location(LocationType.STRAWBERRY, 670), Location(LocationType.KEY, 838)], key_door_ids=[759]),
            "6": Room(11, [Transition("6e")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "6e": Room(12, [Transition("6")], easter_egg=True)
        }, LevelCategory.ADVANCED, 89
    ),
    LevelName.RIGHTSIDE_DOWN_CAVERN:
    Level(
        {
            "intro_SJ": Room(0, [Transition("Vamp_2", [[ItemName.GRAVITY_FIELD, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BLUE_GRAVITY_SPRING]])], [Location(LocationType.STRAWBERRY, 374, [[ItemName.GRAVITY_FIELD]]), Location(LocationType.SILVER_BERRY, 2482, [[ItemName.SPRINGS, ItemName.GRAVITY_FIELD, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.RED_GRAVITY_SPRING, ItemName.BLUE_GRAVITY_SPRING, ItemName.PURPLE_GRAVITY_SPRING]])], start_room=True),
            "Vamp_2": Room(1, [Transition("Vamp_3", [[ItemName.DASH_CRYSTALS]])]),
            "Vamp_3": Room(2, [Transition("Vamp_4")]),
            "Vamp_4": Room(3, [Transition("Vamp_5", [[ItemName.SPRINGS, ItemName.RED_GRAVITY_SPRING]])]),
            "Vamp_5": Room(4, [Transition("Vamp_6")]),
            "Vamp_6": Room(5, [Transition("Vamp_7", [[ItemName.PURPLE_GRAVITY_SPRING]])], [Location(LocationType.STRAWBERRY, 2459, [[ItemName.PURPLE_GRAVITY_SPRING]]), Location(LocationType.STRAWBERRY, 2136, [[ItemName.PURPLE_GRAVITY_SPRING]])]),
            "Vamp_7": Room(6, [Transition("Vamp_8")]),
            "Vamp_8": Room(7, [Transition("Vamp_9")]),
            "Vamp_9": Room(8, [Transition("Vamp_Final")]),
            "Vamp_Final": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.ADVANCED, 90
    ),
    LevelName.CALL_OF_THE_VOID:
    Level(
        {
            "viv0": Room(0, [Transition("viv1", [[ItemName.SPRINGS, ItemName.TOUCH_SWITCH]])], [Location(LocationType.SILVER_BERRY, 1147, [[ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.SPRINGS, ItemName.TOUCH_SWITCH, ItemName.MOVING_TOUCH_SWITCH]])], start_room=True),
            "viv1": Room(1, [Transition("viv2", [[ItemName.DASH_REFILL_WALL]])]),
            "viv2": Room(2, [Transition("viv3", [[ItemName.DOUBLE_DASH_REFILL_WALL]]), Transition("viv2b")]),
            "viv2b": Room(3, [Transition("viv2")], [Location(LocationType.STRAWBERRY, 654)]),
            "viv3": Room(4, [Transition("viv3x", [[ItemName.MOVING_TOUCH_SWITCH]])]),
            "viv3x": Room(5, [Transition("viv4")]),
            "viv4": Room(6, [Transition("viv5")]),
            "viv5": Room(7, [Transition("viv5x"), Transition("viv5b")]),
            "viv5b": Room(8, [Transition("viv5")], [Location(LocationType.STRAWBERRY, 1742)]),
            "viv5x": Room(9, [Transition("viv6")]),
            "viv6": Room(10, [Transition("viv7")]),
            "viv7": Room(11, [Transition("viv8"), Transition("viv7b")]),
            "viv7b": Room(12, [Transition("viv7")], [Location(LocationType.STRAWBERRY, 2006)]),
            "viv8": Room(13, [Transition("vivEnd")], [Location(LocationType.STRAWBERRY, 94)]),
            "vivEnd": Room(14, [Transition("vivEB")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "vivEB": Room(15, [Transition("vivEB_")], [Location(LocationType.STRAWBERRY, 2760)]),
            "vivEB_": Room(16, [Transition("_Endgame")], easter_egg_difficult=True),
            "_Endgame": Room(17, [Transition("vivBonus")], easter_egg_difficult=True),
            "vivBonus": Room(18, [], easter_egg_difficult=True)
        }, LevelCategory.ADVANCED, 91
    ),
    LevelName.RAINDROPS_ON_ROSES:
    Level(
        {
            "1": Room(0, [Transition("2"), Transition("1B")], [Location(LocationType.SILVER_BERRY, 1922)], start_room=True),
            "1B": Room(1, [Transition("1")], [Location(LocationType.STRAWBERRY, 264, [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "1B", 261), ItemName.TOUCH_SWITCH]]), Location(LocationType.KEY, 265, [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "1B", 261)]])], key_door_ids=[261]),
            "2": Room(2, [Transition("3", [[ItemName.DASH_CRYSTALS, getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "2", 1818)]]), Transition("2B", [[ItemName.DASH_CRYSTALS]])], [Location(LocationType.KEY, 1986, [[ItemName.DASH_CRYSTALS]])], key_door_ids=[1818]),
            "2B": Room(3, [Transition("2")]),
            "3": Room(4, [Transition("4", [[ItemName.TOUCH_SWITCH]]), Transition("6-bottomleft", [[ItemName.TOUCH_SWITCH]])]),
            "4": Room(5, [Transition("5")]),
            "5": Room(6, [Transition("6")]),
            "6": Room(7, [Transition("7")], [Location(LocationType.STRAWBERRY, 102)]),
            "6-bottomleft": Room(100, [Transition("3")], [Location(LocationType.STRAWBERRY, 4266)], is_subregion_of="6"),
            "7": Room(8, [Transition("8", [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "7", 2971), getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "7", 3342), getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "7", 3352)]])], [Location(LocationType.KEY, 3007), Location(LocationType.KEY, 2513), Location(LocationType.KEY, 3274, [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "7", 2971)]]), Location(LocationType.KEY, 3361, [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "7", 2971)]]), Location(LocationType.KEY, 3336, [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "7", 2971)]])], key_door_ids=[2971, 3342, 3352]),
            "8": Room(9, [Transition("9", [[getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "8", 2980), getKeyDoorName(LevelName.RAINDROPS_ON_ROSES, "8", 3754)]])], [Location(LocationType.STRAWBERRY, 4916), Location(LocationType.LEVEL_CLEAR_MINI_HEART)], key_door_ids=[2980, 3754]),
            "9": Room(10, [Transition("8")])
        }, LevelCategory.ADVANCED, 92
    ),
    LevelName.MANGO_MESA:
    Level(
        {
            "Start": Room(0, [Transition("heartside_oppen_intro")], start_room=True),
            "heartside_oppen_intro": Room(1, [Transition("heartside_oppen_a")]),
            "heartside_oppen_a": Room(2, [Transition("heartside_Worldwaker2", [[ItemName.CRUMBLING_PLATFORM]]), Transition("heartside_oppen_b", [[ItemName.CRUMBLING_PLATFORM]]), Transition("heartside_oppen_c", [[ItemName.CRUMBLING_PLATFORM]])], [Location(LocationType.GOLDEN_BERRY, 18, heartside_golden)]),
            "heartside_oppen_b": Room(3, [Transition("heartside_oppen_a")]),
            "heartside_oppen_c": Room(4, [Transition("heartside_oppen_a")]),
            "heartside_Worldwaker2": Room(5, [Transition("heartside_TiltTheStars", [[ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "heartside_TiltTheStars": Room(6, [Transition("heartside_Galaksyz", [[ItemName.HONEY_BUBBLES, ItemName.PURPLE_REBOUND_BUBBLE, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "heartside_Galaksyz": Room(7, [Transition("heartside_mmm", [[ItemName.RED_BUBBLES, ItemName.SOAP_BUBBLE, ItemName.GRAY_BUBBLES, ItemName.SPRINGS, ItemName.GREEN_BUBBLES]])]),
            "heartside_mmm": Room(8, [Transition("Crest", [[ItemName.BOUNCY_SPIKES, ItemName.MOMENTUM_SPRING]])]),
            "Crest": Room(9, [Transition("heartside_MousseMoose")], checkpoint="Crest"),
            "heartside_MousseMoose": Room(10, [Transition("heartside_Meario", [[ItemName.SPRINGS, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_CRYSTALS, ItemName.RED_CASSETTE_SWAP_BLOCK, ItemName.YELLOW_MOVING_CASSETTE_BLOCK, ItemName.GREEN_CASSETTE, ItemName.ORANGE_CASSETTE_BLOCK, ItemName.BLUE_CASSETTE, ItemName.PINK_TRAFFIC_CASSETTE, ItemName.PURPLE_CASSETTE_BLOCK]])]),
            "heartside_Meario": Room(11, [Transition("heartside_YaGrillRobib", [[ItemName.DREAM_TRAFFIC_BLOCK]])]),
            "heartside_YaGrillRobib": Room(12, [Transition("heartside_maladroit", [[ItemName.FAKE_CRYSTAL_HEART, ItemName.CRUMBLING_PLATFORM]])]),
            "heartside_maladroit": Room(13, [Transition("heartside_pugroy", [[ItemName.MOVING_BLOCK, ItemName.PUFFER_FISH, ItemName.JELLYFISH]])]),
            "heartside_pugroy": Room(14, [Transition("Ravine", [[ItemName.CRYSTAL_BOMB]])]),
            "Ravine": Room(15, [Transition("heartside_astraxel")], checkpoint="Ravine"),
            "heartside_astraxel": Room(16, [Transition("heartside_Tortoise", [[ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.BLUE_TIME_CRYSTAL, ItemName.TOUCH_SWITCH, ItemName.KEVIN, ItemName.GRAY_TIME_CRYSTAL]])]),
            "heartside_Tortoise": Room(17, [Transition("heartside_Tortoise_B", [[ItemName.MOVING_PLATFORM, ItemName.GROWTH_POTION, ItemName.DASH_SWITCH]])]),
            "heartside_Tortoise_B": Room(18, [Transition("heartside_bluexans")]),
            "heartside_bluexans": Room(19, [Transition("heartside_Vamp", [[ItemName.PURPLE_JELLYFISH, ItemName.SPRINGS, ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.CRUMBLING_PLATFORM]])]),
            "heartside_Vamp": Room(20, [Transition("heartside_Julia", [[ItemName.GRAVITY_FIELD]])]),
            "heartside_Julia": Room(21, [Transition("Aquifer", [[ItemName.JELLYFISH, ItemName.MOVING_TOUCH_SWITCH, ItemName.CORE_BLOCK, ItemName.DREAM_BLOCK, ItemName.PUFFER_FISH]])]),
            "Aquifer": Room(22, [Transition("heartside_sp1029")], checkpoint="Aquifer"),
            "heartside_sp1029": Room(23, [Transition("heartside_hennyburgr", [[ItemName.DASH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.THROW_BOX, ItemName.RED_PORTAL, ItemName.BLUE_PORTAL, ItemName.PURPLE_PORTAL, ItemName.GREEN_PORTAL, ItemName.YELLOW_PORTAL]])]),
            "heartside_hennyburgr": Room(24, [Transition("heartside_Indecx", [[ItemName.MOVING_PLATFORM, ItemName.SWAP_BLOCK]])]),
            "heartside_Indecx": Room(25, [Transition("heartside_Nic", [[ItemName.RED_LINKED_TRAFFIC_BLOCK]])]),
            "heartside_Nic": Room(26, [Transition("heartside_Ian", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASHLESS_SPRING]])]),
            "heartside_Ian": Room(27, [Transition("Landing", [[ItemName.DREAM_DASH_CRYSTAL, ItemName.DREAM_BLOCK]])]),
            "Landing": Room(28, [Transition("heartside_citrea")], checkpoint="Landing"),
            "heartside_citrea": Room(29, [Transition("heartside_RadleyMcTuneston", [[ItemName.DASH_CRYSTALS, ItemName.TOGGLE_SWAP_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "heartside_RadleyMcTuneston": Room(30, [Transition("heartside_Goldian", [[ItemName.MOVING_BLOCK, ItemName.WORMHOLE_BUBBLE, ItemName.TRAFFIC_BLOCKS, ItemName.TOUCH_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_SWITCH, ItemName.SPRINGS]])]),
            "heartside_Goldian": Room(31, [Transition("heartside_jolly", [[ItemName.PULL_STATION_BLOCK, ItemName.SWITCH_CRATE, ItemName.PUSH_STATION_BLOCK]])]),
            "heartside_jolly": Room(32, [Transition("heartside_Viv", [[ItemName.RED_BUBBLES]])]),
            "heartside_Viv": Room(33, [Transition("Fin", [[ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "Fin": Room(34, [], [Location(LocationType.CRYSTAL_HEART)])
        }, LevelCategory.ADVANCED_HEARTSIDE, 93, heartside_access
    )
}