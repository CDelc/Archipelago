from ..Naming import getKeyDoorName, getLocationName
from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelName
from .LogicalObjects import Level, Room, Transition, Location
from ..constants.LocationTypes import LocationType

gmhs_golden_list = [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.GREEN_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.RED_CASSETTE_BLOCK, ItemName.PURPLE_CASSETTE_BLOCK, ItemName.ORANGE_CASSETTE_BLOCK, ItemName.BADELINE_ORB, ItemName.BIRD, ItemName.FEATHER, ItemName.CORE_BLOCK, ItemName.DREAM_BLOCK, ItemName.YELLOW_ROCK, ItemName.DASH_SWITCH, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.JELLYFISH, ItemName.SOAP_BUBBLE, ItemName.BOUNCY_SPIKES, ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.CRUMBLING_PLATFORM, ItemName.BADELINE_ORB, ItemName.TRAFFIC_BLOCKS, ItemName.DREAM_BLOCK, ItemName.SPRINGS, ItemName.GREEN_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.SWAP_BLOCK, ItemName.RED_BUBBLES, ItemName.DASH_SWITCH, ItemName.FEATHER, ItemName.RED_DRUM, ItemName.TOGGLE_DRUM, ItemName.RED_FLYING_LANTERN, ItemName.BLUE_FLYING_LANTERN, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.MOVING_BLOCK, ItemName.BUMPER, ItemName.DOUBLE_DASH_BUMPER, ItemName.ONE_USE_BUMPER, ItemName.MOMENTUM_SPRING, ItemName.DASH_REFILL_WALL, ItemName.BADELINE_ORB, ItemName.CANNON_BALL, ItemName.FAKE_CRYSTAL_HEART, ItemName.SPRINGS, ItemName.DREAM_BLOCK, ItemName.TOUCH_SWITCH, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.FEATHER, ItemName.LAVA_ICE_BALLS, ItemName.FEATHER, ItemName.BADELINE_ORB, ItemName.INFINITE_DASH_FIELD, ItemName.SPRINGS, getKeyDoorName(LevelName.PASSIONFRUIT_PANTHEON, "c2_11-DeathKontrol", 11920), ItemName.MOMENTUM_SPRING, ItemName.GREEN_BUBBLES, ItemName.JUMP_REFILL_WALL, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.RED_BUBBLES, ItemName.DREAM_MOVE_BLOCK, ItemName.MOVING_TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DASH_SWITCH, ItemName.BADELINE_ORB, ItemName.MOVING_BLOCK, ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.TOGGLE_SWAP_BLOCK, ItemName.YELLOW_PORTAL, ItemName.RED_PORTAL, ItemName.SILVER_PORTAL, ItemName.NAVY_PORTAL, ItemName.DREAM_BLOCK, ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH, ItemName.DREAM_DASH_CRYSTAL, ItemName.CRUMBLING_PLATFORM, ItemName.BACKGROUND_SWITCH, ItemName.BADELINE_ORB, ItemName.TOUCH_SWITCH, ItemName.KEVIN, ItemName.DASH_CRYSTALS, ItemName.FEATHER, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.DASH_SWITCH, ItemName.WHITE_LINKED_TRAFFIC_BLOCK, ItemName.BIRD, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_REFILL_WALL, ItemName.JELLYFISH]]
gmhs_access = [[getLocationName(LevelName.SUPERLUMINARY, "end", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.BELLY_OF_THE_BEAST, "a-08", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.WORLD_ABYSS, "a-intro", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.CYCLE_MADNESS_B_SIDE, "10", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.STELLAR_ODYSSEY, "a-04c", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SEVENTY_FOUR, "The End of TIMELINE", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SHATTERSONG, "SHATTER", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.IVORY, "Afterthought", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.SUMMIT_GM, "3000M-02", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.PINBALL_PURGATORY, "pumber", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.CAVE_OF_THE_CRIMSON_SKY, "cotcs-6", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.THE_SOLAR_EXPRESS, "Extraction", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.FLIPSIDE_CLIFFSIDE, "Nostalgia", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.LAVA_LAYER, "Todd", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.KEVINTECHSPAM_BIN, "7", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.NELUMBO, "Lotus", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.DRIFTING_DEEP, "a-11", LocationType.LEVEL_CLEAR_MINI_HEART),
               getLocationName(LevelName.FRACTURED_IRIDESCENCE, "a5", LocationType.LEVEL_CLEAR_MINI_HEART)]]

gm_levels_sj : dict[LevelName, Level] = {
    LevelName.SUPERLUMINARY:
    Level(
        {
            "a-00": Room(0, [Transition("a-01", [[ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 36, [[ItemName.TOGGLE_SWAP_BLOCK, ItemName.SPRINGS, ItemName.PUFFER_FISH, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS]])], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.SPRINGS, ItemName.PUFFER_FISH]])]),
            "a-02": Room(2, [Transition("a-04a", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]]), Transition("a-03", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "a-03": Room(3, [Transition("a-02")], [Location(LocationType.STRAWBERRY, 1517)]),
            "a-04a": Room(4, [Transition("b-04b")]),
            "b-04b": Room(5, [Transition("b-05a", [[ItemName.TOGGLE_SWAP_BLOCK]]), Transition("b-04c")]),
            "b-04c": Room(6, [Transition("b-04b")], [Location(LocationType.STRAWBERRY, 231, [[ItemName.TOGGLE_SWAP_BLOCK]])]),
            "b-05a": Room(7, [Transition("b-05b")]),
            "b-05b": Room(8, [Transition("a-06")]),
            "a-06": Room(9, [Transition("end"), Transition("a-secret")]),
            "a-secret": Room(10, [Transition("a-06")], easter_egg=True),
            "end": Room(11, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 124
    ),
    LevelName.BELLY_OF_THE_BEAST:
    Level(
        {
            "a-01": Room(0, [Transition("a-02intro")], start_room=True),
            "a-02intro": Room(1, [Transition("a-02", [[ItemName.CANNON_BALL]])], [Location(LocationType.SILVER_BERRY, 3518, [[ItemName.CANNON_BALL, ItemName.SPRINGS, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-02": Room(2, [Transition("a-03", [[ItemName.SPRINGS, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-03": Room(3, [Transition("a-04")]),
            "a-04": Room(4, [Transition("a-05")]),
            "a-05": Room(5, [Transition("a-06")]),
            "a-06": Room(6, [Transition("a-07")]),
            "a-07": Room(7, [Transition("a-08")]),
            "a-08": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 125
    ),
    LevelName.WORLD_ABYSS:
    Level(
        {
            "a-intro": Room(0, [Transition("big-1", [[ItemName.MOVING_BLOCK, ItemName.MOVING_TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DREAM_MOVE_BLOCK, ItemName.DASH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 494, [[ItemName.TOUCH_SWITCH, ItemName.MOVING_BLOCK, ItemName.MOVING_TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DREAM_MOVE_BLOCK, ItemName.DASH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS]]), Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.MOVING_BLOCK, ItemName.MOVING_TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DREAM_MOVE_BLOCK, ItemName.DASH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.TOUCH_SWITCH]])], start_room=True),
            "big-1": Room(1, [Transition("chill-0", [[ItemName.SPRINGS]])]),
            "chill-0": Room(2, [Transition("big-2")]),
            "big-2": Room(3, [Transition("chill-sec")]),
            "chill-sec": Room(4, [Transition("big-3")]),
            "big-3": Room(5, [])
        }, LevelCategory.GRANDMASTER, 126
    ),
    LevelName.CYCLE_MADNESS_B_SIDE:
    Level(
        {
            "0": Room(0, [Transition("1", [[getKeyDoorName(LevelName.CYCLE_MADNESS_B_SIDE, "0", 1549)]])], [Location(LocationType.KEY, 1558)], start_room=True, key_door_ids=[1549]),
            "1": Room(1, [Transition("2", [[ItemName.INFINITE_DASH_FIELD]])], [Location(LocationType.SILVER_BERRY, 2350, [[ItemName.MOVING_PLATFORM, ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.INFINITE_DASH_FIELD, getKeyDoorName(LevelName.CYCLE_MADNESS_B_SIDE, "2", 5812)]])]),
            "2": Room(2, [Transition("68a", [[getKeyDoorName(LevelName.CYCLE_MADNESS_B_SIDE, "2", 5812)]]), Transition("5"), Transition("3"), Transition("7")], [Location(LocationType.KEY, 5822, [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.MOVING_PLATFORM, ItemName.SINKING_PLATFORM, ItemName.CRUMBLING_PLATFORM]])], key_door_ids=[5812]),
            "5": Room(3, [Transition("6", [[ItemName.MOVING_PLATFORM]])], [Location(LocationType.STRAWBERRY, 854, [[ItemName.MOVING_PLATFORM, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS]])]),
            "3": Room(4, [Transition("4", [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS]])], [Location(LocationType.STRAWBERRY, 852, [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.MOVING_PLATFORM]])]),
            "7": Room(5, [Transition("8", [[ItemName.SINKING_PLATFORM, ItemName.MOVING_PLATFORM, ItemName.SPRINGS]])], [Location(LocationType.STRAWBERRY, 853, [[ItemName.SINKING_PLATFORM, ItemName.MOVING_PLATFORM, ItemName.SPRINGS]])]),
            "68a": Room(6, [Transition("9")]),
            "68a-left": Room(100, [Transition("2")], is_subregion_of="68a"),
            "68a-right": Room(101, [Transition("2")], is_subregion_of="68a"),
            "9": Room(7, [Transition("10", [[ItemName.MOVING_PLATFORM]])]),
            "10": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE]])]),
            "6": Room(10, [Transition("68a-left", [[ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS]])]),
            "4": Room(11, [Transition("4a", [[ItemName.MOVING_PLATFORM]])]),
            "8": Room(12, [Transition("68a-right")]),
            "4a": Room(13, [Transition("2")])
        }, LevelCategory.GRANDMASTER, 127
    ),
    LevelName.STELLAR_ODYSSEY:
    Level(
        {
            "a-00-start": Room(0, [Transition("a-01")], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.DASH_CRYSTALS, ItemName.MOVING_BLOCK, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS]])], [Location(LocationType.SILVER_BERRY, 6565, [[ItemName.THEO_CRYSTAL, ItemName.SWAP_BLOCK, ItemName.CRUMBLING_PLATFORM, ItemName.JELLYFISH, ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.MOVING_BLOCK, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "a-02": Room(2, [Transition("a-03", [[ItemName.CRUMBLING_PLATFORM, ItemName.JELLYFISH, ItemName.SPRINGS]])], [Location(LocationType.STRAWBERRY, 405, [[ItemName.CRUMBLING_PLATFORM, ItemName.JELLYFISH, ItemName.SPRINGS]])]),
            "a-03": Room(3, [Transition("a-04"), Transition("a-03b")]),
            "a-03b": Room(4, [Transition("a-03")]),
            "a-04": Room(5, [Transition("a-05", [[ItemName.SWAP_BLOCK]]), Transition("a-04b", [[ItemName.SWAP_BLOCK]])], [Location(LocationType.STRAWBERRY, 1179)]),
            "a-04b": Room(6, [Transition("a-04"), Transition("a-04c")]),
            "a-05": Room(7, [Transition("a-06")], [Location(LocationType.STRAWBERRY, 3959)]),
            "a-06": Room(8, [Transition("a-07", [[ItemName.THEO_CRYSTAL]])]),
            "a-07": Room(9, [], [Location(LocationType.STRAWBERRY, 9845, [[ItemName.DASH_SWITCH]])]),
            "a-04c": Room(11, [Transition("a-04")], [Location(LocationType.STRAWBERRY, 4272), Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 128
    ),
    LevelName.SEVENTY_FOUR:
    Level(
        {
            "Overgrown Footpath": Room(0, [Transition("Calling (Bad Reception)", [[ItemName.SINGLE_JUMP_REFILL]]), Transition("Filler Room")], [Location(LocationType.STRAWBERRY, 247, [[ItemName.SINGLE_JUMP_REFILL]])], start_room=True),
            "Filler Room": Room(1, [Transition("Overgrown Footpath")], [Location(LocationType.SILVER_BERRY, 483, [[ItemName.SINGLE_JUMP_REFILL]])]),
            "Calling (Bad Reception)": Room(2, [Transition("Ventilation Ducts")]),
            "Ventilation Ducts": Room(3, [Transition("Attic", [[ItemName.LAVA_ICE_BALLS]])]),
            "Attic": Room(4, [Transition("Nakaniwa Adventure", [[ItemName.CORE_BLOCK, ItemName.SPRINGS]]), Transition("Elevator Shaft", [[ItemName.CORE_BLOCK, ItemName.SPRINGS]])]),
            "Elevator Shaft": Room(5, [Transition("Attic")], [Location(LocationType.STRAWBERRY, 22)]),
            "Nakaniwa Adventure": Room(6, [Transition("Sewers"), Transition("Music Appreciation"), Transition("Broken Resort")]),
            "Music Appreciation": Room(7, [Transition("Nakaniwa Adventure")], [Location(LocationType.STRAWBERRY, 1642)]),
            "Broken Resort": Room(8, [Transition("Nakaniwa Adventure")]),
            "Sewers": Room(9, [Transition("Swimming"), Transition("Kaiten Sushi")]),
            "Kaiten Sushi": Room(10, [Transition("Sewers")], [Location(LocationType.STRAWBERRY, 1292)]),
            "Swimming": Room(11, [Transition("Passenger", [[ItemName.TOUCH_SWITCH]])]),
            "Passenger": Room(12, [Transition("The End of TIMELINE", [[ItemName.FEATHER]])]),
            "The End of TIMELINE": Room(13, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.DASH_CRYSTALS]])])
        }, LevelCategory.GRANDMASTER, 129
    ),
    LevelName.SHATTERSONG:
    Level(
        {
            "Broken Pieces": Room(0, [Transition("First Movement")], [Location(LocationType.SILVER_BERRY, 1414, [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.DASH_REFILL_WALL, ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.GREEN_CASSETTE]])], start_room=True),
            "First Movement": Room(1, [Transition("A1", [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.GREEN_CASSETTE]]), Transition("Runic Archive", [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.GREEN_CASSETTE]])]),
            "Runic Archive": Room(2, [Transition("First Movement")]),
            "A1": Room(3, [Transition("A2", [[ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "A2": Room(4, [Transition("Second Movement", [[ItemName.DASH_REFILL_WALL]]), Transition("Dissonance")]),
            "Dissonance": Room(5, [Transition("A2")], [Location(LocationType.STRAWBERRY, 3087, [[ItemName.JELLYFISH, ItemName.PURPLE_PORTAL, ItemName.SWAP_BLOCK, ItemName.BADELINE_ORB, ItemName.BLUE_PORTAL, ItemName.DASH_SWITCH]])]),
            "Second Movement": Room(6, [Transition("B1")]),
            "B1": Room(7, [Transition("B2")]),
            "B2": Room(8, [Transition("B3")]),
            "B3": Room(9, [Transition("Third Movement"), Transition("Hold")]),
            "Hold": Room(10, [Transition("B3")], [Location(LocationType.STRAWBERRY, 642, [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Third Movement": Room(11, [Transition("C1"), Transition("Welcome Again", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Welcome Again": Room(12, [Transition("Third Movement")], [Location(LocationType.STRAWBERRY, 2222)]),
            "C1": Room(13, [Transition("C2")]),
            "C2": Room(14, [Transition("Cadenza", [[ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("Warning", [[ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("Fading", [[ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Warning": Room(15, [Transition("WARPED")]),
            "Fading": Room(16, [Transition("C2")], [Location(LocationType.STRAWBERRY, 929)]),
            "Cadenza": Room(17, [Transition("Final Movement")]),
            "Final Movement": Room(18, [Transition("SHATTER")]),
            "SHATTER": Room(19, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "WARPED": Room(21, [Transition("C2")], [Location(LocationType.STRAWBERRY, 552, [[ItemName.BLUE_PORTAL, ItemName.PURPLE_PORTAL, ItemName.YELLOW_PORTAL, ItemName.GREEN_PORTAL, ItemName.MINI_FAKE_CRYSTAL_HEART]])])
        }, LevelCategory.GRANDMASTER, 130
    ),
    LevelName.IVORY:
    Level(
        {
            "A Limitless Horizon": Room(0, [Transition("Crowley Scales")], [Location(LocationType.SILVER_BERRY, 1601, [[ItemName.SWAP_BLOCK, ItemName.JUMP_REFILL_WALL, ItemName.BOUNCY_SPIKES, ItemName.DREAM_BLOCK, ItemName.DASH_REFILL_WALL, ItemName.SOAP_BUBBLE, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.JELLYFISH, ItemName.BADELINE_ORB]])], start_room=True),
            "Crowley Scales": Room(1, [Transition("Conspiracy", [[ItemName.DREAM_BLOCK, ItemName.DASH_REFILL_WALL, ItemName.SOAP_BUBBLE, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.JELLYFISH, ItemName.BADELINE_ORB]])]),
            "Conspiracy": Room(2, [Transition("Hawthorne", [[ItemName.JUMP_REFILL_WALL, ItemName.BOUNCY_SPIKES]])]),
            "Hawthorne": Room(3, [Transition("Ascent")]),
            "Ascent": Room(4, [Transition("Ultimatum", [[ItemName.SWAP_BLOCK]]), Transition("Chordless")]),
            "Chordless": Room(5, [Transition("Ascent")], [Location(LocationType.STRAWBERRY, 922, [[ItemName.SWAP_BLOCK]])]),
            "Ultimatum": Room(6, [Transition("Weaver")]),
            "Weaver": Room(7, [Transition("Whale Stitcher"), Transition("Thieves"), Transition("Vexed")]),
            "Thieves": Room(8, [Transition("Weaver")], easter_egg=True),
            "Vexed": Room(9, [Transition("Weaver")], easter_egg=True),
            "Whale Stitcher": Room(10, [Transition("Afterthought")]),
            "Afterthought": Room(11, [Transition("Parasol")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "Parasol": Room(12, [Transition("Break My Ivory Tower 1")]),
            "Break My Ivory Tower 1": Room(13, [Transition("Break My Ivory Tower 2", [[ItemName.SPRINGS, ItemName.KEVIN, ItemName.GREEN_BUBBLES, ItemName.PUFFER_FISH, ItemName.CORE_SWITCH, ItemName.MOVING_BLOCK]])], easter_egg_difficult=True),
            "Break My Ivory Tower 2": Room(14, [Transition("Break My Ivory Tower 4", [[ItemName.FEATHER, ItemName.TRAFFIC_BLOCKS, ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE]]), Transition("Break My Ivory Tower 3", [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE]])], [Location(LocationType.KEY, 1591)], key_door_ids=[2089], easter_egg_difficult=True),
            "Break My Ivory Tower 3": Room(15, [Transition("Break My Ivory Tower 2")], easter_egg_difficult=True),
            "Break My Ivory Tower 4": Room(16, [Transition("Break My Ivory Tower 5", [[ItemName.THEO_CRYSTAL, ItemName.SEEKERS, ItemName.CRUMBLING_PLATFORM]])], easter_egg_difficult=True),
            "Break My Ivory Tower 5": Room(17, [], easter_egg_difficult=True)
        }, LevelCategory.CRACKED_GRANDMASTER, 131
    ),
    LevelName.SUMMIT_GM:
    Level(
        {
            "00": Room(0, [Transition("0000M")], start_room=True),
            "0000M": Room(1, [Transition("0500M", [[ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS, ItemName.BADELINE_ORB]])], [Location(LocationType.SILVER_BERRY, 115, [[ItemName.FEATHER, ItemName.SWAP_BLOCK, ItemName.RED_BUBBLES, ItemName.GREEN_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.MOVING_BLOCK, ItemName.SINKING_PLATFORM, ItemName.MOVING_PLATFORM, ItemName.DREAM_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS, ItemName.CRUMBLING_PLATFORM, ItemName.SPRINGS, ItemName.BADELINE_ORB]])]),
            "0500M": Room(2, [Transition("1000M", [[ItemName.TOUCH_SWITCH, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_CRYSTALS]])]),
            "1000M": Room(3, [Transition("1500M", [[ItemName.DREAM_BLOCK, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "1500M": Room(4, [Transition("2000M", [[ItemName.SINKING_PLATFORM, ItemName.MOVING_PLATFORM]])]),
            "2000M": Room(5, [Transition("2500M", [[ItemName.GREEN_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.MOVING_BLOCK]]), Transition("2000M-Berry", [[ItemName.GREEN_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.MOVING_BLOCK]])]),
            "2000M-Berry": Room(6, [Transition("2000M")], [Location(LocationType.STRAWBERRY, 7162)]),
            "2500M": Room(7, [Transition("2501M", [[ItemName.SWAP_BLOCK, ItemName.RED_BUBBLES]])]),
            "2501M": Room(8, [Transition("3000M-00"), Transition("2501M-Berry")]),
            "2501M-Berry": Room(9, [Transition("2501M")], [Location(LocationType.STRAWBERRY, 1599, [[getKeyDoorName(LevelName.SUMMIT_GM, "2501M-Berry", 1598)]]), Location(LocationType.KEY, 1504, [[ItemName.SEEKERS]])], key_door_ids=[1598]),
            "3000M-00": Room(10, [Transition("3000M-01")]),
            "3000M-01": Room(11, [Transition("3000M-02", [[ItemName.FEATHER]])]),
            "3000M-02": Room(12, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 132
    ),
    LevelName.PINBALL_PURGATORY:
    Level(
        {
            "Insert Coin": Room(0, [Transition("Tutorial")], start_room=True),
            "Tutorial": Room(1, [Transition("Ready?", [[ItemName.BUMPER, ItemName.ONE_USE_BUMPER, ItemName.DOUBLE_DASH_BUMPER, ItemName.MOMENTUM_SPRING, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Ready?": Room(2, [Transition("Helix")], [Location(LocationType.SILVER_BERRY, 3263, [[ItemName.THEO_CRYSTAL, ItemName.MOVING_TOUCH_SWITCH, ItemName.MOVING_BUMPER, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DASH_REFILL_WALL, ItemName.BUMPER, ItemName.ONE_USE_BUMPER, ItemName.DOUBLE_DASH_BUMPER, ItemName.MOMENTUM_SPRING, ItemName.DOUBLE_DASH_CRYSTALS]])]),
            "Helix": Room(3, [Transition("Pursuit", [[ItemName.DASH_CRYSTALS, ItemName.DASH_REFILL_WALL]])]),
            "Pursuit": Room(14, [Transition("Phase", [[ItemName.TOUCH_SWITCH]])]),
            "Phase": Room(4, [Transition("Delta")], [Location(LocationType.STRAWBERRY, 2462)]),
            "Delta": Room(5, [Transition("Symbiosis")]),
            "Symbiosis": Room(6, [Transition("Haste", [[ItemName.MOVING_BUMPER]]), Transition("Instability", [[ItemName.MOVING_BUMPER]])]),
            "Instability": Room(7, [Transition("Symbiosis")], [Location(LocationType.STRAWBERRY, 2816, [[ItemName.MOVING_TOUCH_SWITCH]])]),
            "Haste": Room(8, [Transition("Recoil"), Transition("Rebound")]),
            "Rebound": Room(9, [Transition("Haste")], [Location(LocationType.STRAWBERRY, 3601)]),
            "Recoil": Room(10, [Transition("pumber"), Transition("Extra Ball")]),
            "Extra Ball": Room(11, [Transition("Recoil")], [Location(LocationType.STRAWBERRY, 2820, [[ItemName.THEO_CRYSTAL]])]),
            "pumber": Room(12, [Transition("Malfunction")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "Malfunction": Room(13, [Transition("pumber")], [Location(LocationType.STRAWBERRY, 5214)])
        }, LevelCategory.CRACKED_GRANDMASTER, 133
    ),
    LevelName.CAVE_OF_THE_CRIMSON_SKY:
    Level(
        {
            "cotcs-0B": Room(0, [Transition("cotcs-0")], start_room=True),
            "cotcs-0": Room(1, [Transition("cotcs-1"), Transition("cotcs-0T")], [Location(LocationType.SILVER_BERRY, 308, [[ItemName.SINGLE_JUMP_REFILL, ItemName.DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.MOMENTUM_SPRING, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.TOUCH_SWITCH]])]),
            "cotcs-0T": Room(2, [Transition("cotcs-0")]),
            "cotcs-1": Room(3, [Transition("cotcs-2", [[ItemName.MOMENTUM_SPRING, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.TOUCH_SWITCH]])]),
            "cotcs-2": Room(4, [Transition("cotcs-3", [[ItemName.SINGLE_JUMP_REFILL, ItemName.DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES]]), Transition("cotcs-2B")], [Location(LocationType.STRAWBERRY, 173)]),
            "cotcs-2B": Room(5, [Transition("cotcs-2")]),
            "cotcs-3": Room(6, [Transition("cotcs-4")]),
            "cotcs-4": Room(7, [Transition("cotcs-5")]),
            "cotcs-5": Room(8, [Transition("cotcs-6")], [Location(LocationType.STRAWBERRY, 1486)]),
            "cotcs-6": Room(9, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 134
    ),
    LevelName.THE_SOLAR_EXPRESS:
    Level(
        {
            "All Aboard": Room(0, [Transition("Crumbling Bastions", [[ItemName.DASH_SWITCH, ItemName.CORE_BLOCK, ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS]])], start_room=True),
            "Crumbling Bastions": Room(1, [Transition("Untapped", [[ItemName.DREAM_BLOCK]]), Transition("Domicile A", [[ItemName.DREAM_BLOCK, ItemName.YELLOW_ROCK]])], [Location(LocationType.SILVER_BERRY, 12333, [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DREAM_BLOCK, ItemName.YELLOW_ROCK]])]),
            "Domicile A": Room(2, [Transition("Crumbling Bastions")]),
            "Untapped": Room(3, [Transition("Alexandria", [[ItemName.YELLOW_ROCK]])]),
            "Alexandria": Room(4, [Transition("Crystal Causeway")]),
            "Crystal Causeway": Room(5, [Transition("Miser's Warren", [[ItemName.DASH_CRYSTALS]]), Transition("Domicile B", [[ItemName.DASH_CRYSTALS]])]),
            "Domicile B": Room(6, [Transition("Crystal Causeway")]),
            "Miser's Warren": Room(7, [Transition("Shimmering Expanse", [[ItemName.TOUCH_SWITCH]])]),
            "Shimmering Expanse": Room(8, [Transition("Drill"), Transition("Domicile C")], [Location(LocationType.STRAWBERRY, 21200)]),
            "Domicile C": Room(9, [Transition("Shimmering Expanse")]),
            "Drill": Room(10, [Transition("Alleyway"), Transition("Staging Grounds")]),
            "Alleyway": Room(11, [Transition("Speedway", [[ItemName.PUFFER_FISH]])]),
            "Speedway": Room(12, [Transition("Away")]),
            "Away": Room(13, [Transition("Pilgrim's Way")], [Location(LocationType.STRAWBERRY, 62)]),
            "Pilgrim's Way": Room(14, [Transition("Staging Grounds")], [Location(LocationType.STRAWBERRY, 18656)]),
            "Staging Grounds": Room(15, [Transition("Radiant Obelisk")]),
            "Radiant Obelisk": Room(16, [Transition("Spectacle")]),
            "Spectacle": Room(17, [Transition("Halcyon Promenade")]),
            "Halcyon Promenade": Room(18, [Transition("Arrogance")]),
            "Arrogance": Room(19, [Transition("Luxury Suite")]),
            "Luxury Suite": Room(20, [Transition("Breathe")]),
            "Breathe": Room(21, [Transition("Extraction")]),
            "Extraction": Room(22, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.CRACKED_GRANDMASTER, 135
    ),
    LevelName.FLIPSIDE_CLIFFSIDE:
    Level(
        {
            "Solitude": Room(0, [Transition("Reach", [[ItemName.DREAM_DASH_CRYSTAL, ItemName.BACKGROUND_SWITCH]])], [Location(LocationType.SILVER_BERRY, 1861, [[ItemName.DREAM_DASH_CRYSTAL, ItemName.BACKGROUND_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS]]), Location(LocationType.STRAWBERRY, 373, [[ItemName.DREAM_DASH_CRYSTAL, ItemName.BACKGROUND_SWITCH, ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS]])], start_room=True),
            "Reach": Room(1, [Transition("Glare", [[ItemName.CRUMBLING_PLATFORM, ItemName.DASH_CRYSTALS]])]),
            "Glare": Room(2, [Transition("Basin")]),
            "Basin": Room(3, [Transition("Arrowhead"), Transition("The Crux")]),
            "The Crux": Room(4, [Transition("Basin")], [Location(LocationType.STRAWBERRY, 3590)]),
            "Arrowhead": Room(5, [Transition("Zenith")]),
            "Zenith": Room(6, [Transition("Nostalgia")]),
            "Nostalgia": Room(7, [Transition("The Edge")], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "The Edge": Room(8, [Transition("Nostalgia")], [Location(LocationType.STRAWBERRY, 1729, [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.DOUBLE_DASH_CRYSTALS]])])
        }, LevelCategory.GRANDMASTER, 136
    ),
    LevelName.LAVA_LAYER:
    Level(
        {
            "Bill": Room(0, [Transition("Carol")], [Location(LocationType.SILVER_BERRY, 470, [[ItemName.DASH_CRYSTALS, ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])], start_room=True),
            "Carol": Room(1, [Transition("Fred", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH]])]),
            "Fred": Room(2, [Transition("Jeremy")]),
            "Jeremy": Room(3, [Transition("Kathy")]),
            "Kathy": Room(4, [Transition("Phil", [[ItemName.DASH_CRYSTALS]])]),
            "Phil": Room(5, [Transition("Susan", [[ItemName.SPRINGS]]), Transition("Russel")]),
            "Russel": Room(6, [Transition("Phil"), Transition("oldRussel")], [Location(LocationType.STRAWBERRY, 2619, [[ItemName.SPRINGS]])]),
            "Susan": Room(7, [Transition("Todd"), Transition("gameing_room(for_gameing)")]),
            "gameing_room(for_gameing)": Room(8, [Transition("Susan")], easter_egg=True),
            "Todd": Room(9, [], [Location(LocationType.STRAWBERRY, 566), Location(LocationType.LEVEL_CLEAR_MINI_HEART)]),
            "oldRussel": Room(11, [], easter_egg=True)
        }, LevelCategory.GRANDMASTER, 137
    ),
    LevelName.KEVINTECHSPAM_BIN:
    Level(
        {
            "1": Room(0, [Transition("2", [[ItemName.KEVIN]])], [Location(LocationType.SILVER_BERRY, 1265, [[ItemName.BADELINE_ORB, ItemName.BIRD, ItemName.WHITE_LINKED_TRAFFIC_BLOCK, ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.TOUCH_SWITCH, ItemName.DASH_SWITCH, ItemName.SPRINGS, ItemName.DASH_CRYSTALS, ItemName.KEVIN, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.TRAFFIC_BLOCKS, ItemName.FEATHER, ItemName.DASH_REFILL_WALL]])], start_room=True),
            "2": Room(1, [Transition("3", [[ItemName.DOUBLE_DASH_CRYSTALS, ItemName.JELLYFISH, ItemName.TRAFFIC_BLOCKS, ItemName.FEATHER, ItemName.DASH_REFILL_WALL]])]),
            "3": Room(2, [Transition("4", [[ItemName.DOUBLE_DASH_REFILL_WALL, ItemName.TOUCH_SWITCH, ItemName.DASH_SWITCH, ItemName.SPRINGS, ItemName.DASH_CRYSTALS]])]),
            "4": Room(3, [Transition("5"), Transition("Q4-pleasantsight")]),
            "Q4-pleasantsight": Room(4, [Transition("4")], easter_egg=True),
            "5": Room(5, [Transition("6", [[ItemName.WHITE_LINKED_TRAFFIC_BLOCK]])]),
            "6": Room(6, [Transition("7", [[ItemName.BIRD]])]),
            "7": Room(7, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART, access_rule=[[ItemName.BADELINE_ORB]])])
        }, LevelCategory.GRANDMASTER, 138
    ),
    LevelName.NELUMBO:
    Level(
        {
            "Atrium": Room(0, [Transition("Veranda", [[ItemName.RED_DRUM, ItemName.DASH_CRYSTALS, ItemName.TOGGLE_DRUM, ItemName.RED_FLYING_LANTERN]])], [Location(LocationType.SILVER_BERRY, 1762, [[ItemName.MOVING_BLOCK, ItemName.TOUCH_SWITCH, ItemName.BLUE_FLYING_LANTERN, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.RED_DRUM, ItemName.DASH_CRYSTALS, ItemName.TOGGLE_DRUM, ItemName.RED_FLYING_LANTERN]])], start_room=True),
            "Veranda": Room(1, [Transition("Pier", [[ItemName.TOUCH_SWITCH, ItemName.BLUE_FLYING_LANTERN, ItemName.DOUBLE_DASH_CRYSTALS]]), Transition("Oxbow", [[ItemName.TOUCH_SWITCH]])]),
            "Oxbow": Room(2, [Transition("Veranda")]),
            "Pier": Room(3, [Transition("Backstreet", [[ItemName.MOVING_BLOCK]])]),
            "Backstreet": Room(4, [Transition("Opulence")]),
            "Opulence": Room(5, [Transition("Rat Run")]),
            "Rat Run": Room(6, [Transition("Zigzag")], [Location(LocationType.STRAWBERRY, 581)]),
            "Zigzag": Room(7, [Transition("Lotus")]),
            "Lotus": Room(8, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.CRACKED_GRANDMASTER, 139
    ),
    LevelName.DRIFTING_DEEP:
    Level(
        {
            "a-00": Room(0, [Transition("a-01")], start_room=True),
            "a-01": Room(1, [Transition("a-02", [[ItemName.GREEN_BUBBLES, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.FEATHER, ItemName.RED_BUBBLES]])], [Location(LocationType.SILVER_BERRY, 22145, [[ItemName.DREAM_BLOCK, ItemName.DASH_CRYSTALS, ItemName.GREEN_BUBBLES, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.FEATHER, ItemName.RED_BUBBLES]])]),
            "a-02": Room(2, [Transition("a-03")]),
            "a-03": Room(3, [Transition("a-04", [[ItemName.DASH_CRYSTALS]]), Transition("berry1", [[ItemName.DASH_CRYSTALS]])]),
            "berry1": Room(4, [Transition("a-03")], [Location(LocationType.STRAWBERRY, 10161), Location(LocationType.STRAWBERRY, 9634)]),
            "a-04": Room(5, [Transition("a-05")]),
            "a-05": Room(6, [Transition("a-06")]),
            "a-06": Room(7, [Transition("a-07"), Transition("berry2")]),
            "berry2": Room(8, [Transition("a-06")], [Location(LocationType.STRAWBERRY, 2033)]),
            "a-07": Room(9, [Transition("a-08"), Transition("berry3")]),
            "berry3": Room(10, [Transition("a-07")], [Location(LocationType.STRAWBERRY, 2579, [[ItemName.DREAM_BLOCK]])]),
            "a-08": Room(11, [Transition("a-09", [[ItemName.DREAM_BLOCK]]), Transition("berry4", [[ItemName.DREAM_BLOCK]])]),
            "berry4": Room(12, [Transition("a-08")], [Location(LocationType.STRAWBERRY, 12924)]),
            "a-09": Room(13, [Transition("a-10")]),
            "a-10": Room(14, [Transition("a-11")]),
            "a-11": Room(15, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 140
    ),
    LevelName.FRACTURED_IRIDESCENCE:
    Level(
        {
            "a0": Room(0, [Transition("a1", [[ItemName.DASH_REFILL_WALL, ItemName.TRAFFIC_BLOCKS]])], [Location(LocationType.SILVER_BERRY, 2407, [[ItemName.DASH_REFILL_WALL, ItemName.TRAFFIC_BLOCKS, ItemName.JELLYFISH, ItemName.DASH_CRYSTALS, ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_REFILL_WALL]])], start_room=True),
            "a1": Room(1, [Transition("a2", [[ItemName.JELLYFISH]])]),
            "a2": Room(2, [Transition("a3", [[ItemName.DASH_CRYSTALS]])]),
            "a3": Room(3, [Transition("a4", [[ItemName.TOUCH_SWITCH, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "a4": Room(4, [Transition("a5")]),
            "a5": Room(5, [], [Location(LocationType.LEVEL_CLEAR_MINI_HEART)])
        }, LevelCategory.GRANDMASTER, 141
    ),
    LevelName.PASSIONFRUIT_PANTHEON:
    Level(
        {
            "a0-Start": Room(0, [Transition("a1_18-Xplosives")], start_room=True),
            "a1_18-Xplosives": Room(1, [Transition("a2_17-Todd", [[ItemName.BIRD, ItemName.TRAFFIC_BLOCKS, ItemName.DASH_REFILL_WALL, ItemName.JELLYFISH]])], [Location(LocationType.GOLDEN_BERRY, 9004)]),
            "a2_17-Todd": Room(2, [Transition("a3_16-Cookie", [[ItemName.TOUCH_SWITCH, ItemName.KEVIN, ItemName.DASH_CRYSTALS, ItemName.FEATHER, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS, ItemName.DASH_SWITCH, ItemName.WHITE_LINKED_TRAFFIC_BLOCK]])]),
            "a3_16-Cookie": Room(3, [Transition("b0-Humility", [[ItemName.DREAM_DASH_CRYSTAL, ItemName.CRUMBLING_PLATFORM, ItemName.BACKGROUND_SWITCH, ItemName.BADELINE_ORB]])]),
            "b0-Humility": Room(4, [Transition("b1_15-Alisticious")], checkpoint="Humility"),
            "b1_15-Alisticious": Room(5, [Transition("b2_14-Ecl1psed", [[ItemName.DASH_CRYSTALS, ItemName.TOGGLE_SWAP_BLOCK, ItemName.YELLOW_PORTAL, ItemName.RED_PORTAL, ItemName.SILVER_PORTAL, ItemName.NAVY_PORTAL, ItemName.DREAM_BLOCK, ItemName.PUFFER_FISH, ItemName.TOUCH_SWITCH]])]),
            "b2_14-Ecl1psed": Room(6, [Transition("b3_13-TheDavSmasher", [[ItemName.MOVING_BLOCK, ItemName.SPRINGS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.JELLYFISH]])]),
            "b3_13-TheDavSmasher": Room(7, [Transition("c0-Divinity", [[ItemName.DREAM_MOVE_BLOCK, ItemName.MOVING_TOUCH_SWITCH, ItemName.DASH_SPRING, ItemName.DASH_SWITCH, ItemName.BADELINE_ORB]])]),
            "c0-Divinity": Room(8, [Transition("c1_12-RedBatNick")], checkpoint="Divinity"),
            "c1_12-RedBatNick": Room(9, [Transition("c2_11-DeathKontrol", [[ItemName.MOMENTUM_SPRING, ItemName.GREEN_BUBBLES, ItemName.JUMP_REFILL_WALL, ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.RED_BUBBLES]])]),
            "c2_11-DeathKontrol": Room(10, [Transition("c3_10-fishtank", [[ItemName.INFINITE_DASH_FIELD, ItemName.SPRINGS, getKeyDoorName(LevelName.PASSIONFRUIT_PANTHEON, "c2_11-DeathKontrol", 11920)]])], [Location(LocationType.KEY, 11922, [[ItemName.INFINITE_DASH_FIELD, ItemName.SPRINGS]])], key_door_ids=[11920]),
            "c3_10-fishtank": Room(11, [Transition("d0-Purity", [[ItemName.LAVA_ICE_BALLS, ItemName.FEATHER, ItemName.BADELINE_ORB]])]),
            "d0-Purity": Room(12, [Transition("d1_09-xlibiza")], checkpoint="Purity"),
            "d1_09-xlibiza": Room(13, [Transition("d2_08-Aiden", [[ItemName.DREAM_BLOCK, ItemName.TOUCH_SWITCH, ItemName.GREEN_BUBBLES, ItemName.RED_BUBBLES, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.FEATHER]])]),
            "d2_08-Aiden": Room(14, [Transition("d3_07-Maya", [[ItemName.CANNON_BALL, ItemName.FAKE_CRYSTAL_HEART, ItemName.SPRINGS]])]),
            "d3_07-Maya": Room(15, [Transition("e0-Clarity", [[ItemName.BUMPER, ItemName.DOUBLE_DASH_BUMPER, ItemName.ONE_USE_BUMPER, ItemName.MOMENTUM_SPRING, ItemName.DASH_REFILL_WALL, ItemName.BADELINE_ORB]])]),
            "e0-Clarity": Room(16, [Transition("e1_06-tofu")], checkpoint="Clarity"),
            "e1_06-tofu": Room(17, [Transition("e2_05-ello", [[ItemName.FEATHER, ItemName.RED_DRUM, ItemName.TOGGLE_DRUM, ItemName.RED_FLYING_LANTERN, ItemName.BLUE_FLYING_LANTERN, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.MOVING_BLOCK]])]),
            "e2_05-ello": Room(18, [Transition("e3_04-Linj", [[ItemName.CRUMBLING_PLATFORM, ItemName.BADELINE_ORB, ItemName.TRAFFIC_BLOCKS, ItemName.DREAM_BLOCK, ItemName.SPRINGS, ItemName.GREEN_BUBBLES, ItemName.CLOUDS, ItemName.PINK_CLOUDS, ItemName.SWAP_BLOCK, ItemName.RED_BUBBLES, ItemName.DASH_SWITCH]])]),
            "e3_04-Linj": Room(19, [Transition("f0-Icarus", [[ItemName.JELLYFISH, ItemName.SOAP_BUBBLE, ItemName.BOUNCY_SPIKES, ItemName.DASH_REFILL_WALL, ItemName.DOUBLE_DASH_REFILL_WALL]])]),
            "f0-Icarus": Room(20, [Transition("f1_03-tobyaaa")], checkpoint="Icarus"),
            "f1_03-tobyaaa": Room(21, [Transition("f2_02-Soloiini", [[ItemName.TOUCH_SWITCH, ItemName.DASH_CRYSTALS, ItemName.DOUBLE_DASH_CRYSTALS, ItemName.SPRINGS]])]),
            "f2_02-Soloiini": Room(22, [Transition("f3_01-Hydro", [[ItemName.CORE_BLOCK, ItemName.DREAM_BLOCK, ItemName.YELLOW_ROCK, ItemName.DASH_SWITCH]])]),
            "f3_01-Hydro": Room(23, [Transition("gg_Heart", [[ItemName.BLUE_CASSETTE, ItemName.PINK_CASSETTE, ItemName.GREEN_CASSETTE, ItemName.YELLOW_CASSETTE, ItemName.RED_CASSETTE_BLOCK, ItemName.PURPLE_CASSETTE_BLOCK, ItemName.ORANGE_CASSETTE_BLOCK, ItemName.BADELINE_ORB, ItemName.BIRD, ItemName.FEATHER]])]),
            "gg_Heart": Room(24, [], [Location(LocationType.CRYSTAL_HEART)])
        }, LevelCategory.CRACKED_GRANDMASTER, 142, heartside = True
    )
}