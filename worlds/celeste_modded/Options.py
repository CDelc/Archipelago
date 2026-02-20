
from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle
from .constants.LevelNames import LevelName, LevelCategory


class IncludeBeginner(DefaultOnToggle):
    """
    Include levels from the beginner lobby
    """
    display_name = "Include Beginner Levels"
    
class IncludeIntermediate(DefaultOnToggle):
    """
    Include levels from the intermediate lobby
    """
    display_name = "Include Intermediate Levels"
    
class IncludeAdvanced(DefaultOnToggle):
    """
    Include levels from the advanced lobby
    """
    display_name = "Include Advanced Levels"
    
class IncludeExpert(DefaultOnToggle):
    """
    Include levels from the expert lobby
    """
    display_name = "Include Expert Levels"
    
class IncludeGrandmaster(DefaultOnToggle):
    """
    Include non-cracked levels from the grandmaster lobby
    """
    display_name = "Include Grandmaster Levels"
    
class IncludeCrackedGrandmaster(DefaultOnToggle):
    """
    Include cracked levels from the grandmaster lobby
    """
    display_name = "Include Cracked Grandmaster Levels"
    
class IncludeBSides(DefaultOnToggle):
    """
    Include vanilla B-Sides
    """
    display_name = "Include B-Sides"
    
class IncludeCSides(DefaultOnToggle):
    """
    Include vanilla C-Sides, this will also enable the B-Sides
    """
    display_name = "Include C-Sides"
    
class IncludeFarewell(DefaultOnToggle):
    """
    Include Farewell from the vanilla game
    """
    display_name = "Include Farewell"
    
class RandomizeCheckpoints(Toggle):
    """
    Add level checkpoints to the item/check pool
    """
    display_name = "Randomize Checkpoints"

class RoomChecks(Toggle):
    """
    Make each room a check
    """
    display_name = "Room Checks"
    
class RandomizeClimb(Toggle):
    """
    Remove the ability to climb at the start and put it in the item pool
    """
    display_name = "Randomize Climb"

class IncludeHeartSideGolden(Toggle):
    """
    Include Golden Berries from Heart Sides (This will only affect Heart Side Levels in lobbies where silvers are already active)
    """
    display_name = "Include Heartside Goldens"

class IncludeBeginnerSilvers(Toggle):
    """
    Include silver berries from the beginner lobby
    """
    display_name = "Include Beginner Silvers"
    
class IncludeIntermediateSilvers(Toggle):
    """
    Include silver berries from the intermediate lobby
    """
    display_name = "Include Intermediate Silvers"
    
class IncludeAdvancedSilvers(Toggle):
    """
    Include silver berries from the advanced lobby
    """
    display_name = "Include Advanced Silvers"
    
class IncludeExpertSilvers(Toggle):
    """
    Include silver berries from the expert lobby
    """
    display_name = "Include Expert Silvers"
    
class IncludeGrandmasterSilvers(Toggle):
    """
    Include non-cracked level silver berries from the grandmaster lobby
    """
    display_name = "Include Grandmaster Silvers"
    
class IncludeCrackedGrandmasterSilvers(Toggle):
    """
    Include cracked level silver berries from the grandmaster lobby
    """
    display_name = "Include Cracked Grandmaster Silvers"
    
class IncludeASideGoldens(Toggle):
    """
    Include vanilla A-Side Goldens
    """
    display_name = "Include A-Sides Goldens"  
    
class IncludeBSideGoldens(Toggle):
    """
    Include vanilla B-Side Goldens
    """
    display_name = "Include B-Sides Goldens"
    
class IncludeCSideGoldens(Toggle):
    """
    Include vanilla C-Side Goldens
    """
    display_name = "Include C-Sides Goldens"
    
class IncludeFarewellGolden(Toggle):
    """
    Include Farewell Golden
    """
    display_name = "Include Farewell Golden"
    
class WinConditionLevel(Choice):
    """
    The Level that must be completed in order to achieve victory
    """
    display_name = "Win Condition Level"
    default = 0
    option_forsaken_city_a = 0
    option_summit_a = 1
    option_summit_b = 2
    option_farewell = 3
    option_beginner_heartside = 4
    option_intermediate_heartside = 5
    option_advanced_heartside = 6
    option_expert_heartside = 7
    option_grandmaster_heartside = 8
    
class ProtectVictoryLevelCheckpoints(DefaultOnToggle):
    """
    Do not randomize checkpoints for the win condition level regardless of the checkpoint setting (ensure it must be completed start to finish)
    """
    display_name = "Protect Win Condition Level Checkpoints"

class StrawberriesRequiredPercentage(Range):
    """
    Percentage of existing strawberries you must receive to complete the game
    """
    display_name = "Strawberry Victory Condition"
    range_start = 0
    range_end = 100
    default = 80
    
class TotalStrawberries(Range):
    """
    Total Strawberries to be placed in the item pool (Actual generated strawberries may be lower depending on availability)
    """
    display_name = "Total Strawberries"
    range_start = 50
    range_end = 500
    default = 300
    
class RequireMoonBerry(Toggle):
    """
    Require that the moon berry be collected in addition to the required strawberries
    """
    display_name = "Require Moon Berry"
    
class LockWinConditionBehindStrawberries(DefaultOnToggle):
    """
    Do not allow access to the win condition level until enough strawberries have been collected
    """
    display_name = "Lock Win Condition Level Behind Strawberries"
    
class StartLevelSet(Choice):
    """
    Which set of levels will be available from the start
    """
    display_name = "Start Level Set"
    option_vanilla_a_sides = 0
    option_beginner_lobby = 1
    option_intermediate_lobby = 2
    option_advanced_lobby = 3
    option_expert_lobby = 4
    option_grandmaster_lobby = 5
    
    default = 0
    
class IncludeWingedGolden(Toggle):
    """
    Include the Winged Golden Berry check in 1A
    """
    display_name = "Winged Golden Berry"
    
def map_options(world):
    start_level_list = [LevelCategory.A_SIDE,
                            LevelCategory.BEGINNER,
                            LevelCategory.INTERMEDIATE,
                            LevelCategory.ADVANCED,
                            LevelCategory.EXPERT,
                            LevelCategory.GRANDMASTER]
    world.start_level_set = start_level_list[world.options.start_level_set.value]
    
    victory_level_list = [LevelName.FORSAKEN_CITY_A,
                                LevelName.SUMMIT_A,
                                LevelName.SUMMIT_B,
                                LevelName.FAREWELL,
                                LevelName.BLUEBERRY_BAY,
                                LevelName.RASPBERRY_ROOTS,
                                LevelName.MANGO_MESA,
                                LevelName.STARFRUIT_SUPERNOVA,
                                LevelName.PASSIONFRUIT_PANTHEON]
    world.win_condition_level = victory_level_list[world.options.win_condition_level.value]

groups = [
    OptionGroup("Levels", [StartLevelSet, IncludeBeginner, IncludeIntermediate, IncludeAdvanced, IncludeExpert, IncludeGrandmaster, IncludeCrackedGrandmaster, IncludeBSides, IncludeCSides, IncludeFarewell]),
    OptionGroup("Checks", [RandomizeClimb, RandomizeCheckpoints, RoomChecks, IncludeWingedGolden]),
    OptionGroup("Deathless Berries", [IncludeHeartSideGolden, IncludeBeginnerSilvers, IncludeIntermediateSilvers, IncludeAdvancedSilvers, IncludeExpertSilvers, IncludeGrandmasterSilvers, IncludeCrackedGrandmasterSilvers, IncludeASideGoldens, IncludeBSideGoldens, IncludeCSideGoldens, IncludeFarewellGolden]),
    OptionGroup("Win Condition", [WinConditionLevel, ProtectVictoryLevelCheckpoints, StrawberriesRequiredPercentage, TotalStrawberries, RequireMoonBerry, LockWinConditionBehindStrawberries])
]

@dataclass
class CelesteModdedOptions(PerGameCommonOptions):
    start_level_set: StartLevelSet
    include_beginner: IncludeBeginner
    include_intermediate: IncludeIntermediate
    include_advanced: IncludeAdvanced
    include_expert: IncludeExpert
    include_grandmaster: IncludeGrandmaster
    include_cracked_grandmaster: IncludeCrackedGrandmaster
    include_b_sides: IncludeBSides
    include_c_sides: IncludeCSides
    include_farewell: IncludeFarewell
    
    randomize_checkpoints: RandomizeCheckpoints
    room_checks: RoomChecks
    
    include_heart_side_golden: IncludeHeartSideGolden
    include_beginner_silvers: IncludeBeginnerSilvers
    include_intermediate_silvers: IncludeIntermediateSilvers
    include_advanced_silvers: IncludeAdvancedSilvers
    include_expert_silvers: IncludeExpertSilvers
    include_grandmaster_silvers: IncludeGrandmasterSilvers
    include_cracked_grandmaster_silvers: IncludeCrackedGrandmasterSilvers
    include_a_sides_goldens: IncludeASideGoldens
    include_b_sides_goldens: IncludeBSideGoldens
    include_c_sides_goldens: IncludeCSideGoldens
    include_farewell_golden: IncludeFarewellGolden
    
    win_condition_level: WinConditionLevel
    protect_victory_level_checkpoints: ProtectVictoryLevelCheckpoints
    strawberries_required_percentage: StrawberriesRequiredPercentage
    total_strawberries: TotalStrawberries
    require_moon_berry: RequireMoonBerry
    lock_win_condition_behind_strawberries: LockWinConditionBehindStrawberries