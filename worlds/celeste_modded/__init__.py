from BaseClasses import Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.celeste_modded.ItemLocationClasses import ModdedCelesteItem
from worlds.celeste_modded.ValidateLayout import validate
from .Options import CelesteModdedOptions, groups
from .constants.ItemNames import ItemName
from .constants.LevelNames import LevelName, LevelCategory
from .constants import Constants
from .constants.ItemTypes import ItemType
from .constants.LocationTypes import LocationType
from . import LogicParser

# TODO
# - All levels showing as complete in journal
# - Cassette and Heart text should show item unlock info
# - Allow separate A/B/C side enables
# - More customizable difficulty ceilings
# - Room checks enabled by level category
# - Consolidate mechanics / disable mechanic unlocks
# - Starting inventory instead of 1A opened

game_name = Constants.game_name

WORLD_VERSION = "1.1.1"
MINIMUM_MOD_VERSION = "1.1.1"

class CelesteModdedWebWorld(WebWorld):
    theme = "partyTime"
    
    option_groups = groups

class CelesteModdedWorld(World):
    
    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        
        self.levels_categories_in_play: set[LevelCategory] = set()
        self.location_types_in_play: set[LocationType] = set()
        self.item_types_in_play: set[ItemType] = set()
        
        self.item_type_dict: dict[str, ItemType] = LogicParser.item_type_dict
        self.location_type_dict: dict[str, LocationType] = LogicParser.location_type_dict
        
        self.total_strawberries_generated = 0
        self.required_strawberries = 0
        self.start_items_needed = 0
        self.start_locations_created = 0
        
    
    game = game_name
    web = CelesteModdedWebWorld()
    options_dataclass = CelesteModdedOptions
    options: CelesteModdedOptions
    topology_present = True
        
    item_name_to_id: dict[str, int] = LogicParser.item_id_table
    location_name_to_id: dict[str, int] = LogicParser.location_id_table
    
    start_level_set: LevelCategory
    win_condition_level: LevelName
        
    def generate_early(self) -> None:
        options = self.options
        
        Options.map_options(self)
        
        if options.include_beginner.value or self.start_level_set == LevelCategory.BEGINNER or self.win_condition_level == LevelName.BLUEBERRY_BAY or LogicParser.deathlessEnabled(LevelCategory.BEGINNER, self):
            self.levels_categories_in_play.add(LevelCategory.BEGINNER)
        if options.include_intermediate.value or self.start_level_set == LevelCategory.INTERMEDIATE or self.win_condition_level == LevelName.RASPBERRY_ROOTS or LogicParser.deathlessEnabled(LevelCategory.INTERMEDIATE, self):
            self.levels_categories_in_play.add(LevelCategory.INTERMEDIATE)
        if options.include_advanced.value or self.start_level_set == LevelCategory.ADVANCED or self.win_condition_level == LevelName.MANGO_MESA or LogicParser.deathlessEnabled(LevelCategory.ADVANCED, self):
            self.levels_categories_in_play.add(LevelCategory.ADVANCED)
        if options.include_expert.value or self.start_level_set == LevelCategory.EXPERT or self.win_condition_level == LevelName.STARFRUIT_SUPERNOVA or LogicParser.deathlessEnabled(LevelCategory.EXPERT, self):
            self.levels_categories_in_play.add(LevelCategory.EXPERT)
        if options.include_grandmaster.value or self.start_level_set == LevelCategory.GRANDMASTER or self.win_condition_level == LevelName.PASSIONFRUIT_PANTHEON or LogicParser.deathlessEnabled(LevelCategory.GRANDMASTER, self):
            self.levels_categories_in_play.add(LevelCategory.GRANDMASTER)
        if options.include_cracked_grandmaster.value or self.win_condition_level == LevelName.PASSIONFRUIT_PANTHEON or LogicParser.deathlessEnabled(LevelCategory.CRACKED_GRANDMASTER, self):
            self.levels_categories_in_play.add(LevelCategory.CRACKED_GRANDMASTER)
        if options.include_vanilla_levels.value >= 1 or self.start_level_set == LevelCategory.A_SIDE or self.win_condition_level == LevelName.SUMMIT_A or LogicParser.deathlessEnabled(LevelCategory.A_SIDE, self):
            self.levels_categories_in_play.add(LevelCategory.A_SIDE)
        if options.include_vanilla_levels.value >= 2 or self.win_condition_level == LevelName.SUMMIT_B or LogicParser.deathlessEnabled(LevelCategory.B_SIDE, self):
            self.levels_categories_in_play.add(LevelCategory.B_SIDE)
        if options.include_vanilla_levels.value >= 3 or LogicParser.deathlessEnabled(LevelCategory.C_SIDE, self):
            self.levels_categories_in_play.add(LevelCategory.C_SIDE)
        if options.include_farewell.value or self.win_condition_level == LevelName.FAREWELL or LogicParser.deathlessEnabled(LevelCategory.FAREWELL, self):
            self.levels_categories_in_play.add(LevelCategory.FAREWELL)
            self.levels_categories_in_play.add(LevelCategory.A_SIDE)
            self.levels_categories_in_play.add(LevelCategory.B_SIDE)
            
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
            "include_cracked_grandmaster": LevelCategory.CRACKED_GRANDMASTER in self.levels_categories_in_play,
            "include_a_sides": LevelCategory.A_SIDE in self.levels_categories_in_play,
            "include_b_sides": LevelCategory.B_SIDE in self.levels_categories_in_play,
            "include_c_sides": LevelCategory.C_SIDE in self.levels_categories_in_play,
            "include_farewell": LevelCategory.FAREWELL in self.levels_categories_in_play,
            "start_level_set": self.options.start_level_set.value,
            "heart_sides_start_unlocked": self.options.heart_sides_start_unlocked.value,
            "exclude_puzzle_levels": self.options.exclude_puzzle_levels.value,
            
            "randomize_checkpoints": self.options.randomize_checkpoints.value,
            "room_checks": self.options.room_checks.value,
            "winged_golden": self.options.winged_golden.value,
            
            "include_beginner_silvers": self.options.include_beginner_silvers.value,
            "include_intermediate_silvers": self.options.include_intermediate_silvers.value,
            "include_advanced_silvers": self.options.include_advanced_silvers.value,
            "include_expert_silvers": self.options.include_expert_silvers.value,
            "include_grandmaster_silvers": self.options.include_grandmaster_silvers.value,
            "include_cracked_grandmaster_silvers": self.options.include_cracked_grandmaster_silvers.value,
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

            "apworld_version": WORLD_VERSION,
            "minimum_mod_version": MINIMUM_MOD_VERSION
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
