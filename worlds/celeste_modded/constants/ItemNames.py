from enum import StrEnum

# up_dash = "Up Dash"
# right_dash = "Right Dash"
# down_dash = "Down Dash"
# left_dash = "Left Dash"
# up_right_dash = "Up-Right Dash"
# up_left_dash = "Up-Left Dash"
# down_right_dash = "Down-Right Dash"
# down_left_dash = "Down-Left Dash"

class ItemName(StrEnum):
    
    DASH_CRYSTALS = "Dash Crystals"
    TRAFFIC_BLOCKS = "Traffic Blocks"
    SPRINGS = "Springs"
    BLUE_CASSETTE = "Blue Cassette Blocks"
    PINK_CASSETTE = "Pink Cassette Blocks"
    CRUMBLING_PLATFORM = "Crumbling Platform",
    TOUCH_SWITCH = "Touch Switches",
    DREAM_BLOCK = "Dream Blocks",
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
    WHITE_BLOCK = "White Block"
            
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
    ItemName.WHITE_BLOCK: 19
}