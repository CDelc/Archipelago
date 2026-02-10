from enum import StrEnum


class LocationType(StrEnum):
    STRAWBERRY = "strawberry"
    CASSETTE = "cassette"
    LEVEL_CLEAR = "level_clear"
    LEVEL_CLEAR_MINI_HEART = "level_clear_mini_heart"
    CRYSTAL_HEART = "crystal_heart"
    CHECKPOINT = "checkpoint"
    KEY = "key"
    GOLDEN_BERRY = "golden_berry"
    SILVER_BERRY = "silver_berry"
    RAINBOW_BERRY = "rainbow_berry"
    WINGED_GOLDEN = "winged_golden_berry"
    ROOM = "room"
    GEM = "gem"

BEGINNER_RAINBOW_BERRY = "Beginner Rainbow Berry"
INTERMEDIATE_RAINBOW_BERRY = "Intermediate Rainbow Berry"
ADVANCED_RAINBOW_BERRY = "Advanced Rainbow Berry"
EXPERT_RAINBOW_BERRY = "Expert Rainbow Berry"
GRANDMASTER_RAINBOW_BERRY = "Grandmaster Rainbow Berry"

RAINBOW_BERRIES = [BEGINNER_RAINBOW_BERRY, INTERMEDIATE_RAINBOW_BERRY, ADVANCED_RAINBOW_BERRY, EXPERT_RAINBOW_BERRY, GRANDMASTER_RAINBOW_BERRY]