from BaseClasses import Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .ItemLocationClasses import ModdedCelesteItem
from .ValidateLayout import validate
from .Options import CelesteModdedOptions, groups
from .constants.ItemNames import ItemName
from .constants.LevelNames import LevelName, LevelCategory
from .constants import Constants
from .constants.ItemTypes import ItemType
from .constants.LocationTypes import LocationType
from . import LogicParser

# TODO
# - All levels showing as complete in journal
# - Look into making the AP connection UI work a bit better
# - Heart gates open except goal level option
# - Automatically collect no-gameplay room locations
# - Hard logic
# - Disable mini-strawberries
# - Refactor c# mapping to grab all the data from slot data rather than copying it over manually

game_name = Constants.game_name

WORLD_VERSION = "1.2.0"
MINIMUM_MOD_VERSION = "1.2.0"

class CelesteModdedWebWorld(WebWorld):
    theme = "partyTime"
    
    option_groups = groups

class CelesteModdedWorld(World):
    
    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        
        self.levels_categories_in_play: set[LevelCategory] = set()
        self.room_check_categories: set[LevelCategory] = set()
        self.location_types_in_play: set[LocationType] = set()
        self.item_types_in_play: set[ItemType] = set()
        self.deathless_categories_in_play: set[LevelCategory] = set()
        
        self.item_type_dict: dict[str, ItemType] = LogicParser.item_type_dict
        self.location_type_dict: dict[str, LocationType] = LogicParser.location_type_dict
        
        self.total_strawberries_generated = 0
        self.required_strawberries = 0
        self.start_items_needed = 0
        self.start_locations_created = 0
        self.precollected_items = 0
        
    
    game = game_name
    web = CelesteModdedWebWorld()
    options_dataclass = CelesteModdedOptions
    options: CelesteModdedOptions
    topology_present = True
        
    item_name_to_id: dict[str, int] = LogicParser.item_id_table
    location_name_to_id: dict[str, int] = LogicParser.location_id_table
    
    start_level_set: LevelCategory
    win_condition_level: LevelName
    consolidation_mapping: dict[str, str]
        
    def generate_early(self) -> None:
        options = self.options
        
        Options.map_options(self)
            
        LogicParser.calculate_strawberries(self)
                 
    def create_regions(self) -> None:
        LogicParser.parse_regions(self)
    
    def create_item(self, name: str) -> ModdedCelesteItem:
        # Normalize ItemName StrEnum members to plain strings before creating AP Items. (Thank you to Littlemuzz5 for this)
        if isinstance(name, ItemName):
            name = name.value
        classification = ItemClassification.filler
        try:
            if self.item_type_dict[name] in {ItemType.KEY_DOOR, ItemType.MECHANIC, ItemType.LEVEL}:
                classification = ItemClassification.progression
            elif self.item_type_dict[name] in {ItemType.CHECKPOINT, ItemType.CRYSTAL_HEART_SJ, ItemType.CRYSTAL_HEART_VANILLA, ItemType.STRAWBERRY, ItemType.MOON_BERRY, ItemType.VICTORY, ItemType.GEM}:
                classification = ItemClassification.progression_skip_balancing
        except KeyError:
            raise KeyError(f"Tried to create item that does not exist in item table: {name}")
        return ModdedCelesteItem(name, classification, self.item_name_to_id[name], self.player)
        
    def create_items(self) -> None:
        LogicParser.create_items(self)


    def fill_slot_data(self):
        return {
            "include_beginner": LevelCategory.BEGINNER in self.levels_categories_in_play,
            "include_intermediate": LevelCategory.INTERMEDIATE in self.levels_categories_in_play,
            "include_advanced": LevelCategory.ADVANCED in self.levels_categories_in_play,
            "include_expert": LevelCategory.EXPERT in self.levels_categories_in_play,
            "include_grandmaster": LevelCategory.GRANDMASTER in self.levels_categories_in_play,
            "include_a_sides": LevelCategory.A_SIDE in self.levels_categories_in_play,
            "include_b_sides": LevelCategory.B_SIDE in self.levels_categories_in_play,
            "include_c_sides": LevelCategory.C_SIDE in self.levels_categories_in_play,
            "include_farewell": LevelCategory.FAREWELL in self.levels_categories_in_play,
            "start_level_set": self.options.start_level_set.value,
            "heart_sides_start_unlocked": self.options.heart_sides_start_unlocked.value,
            "exclude_puzzle_levels": self.options.exclude_puzzle_levels.value,
            
            "randomize_checkpoints": self.options.randomize_checkpoints.value,
            "winged_golden": self.options.winged_golden.value,
            "item_consolidation_mode": self.options.item_consolidation_mode.value,

            "room_checks": self.options.room_checks.value,
            "room_checks_a_side": self.options.room_checks_a_side.value,
            "room_checks_b_side": self.options.room_checks_b_side.value,
            "room_checks_c_side": self.options.room_checks_c_side.value,
            "room_checks_farewell": self.options.room_checks_farewell.value,
            "room_checks_beginner": self.options.room_checks_beginner.value,
            "room_checks_intermediate": self.options.room_checks_intermediate.value,
            "room_checks_advanced": self.options.room_checks_advanced.value,
            "room_checks_expert": self.options.room_checks_expert.value,
            "room_checks_grandmaster": self.options.room_checks_grandmaster.value,
            
            "include_beginner_silvers": self.options.include_beginner_silvers.value,
            "include_intermediate_silvers": self.options.include_intermediate_silvers.value,
            "include_advanced_silvers": self.options.include_advanced_silvers.value,
            "include_expert_silvers": self.options.include_expert_silvers.value,
            "include_grandmaster_silvers": self.options.include_grandmaster_silvers.value,
            "include_a_sides_goldens": self.options.include_a_sides_goldens.value,
            "include_b_sides_goldens": self.options.include_b_sides_goldens.value,
            "include_c_sides_goldens": self.options.include_c_sides_goldens.value,
            "include_farewell_golden": self.options.include_farewell_golden.value,
            
            "win_condition_level": self.options.win_condition_level.value,
            "protect_victory_level_checkpoints": self.options.protect_victory_level_checkpoints.value,
            "strawberries_required_percentage": self.options.strawberries_required_percentage.value,
            "total_strawberries": self.options.total_strawberries.value,
            "require_moon_berry": self.options.require_moon_berry.value,
            "require_berries_for_goal": self.options.require_berries_for_goal.value,
            "required_strawberries": self.required_strawberries,
            "open_heart_gates": self.options.open_heart_gates.value,
            "start_items_needed": self.start_items_needed,
            "precollected_items": self.precollected_items,

            "apworld_version": WORLD_VERSION,
            "minimum_mod_version": MINIMUM_MOD_VERSION,

            "enabled_level_list": LogicParser.getActiveLevelList(self),
            "start_unlocked_level_list": LogicParser.getStartUnlockedLevelList(self),
            "deathless_level_list": LogicParser.getDeathlessLevelList(self),
            "roomcheck_level_list": LogicParser.getRoomCheckLevelList(self)
        }
    
    def get_filler_item_name(self) -> str:
        return self.random.choice([
            ItemName.BLUEBERRY,
            ItemName.BLACKBERRY,
            ItemName.RASPBERRY,
            ItemName.CRANBERRY,
            ItemName.HUCKLEBERRY,
            ItemName.ELDERBERRY
        ])
