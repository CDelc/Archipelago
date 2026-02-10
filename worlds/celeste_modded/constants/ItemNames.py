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
    CLIMB = "Climb"
    
    DASH_CRYSTALS = "Dash Crystals"
    TRAFFIC_BLOCKS = "Traffic Blocks"
    SPRINGS = "Springs"
    
    BLUE_CASSETTE = "Blue Cassette Blocks"
    PINK_CASSETTE = "Pink Cassette Blocks"
            
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
    ItemName.CLIMB: 0,
    ItemName.DASH_CRYSTALS: 1,
    ItemName.TRAFFIC_BLOCKS: 2,
    ItemName.SPRINGS: 3,
    ItemName.BLUE_CASSETTE: 4,
    ItemName.PINK_CASSETTE: 5
}