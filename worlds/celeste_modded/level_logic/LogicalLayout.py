from dataclasses import dataclass, field
import dataclasses
from worlds.celeste_modded.constants.LocationTypes import LocationType
from worlds.celeste_modded.constants.LevelNames import LevelName, LevelCategory
from worlds.celeste_modded.constants.ItemNames import ItemName
from worlds.celeste_modded.level_logic.VanillaLevels import vanilla_levels
from worlds.celeste_modded.level_logic.VanillaPostGame import vanilla_post_game_levels
from worlds.celeste_modded.level_logic.BeginnerSJ import beginner_levels_sj
from worlds.celeste_open_world.Levels import Level

levelList: dict[LevelName, Level] = vanilla_levels | vanilla_post_game_levels | beginner_levels_sj