from typing import TYPE_CHECKING
from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle
from .constants.LevelNames import LevelName, LevelCategory
from .constants.ItemNames import consolidated_mechanics_colors, consolidated_mechanics, consolidated_mechanics_minimal, vanilla_consolidation, extreme_consolidation, no_consolidation, no_mechanics
from .LogicParser import getMaximumDifficulty
if TYPE_CHECKING:
    from . import CelesteModdedWorld

class StrawberryJamMaxDifficulty(Choice):
    """
    Shortcut setting to quickly enable all levels up to a certain difficulty.
    If another setting asks to enable a difficulty higher than the one selected here, this setting will not override it
    If you would like more customization than this, set it to none and use the settings below
    """
    display_name = "Strawberry Jam Select All Up to Difficulty"
    option_none = 0
    option_beginner_green = 1
    option_beginner_yellow = 2
    option_beginner_red = 3
    option_intermediate_green = 4
    option_intermediate_yellow = 5
    option_intermediate_red = 6
    option_advanced_green = 7
    option_advanced_yellow = 8
    option_advanced_red = 9
    option_expert_green = 10
    option_expert_yellow = 11
    option_expert_red = 12
    option_grandmaster_green = 13
    option_grandmaster_yellow = 14
    option_grandmaster_red = 15
    option_grandmaster_cracked = 16

    default = 3

class IncludeBeginner(Choice):
    """
    Include levels from the beginner lobby
    """
    display_name = "Include Beginner Levels"
    option_none = 0
    option_green_only = 1
    option_up_to_yellow = 2
    option_all = 4
    default = 0

class IncludeIntermediate(Choice):
    """
    Include levels from the intermediate lobby
    """
    display_name = "Include Intermediate Levels"
    option_none = 0
    option_green_only = 1
    option_up_to_yellow = 2
    option_all = 4
    default = 0
    
class IncludeAdvanced(Choice):
    """
    Include levels from the advanced lobby
    """
    display_name = "Include Advanced Levels"
    option_none = 0
    option_green_only = 1
    option_up_to_yellow = 2
    option_all = 4
    default = 0
    
class IncludeExpert(Choice):
    """
    Include levels from the expert lobby
    """
    display_name = "Include Expert Levels"
    option_none = 0
    option_green_only = 1
    option_up_to_yellow = 2
    option_all = 4
    default = 0
    
class IncludeGrandmaster(Choice):
    """
    Include non-cracked levels from the grandmaster lobby
    """
    display_name = "Include Grandmaster Levels"
    option_none = 0
    option_green_only = 1
    option_up_to_yellow = 2
    option_up_to_red = 3
    option_all = 4
    default = 0

class IncludeVanillaASides(Toggle):
    display_name = "Include Vanilla A-Sides"

class IncludeVanillaBSides(Toggle):
    display_name = "Include Vanilla B-Sides"

class IncludeVanillaCSides(Toggle):
    display_name = "Include Vanilla C-Sides"
    
class IncludeFarewell(Toggle):
    """
    Include Farewell from the vanilla game, also enables A and B sides
    """
    display_name = "Include Farewell"

class ExcludePuzzleLevels(Toggle):
    """
    Exclude levels that are more about puzzle solving than gameplay. Puzzle levels include the following:
    Dropzle (Beginner)
    A Gift from the Stars (Beginner)
    Pointless Machines (Intermediate)
    Lost Woods (Advanced)
    Java's Crypt (Advanced)
    Lunar Pagoda (Expert)
    """
    display_name = "Exclude Puzzle Levels"
    
class RandomizeCheckpoints(Toggle):
    """
    Add level checkpoints to the item/check pool
    """
    display_name = "Randomize Checkpoints"

class AllRoomChecks(Toggle):
    """
    Make each room a check (Turns all room checks on)
    """
    display_name = "Universal Room Checks"

class RoomChecksASide(Toggle):
    """
    Make each room in the A-Sides a check
    """
    display_name = "A-Side Room Checks"

class RoomChecksBSide(Toggle):
    """
    Make each room in the B-Sides a check
    """
    display_name = "B-Side Room Checks"

class RoomChecksCSide(Toggle):
    """
    Make each room in the C-Sides a check
    """
    display_name = "C-Side Room Checks"

class RoomChecksFarewell(Toggle):
    """
    Make each room in Farewell
    """
    display_name = "Farewell Room Checks"

class RoomChecksBeginnerSJ(Toggle):
    """
    Make each room in Farewell
    """
    display_name = "Beginner Room Checks"

class RoomChecksIntermediateSJ(Toggle):
    """
    Make each room in Farewell
    """
    display_name = "Intermediate Room Checks"

class RoomChecksAdvancedSJ(Toggle):
    """
    Make each room in Farewell
    """
    display_name = "Advanced Room Checks"

class RoomChecksExpertSJ(Toggle):
    """
    Make each room in Farewell
    """
    display_name = "Expert Room Checks"

class RoomChecksGrandmasterSJ(Toggle):
    """
    Make each room in Farewell
    """
    display_name = "Grandmaster Room Checks"

class IncludeEasterEggRooms(Toggle):
    """
    Include hidden easter egg rooms as long as they fit within the difficulty range of the level it is contained in
    """
    display_name = "Include Normal Easter Egg Rooms"

class IncludeEasterEggRoomsDifficult(Toggle):
    """
    Include all hidden easter egg rooms regardless of how difficult they are to access
    """
    display_name = "Include Difficult Easter Egg Rooms"

class IncludeBeginnerSilvers(Toggle):
    """
    Include silver berries from the beginner lobby, this will enable all levels in this lobby
    """
    display_name = "Include Beginner Silvers"
    
class IncludeIntermediateSilvers(Toggle):
    """
    Include silver berries from the intermediate lobby, this will enable all levels in this lobby
    """
    display_name = "Include Intermediate Silvers"
    
class IncludeAdvancedSilvers(Toggle):
    """
    Include silver berries from the advanced lobby, this will enable all levels in this lobby
    """
    display_name = "Include Advanced Silvers"
    
class IncludeExpertSilvers(Toggle):
    """
    Include silver berries from the expert lobby, this will enable all levels in this lobby
    """
    display_name = "Include Expert Silvers"
    
class IncludeGrandmasterSilvers(Toggle):
    """
    Include non-cracked level silver berries from the grandmaster lobby, this will enable all grandmaster levels in this lobby
    """
    display_name = "Include Grandmaster Silvers"
    
class IncludeASideGoldens(Toggle):
    """
    Include vanilla A-Side Goldens
    """
    display_name = "Include A-Sides Goldens"  
    
class IncludeBSideGoldens(Toggle):
    """
    Include vanilla B-Side Goldens, this will enable B side levels
    """
    display_name = "Include B-Sides Goldens"
    
class IncludeCSideGoldens(Toggle):
    """
    Include vanilla C-Side Goldens, this will enable B and C side levels
    """
    display_name = "Include C-Sides Goldens"
    
class IncludeFarewellGolden(Toggle):
    """
    Include Farewell Golden, this will enable Farewell
    """
    display_name = "Include Farewell Golden"
    
class WinConditionLevel(Choice):
    """
    The Level that must be completed in order to achieve victory, this will enable whichever levels are in the same category as the win condition
    """
    display_name = "Win Condition Level"
    default = 3
    option_summit_a = 0
    option_core_a = 10
    option_summit_b = 1
    option_core_b = 8
    option_core_c = 9
    option_farewell = 2
    option_beginner_heartside = 3
    option_intermediate_heartside = 4
    option_advanced_heartside = 5
    option_expert_heartside = 6
    option_grandmaster_heartside = 7
    
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
    default = 50
    
class TotalStrawberries(Range):
    """
    Maximum Strawberries to be placed in the item pool (Actual generated strawberries may be lower depending on availability)
    """
    display_name = "Maximum Strawberries"
    range_start = 0
    range_end = 3000
    default = 500
    
class RequireMoonBerry(Toggle):
    """
    Require that the moon berry be collected in addition to the required strawberries
    """
    display_name = "Require Moon Berry"

class RequireBerriesForGoalLevelEntry(DefaultOnToggle):
    """
    Keep the goal level locked until all required berries are collected
    """
    display_name = "Require Berries for Goal Level"
    
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
    option_none = 6
    option_all_enabled_levels = 7
    
    default = 1
    
class IncludeWingedGolden(Toggle):
    """
    Include the Winged Golden Berry check in 1A
    """
    display_name = "Winged Golden Berry"

class ItemConsildationMode(Choice):
    """
    Select how all of the different mechanics will be consolidated into items that get placed into the item pool. In some cases, mechanics may be considered a combination of multiple unlock items.
    - None - All mechanics and all of their variants will be separately placed into the item pool
    - Mild - All mechanics will be included in the item pool, but different variants of the same mechanic will be consolidated into a single item
    - Balanced - Some less prevalent mechanics will be either wrapped into the unlock of another mechanic or will be enabled from the start
    - Aggressive - Many less prevalent mechanics start unlocked, all others are wrapped into extremely broad unlock items
    - Balanced Colored - Same as balanced, but colors will be added as items into the pool. Mechanics that have color variants will require that mechanic unlock as well as its color item.
    - Vanilla - All vanilla mechanics will be placed into the item pool, all other mechanics will either start enabled or be approximated to a vanilla mechanic
    - No Mechanics - All mechanics start unlocked and mechanic unlocks are not in the item pool
    """
    display_name = "Item Consolidation Mode"
    option_mild = 0
    option_balanced = 1
    option_aggressive = 2
    option_balanced_colored = 3
    option_vanilla = 4
    option_none = 5
    option_no_mechanics = 6

    default = 0

class HeartsidesStartUnlocked(DefaultOnToggle):
    """
    Unlock the heartsides by default, as they are already behind heart gates
    """
    display_name = "Heartsides Start Unlocked"

class OpenHeartGates(Toggle):
    """
    All heart gates start open
    """
    display_name = "Open heart gates"
    
def map_options(world: "CelesteModdedWorld"):

    # Set start level set
    start_level_list = [LevelCategory.A_SIDE,
                            LevelCategory.BEGINNER,
                            LevelCategory.INTERMEDIATE,
                            LevelCategory.ADVANCED,
                            LevelCategory.EXPERT,
                            LevelCategory.GRANDMASTER,
                            LevelCategory.NONE,
                            LevelCategory.ALL]
    world.start_level_set = start_level_list[world.options.start_level_set.value]

    # Set win condition level
    victory_level_list = [LevelName.SUMMIT_A,
                                LevelName.SUMMIT_B,
                                LevelName.FAREWELL,
                                LevelName.BLUEBERRY_BAY,
                                LevelName.RASPBERRY_ROOTS,
                                LevelName.MANGO_MESA,
                                LevelName.STARFRUIT_SUPERNOVA,
                                LevelName.PASSIONFRUIT_PANTHEON,
                                LevelName.CORE_B,
                                LevelName.CORE_C,
                                LevelName.CORE_A]
    world.win_condition_level = victory_level_list[world.options.win_condition_level.value]

    # Set item consolidation map
    item_condolidation_list = [consolidated_mechanics_minimal,
                                    consolidated_mechanics,
                                    extreme_consolidation,
                                    consolidated_mechanics_colors,
                                    vanilla_consolidation,
                                    no_consolidation,
                                    no_mechanics]
    world.consolidation_mapping = item_condolidation_list[world.options.item_consolidation_mode.value]

    # Set active level categories
    if getMaximumDifficulty(LevelCategory.BEGINNER, world):
        world.levels_categories_in_play.add(LevelCategory.BEGINNER)
    if getMaximumDifficulty(LevelCategory.INTERMEDIATE, world):
        world.levels_categories_in_play.add(LevelCategory.INTERMEDIATE)
    if getMaximumDifficulty(LevelCategory.ADVANCED, world):
        world.levels_categories_in_play.add(LevelCategory.ADVANCED)
    if getMaximumDifficulty(LevelCategory.EXPERT, world):
        world.levels_categories_in_play.add(LevelCategory.EXPERT)
    if getMaximumDifficulty(LevelCategory.GRANDMASTER, world):
        world.levels_categories_in_play.add(LevelCategory.GRANDMASTER)
    if world.options.include_a_sides.value:
        world.levels_categories_in_play.add(LevelCategory.A_SIDE)
    if world.options.include_b_sides.value:
        world.levels_categories_in_play.add(LevelCategory.B_SIDE)
    if world.options.include_c_sides.value:
        world.levels_categories_in_play.add(LevelCategory.C_SIDE)
    if world.options.include_farewell.value:
        world.levels_categories_in_play.add(LevelCategory.FAREWELL)

    # Set room checks
    if world.options.room_checks_a_side.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.A_SIDE)
    if world.options.room_checks_b_side.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.B_SIDE)
    if world.options.room_checks_c_side.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.C_SIDE)
    if world.options.room_checks_farewell.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.FAREWELL)
    if world.options.room_checks_beginner.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.BEGINNER)
    if world.options.room_checks_intermediate.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.INTERMEDIATE)
    if world.options.room_checks_advanced.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.ADVANCED)
    if world.options.room_checks_expert.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.EXPERT)
    if world.options.room_checks_grandmaster.value or world.options.room_checks.value:
        world.room_check_categories.add(LevelCategory.GRANDMASTER)

    # Set deathless
    if world.options.include_beginner_silvers.value:
        world.deathless_categories_in_play.add(LevelCategory.BEGINNER)
    if world.options.include_intermediate_silvers.value:
        world.deathless_categories_in_play.add(LevelCategory.INTERMEDIATE)
    if world.options.include_advanced_silvers.value:
        world.deathless_categories_in_play.add(LevelCategory.ADVANCED)
    if world.options.include_expert_silvers.value:
        world.deathless_categories_in_play.add(LevelCategory.EXPERT)
    if world.options.include_grandmaster_silvers.value:
        world.deathless_categories_in_play.add(LevelCategory.GRANDMASTER)
    if world.options.include_a_sides_goldens.value:
        world.deathless_categories_in_play.add(LevelCategory.A_SIDE)
    if world.options.include_b_sides_goldens.value:
        world.deathless_categories_in_play.add(LevelCategory.B_SIDE)
    if world.options.include_c_sides_goldens.value:
        world.deathless_categories_in_play.add(LevelCategory.C_SIDE)
    if world.options.include_farewell_golden.value:
        world.deathless_categories_in_play.add(LevelCategory.FAREWELL)


    import logging
    COLOR_YELLOW = "\033[93m"
    COLOR_RESET = "\033[0m"
    if len(world.room_check_categories - world.levels_categories_in_play) > 0:
        logging.warning(f"{COLOR_YELLOW}[Celeste Modded] Slot {world.player_name} has selected {[category.value for category in world.room_check_categories - world.levels_categories_in_play]} as level categories for room randomization, but these categories have no levels enabled{COLOR_RESET}")
    if len(world.deathless_categories_in_play - world.levels_categories_in_play) > 0:
        logging.warning(f"{COLOR_YELLOW}[Celeste Modded] Slot {world.player_name} has selected {[category.value for category in world.deathless_categories_in_play - world.levels_categories_in_play]} as level categories for deathless berries, but these categories have no levels enabled{COLOR_RESET}")

    if world.start_level_set not in world.levels_categories_in_play:
        logging.warning(f"{COLOR_YELLOW}[Celeste Modded] Slot {world.player_name} has selected {world.start_level_set.value} as the start level set, but has no levels enabled in that set. This setting will be overridden: all levels in {world.start_level_set.value} will be turned on.{COLOR_RESET}")
        match world.start_level_set:
            case LevelCategory.BEGINNER:
                world.levels_categories_in_play.add(LevelCategory.BEGINNER)
                world.options.include_beginner.value = 4
            case LevelCategory.INTERMEDIATE:
                world.levels_categories_in_play.add(LevelCategory.INTERMEDIATE)
                world.options.include_intermediate.value = 4
            case LevelCategory.ADVANCED:
                world.levels_categories_in_play.add(LevelCategory.ADVANCED)
                world.options.include_advanced.value = 4
            case LevelCategory.EXPERT:
                world.levels_categories_in_play.add(LevelCategory.EXPERT)
                world.options.include_expert.value = 4
            case LevelCategory.GRANDMASTER:
                world.levels_categories_in_play.add(LevelCategory.GRANDMASTER)
                world.options.include_grandmaster.value = 4
            case LevelCategory.A_SIDE:
                world.levels_categories_in_play.add(LevelCategory.A_SIDE)
                world.options.include_a_sides.value = True
            case LevelCategory.B_SIDE:
                world.levels_categories_in_play.add(LevelCategory.B_SIDE)
                world.options.include_b_sides.value = True
            case LevelCategory.C_SIDE:
                world.levels_categories_in_play.add(LevelCategory.C_SIDE)
                world.options.include_c_sides.value = True
            case LevelCategory.FAREWELL:
                world.levels_categories_in_play.add(LevelCategory.FAREWELL)
                world.options.include_farewell.value = True
            case _:
                return False

groups = [
    OptionGroup("Items", [ItemConsildationMode, OpenHeartGates]),
    OptionGroup("Levels", [StartLevelSet, StrawberryJamMaxDifficulty, IncludeVanillaASides, IncludeVanillaBSides, IncludeVanillaCSides, IncludeFarewell, IncludeBeginner, IncludeIntermediate, IncludeAdvanced, IncludeExpert, IncludeGrandmaster, HeartsidesStartUnlocked, ExcludePuzzleLevels]),
    OptionGroup("Locations", [RandomizeCheckpoints, IncludeWingedGolden, IncludeEasterEggRooms, IncludeEasterEggRoomsDifficult]),
    OptionGroup("Room Locations", [AllRoomChecks, RoomChecksASide, RoomChecksBSide, RoomChecksCSide, RoomChecksFarewell, RoomChecksBeginnerSJ, RoomChecksIntermediateSJ, RoomChecksAdvancedSJ, RoomChecksExpertSJ, RoomChecksGrandmasterSJ]),
    OptionGroup("Win Condition", [WinConditionLevel, ProtectVictoryLevelCheckpoints, StrawberriesRequiredPercentage, TotalStrawberries, RequireMoonBerry, RequireBerriesForGoalLevelEntry]),
    OptionGroup("Deathless Berries", [IncludeASideGoldens, IncludeBSideGoldens, IncludeCSideGoldens, IncludeFarewellGolden, IncludeBeginnerSilvers, IncludeIntermediateSilvers, IncludeAdvancedSilvers, IncludeExpertSilvers, IncludeGrandmasterSilvers])
]

@dataclass
class CelesteModdedOptions(PerGameCommonOptions):
    include_beginner: IncludeBeginner
    include_intermediate: IncludeIntermediate
    include_advanced: IncludeAdvanced
    include_expert: IncludeExpert
    include_grandmaster: IncludeGrandmaster
    include_farewell: IncludeFarewell
    include_a_sides: IncludeVanillaASides
    include_b_sides: IncludeVanillaBSides
    include_c_sides: IncludeVanillaCSides
    start_level_set: StartLevelSet
    heart_sides_start_unlocked: HeartsidesStartUnlocked
    exclude_puzzle_levels: ExcludePuzzleLevels
    strawberry_jam_max_difficulty: StrawberryJamMaxDifficulty
    
    randomize_checkpoints: RandomizeCheckpoints
    winged_golden: IncludeWingedGolden
    easter_egg_rooms: IncludeEasterEggRooms
    easter_egg_rooms_difficult: IncludeEasterEggRoomsDifficult
    item_consolidation_mode: ItemConsildationMode

    room_checks: AllRoomChecks
    room_checks_a_side: RoomChecksASide
    room_checks_b_side: RoomChecksBSide
    room_checks_c_side: RoomChecksCSide
    room_checks_farewell: RoomChecksFarewell
    room_checks_beginner: RoomChecksBeginnerSJ
    room_checks_intermediate: RoomChecksIntermediateSJ
    room_checks_advanced: RoomChecksAdvancedSJ
    room_checks_expert: RoomChecksExpertSJ
    room_checks_grandmaster: RoomChecksGrandmasterSJ
    
    include_beginner_silvers: IncludeBeginnerSilvers
    include_intermediate_silvers: IncludeIntermediateSilvers
    include_advanced_silvers: IncludeAdvancedSilvers
    include_expert_silvers: IncludeExpertSilvers
    include_grandmaster_silvers: IncludeGrandmasterSilvers
    include_a_sides_goldens: IncludeASideGoldens
    include_b_sides_goldens: IncludeBSideGoldens
    include_c_sides_goldens: IncludeCSideGoldens
    include_farewell_golden: IncludeFarewellGolden
    
    win_condition_level: WinConditionLevel
    protect_victory_level_checkpoints: ProtectVictoryLevelCheckpoints
    strawberries_required_percentage: StrawberriesRequiredPercentage
    total_strawberries: TotalStrawberries
    require_moon_berry: RequireMoonBerry
    require_berries_for_goal: RequireBerriesForGoalLevelEntry
    open_heart_gates: OpenHeartGates
