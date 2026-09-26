from dataclasses import dataclass, field
import dataclasses
from ..constants.LocationTypes import LocationType
from ..constants.LevelNames import LevelName, LevelCategory
from ..constants.ItemNames import ItemName
from ..level_logic.VanillaLevels import vanilla_levels
from ..level_logic.VanillaPostGame import vanilla_post_game_levels
from ..level_logic.BeginnerSJ import beginner_levels_sj
from ..level_logic.IntermediateSJ import intermediate_levels_sj
from ..level_logic.AdvancedSJ import advanced_levels_sj
from ..level_logic.ExpertSJ import expert_levels_sj
from ..level_logic.GrandmasterSJ import gm_levels_sj
from ..level_logic.LogicalObjects import Level

levelList: dict[LevelName, Level] = vanilla_levels | vanilla_post_game_levels | beginner_levels_sj | intermediate_levels_sj | advanced_levels_sj | expert_levels_sj | gm_levels_sj