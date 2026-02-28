from enum import StrEnum

from worlds.celeste_modded.constants.LevelNames import LevelCategory

# up_dash = "Up Dash"
# right_dash = "Right Dash"
# down_dash = "Down Dash"
# left_dash = "Left Dash"
# up_right_dash = "Up-Right Dash"
# up_left_dash = "Up-Left Dash"
# down_right_dash = "Down-Right Dash"
# down_left_dash = "Down-Left Dash"

class ItemName(StrEnum):
    
    DASH_CRYSTALS = "Single Dash Crystals"
    TRAFFIC_BLOCKS = "Traffic Blocks"
    SPRINGS = "Springs"
    BLUE_CASSETTE = "Blue Cassette Blocks"
    PINK_CASSETTE = "Pink Cassette Blocks"
    CRUMBLING_PLATFORM = "Crumbling Platform",
    TOUCH_SWITCH = "Touch Switches",
    DREAM_BLOCK = "Normal Dream Blocks",
    BADELINE_ORB = "Badeline Orbs",
    SINKING_PLATFORM = "Sinking Platforms",
    GREEN_BUBBLES = "Blue Bubbles",
    CLOUDS = "Clouds",
    PINK_CLOUDS = "Pink Clouds",
    MOVING_BLOCK = "Moving Blocks",
    RED_BUBBLES = "Red Bubbles",
    SWAP_BLOCK = "Swap Blocks",
    DASH_SWITCH = "Dash Switches",
    FEATHER = "Feather",
    MOVING_PLATFORM = "Moving Platforms",
    WHITE_BLOCK = "White Block",
    SEEKERS = "Seekers",
    THEO_CRYSTAL = "Theo Crystal",
    KEVIN = "Kevins",
    BUMPER = "Bumpers",
    CORE_BLOCK = "Core Blocks",
    CORE_SWITCH = "Core Switches",
    LAVA_ICE_BALLS = "Fire/Ice Balls",
    BREAKER_BOX = "Breaker Boxes",
    BIRD = "Bird",
    JELLYFISH = "Jellyfish",
    PUFFER_FISH = "Puffer fish",
    DOUBLE_DASH_CRYSTALS = "Double Dash Crystals",
    YELLOW_CASSETTE = "Yellow Cassette Blocks",
    GREEN_CASSETTE = "Green Cassette Blocks",
    LOOP_BLOCK = "Loopy Blocks"
    DREAM_DASH_CRYSTAL = "Dream Dash Crystals",
    INTRO_CRUSHER = "Falling/Moving Ice Blocks",
    DASH_TRAFFIC_BLOCK = "Dash-Activated Traffic Blocks",
    BLUE_TRAFFIC_CASSETTE = "Blue Cassette Traffic Blocks",
    PINK_TRAFFIC_CASSETTE = "Pink Cassette Traffic Blocks",
    YELLOW_TRAFFIC_CASSETTE = "Yellow Cassette Traffic Blocks",
    SOAP_BUBBLE = "Soap Bubbles",
    DASHLESS_SPRING = "Dashless Blue Springs",
    SINGLE_JUMP_REFILL = "Single Jump Refills",
    TRIPLE_JUMP_REFILL = "Triple Jump Refills",
    DOUBLE_DASH_DREAM_BLOCK = "Double Dash Dream Blocks"
            
    STRAWBERRY = "Strawberry"
    
    MOON_BERRY = "Moon Berry"
        
    LEVEL_VICTORY = "Win Condition Level Victory"
    
    RASPBERRY = "Raspberry"
    BLUEBERRY = "Blueberry"
    BLACKBERRY = "Blackberry"
    CRANBERRY = "Cranberry"
    ELDERBERRY = "Elderberry"
    HUCKLEBERRY = "Huckleberry"


filler = {
    ItemName.RASPBERRY: 0, ItemName.BLUEBERRY: 1, ItemName.BLACKBERRY: 2, ItemName.CRANBERRY: 3, ItemName.ELDERBERRY: 4, ItemName.HUCKLEBERRY: 5
}

strawberry = {ItemName.STRAWBERRY: 0}

moon_berry = {ItemName.MOON_BERRY: 0}

level_victory = {ItemName.LEVEL_VICTORY: 0}

mechanic = {
    ItemName.DASH_CRYSTALS: 0,
    ItemName.TRAFFIC_BLOCKS: 1,
    ItemName.SPRINGS: 2,
    ItemName.BLUE_CASSETTE: 3,
    ItemName.PINK_CASSETTE: 4,
    ItemName.CRUMBLING_PLATFORM: 5,
    ItemName.TOUCH_SWITCH: 6,
    ItemName.DREAM_BLOCK: 7,
    ItemName.BADELINE_ORB: 8,
    ItemName.SINKING_PLATFORM: 9,
    ItemName.GREEN_BUBBLES: 10,
    ItemName.CLOUDS: 11,
    ItemName.PINK_CLOUDS: 12,
    ItemName.MOVING_BLOCK: 13,
    ItemName.RED_BUBBLES: 14,
    ItemName.SWAP_BLOCK: 15,
    ItemName.DASH_SWITCH: 16,
    ItemName.FEATHER: 17,
    ItemName.MOVING_PLATFORM: 18,
    ItemName.WHITE_BLOCK: 19,
    ItemName.SEEKERS: 20,
    ItemName.THEO_CRYSTAL: 21,
    ItemName.KEVIN: 22,
    ItemName.BUMPER: 23,
    ItemName.CORE_BLOCK: 24,
    ItemName.CORE_SWITCH: 25,
    ItemName.LAVA_ICE_BALLS: 26,
    ItemName.BREAKER_BOX: 27,
    ItemName.BIRD: 28,
    ItemName.JELLYFISH: 29,
    ItemName.PUFFER_FISH: 30,
    ItemName.DOUBLE_DASH_CRYSTALS: 31,
    ItemName.YELLOW_CASSETTE: 32,
    ItemName.GREEN_CASSETTE: 33,
    ItemName.LOOP_BLOCK: 34,
    ItemName.DREAM_DASH_CRYSTAL: 35,
    ItemName.INTRO_CRUSHER: 36,
    ItemName.DASH_TRAFFIC_BLOCK: 37,
    ItemName.BLUE_TRAFFIC_CASSETTE: 38,
    ItemName.PINK_TRAFFIC_CASSETTE: 39,
    ItemName.YELLOW_TRAFFIC_CASSETTE: 40,
    ItemName.SOAP_BUBBLE: 41,
    ItemName.DASHLESS_SPRING: 42,
    ItemName.SINGLE_JUMP_REFILL: 43,
    ItemName.TRIPLE_JUMP_REFILL: 44,
    ItemName.DOUBLE_DASH_DREAM_BLOCK: 45
}

mechanic_categories = {
    ItemName.DASH_CRYSTALS: [],
    ItemName.TRAFFIC_BLOCKS: [],
    ItemName.SPRINGS: [],
    ItemName.BLUE_CASSETTE: [],
    ItemName.PINK_CASSETTE: [],
    ItemName.CRUMBLING_PLATFORM: [],
    ItemName.TOUCH_SWITCH: [],
    ItemName.DREAM_BLOCK: [],
    ItemName.BADELINE_ORB: [],
    ItemName.SINKING_PLATFORM: [],
    ItemName.GREEN_BUBBLES: [],
    ItemName.CLOUDS: [],
    ItemName.PINK_CLOUDS: [],
    ItemName.MOVING_BLOCK: [],
    ItemName.RED_BUBBLES: [],
    ItemName.SWAP_BLOCK: [],
    ItemName.DASH_SWITCH: [],
    ItemName.FEATHER: [],
    ItemName.MOVING_PLATFORM: [],
    ItemName.WHITE_BLOCK: [],
    ItemName.SEEKERS: [],
    ItemName.THEO_CRYSTAL: [],
    ItemName.KEVIN: [],
    ItemName.BUMPER: [],
    ItemName.CORE_BLOCK: [],
    ItemName.CORE_SWITCH: [],
    ItemName.LAVA_ICE_BALLS: [],
    ItemName.BREAKER_BOX: [LevelCategory.FAREWELL],
    ItemName.BIRD: [LevelCategory.FAREWELL],
    ItemName.JELLYFISH: [LevelCategory.FAREWELL],
    ItemName.PUFFER_FISH: [LevelCategory.FAREWELL],
    ItemName.DOUBLE_DASH_CRYSTALS: [LevelCategory.FAREWELL],
    ItemName.YELLOW_CASSETTE: [LevelCategory.FAREWELL],
    ItemName.GREEN_CASSETTE: [LevelCategory.FAREWELL],
    ItemName.LOOP_BLOCK: [LevelCategory.BEGINNER],
    ItemName.DREAM_DASH_CRYSTAL: [LevelCategory.BEGINNER],
    ItemName.INTRO_CRUSHER: [],
    ItemName.DASH_TRAFFIC_BLOCK: [LevelCategory.BEGINNER],
    ItemName.BLUE_TRAFFIC_CASSETTE: [LevelCategory.BEGINNER],
    ItemName.PINK_TRAFFIC_CASSETTE: [LevelCategory.BEGINNER],
    ItemName.YELLOW_TRAFFIC_CASSETTE: [LevelCategory.BEGINNER],
    ItemName.SOAP_BUBBLE: [LevelCategory.BEGINNER],
    ItemName.DASHLESS_SPRING: [LevelCategory.BEGINNER],
    ItemName.SINGLE_JUMP_REFILL: [LevelCategory.BEGINNER],
    ItemName.TRIPLE_JUMP_REFILL: [LevelCategory.BEGINNER],
    ItemName.DOUBLE_DASH_DREAM_BLOCK: [LevelCategory.BEGINNER]
}