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


game_name = Constants.game_name

class CelesteModdedWebWorld(WebWorld):
    theme = "partyTime"
    
    tutorial = Tutorial(
        tutorial_name="Placeholder Name",
        description="Placeholder Description",
        language="English",
        file_name="tutorial.md",
        link="",
        authors=["Carden"]
    )
    
    tutorials = [
        tutorial
    ]
    
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
        #validate()
        self.levels_categories_in_play.add(LevelCategory.A_SIDE)
        options = self.options
        
        Options.map_options(self)
        
        match self.options.start_level_set:
            case 0:
                self.start_level_set = LevelCategory.A_SIDE
            case 1:
                self.start_level_set = LevelCategory.BEGINNER
            case 2:
                self.start_level_set = LevelCategory.INTERMEDIATE
            case 3:
                self.start_level_set = LevelCategory.ADVANCED
            case 4:
                self.start_level_set = LevelCategory.EXPERT
            case 5:
                self.start_level_set = LevelCategory.GRANDMASTER
            case _:
                self.start_level_set = LevelCategory.A_SIDE
                
        match self.options.win_condition_level:
            case 0:
                self.win_condition_level = LevelName.SUMMIT_A
            case 1:
                self.win_condition_level = LevelName.SUMMIT_B
            case 2:
                self.win_condition_level = LevelName.FAREWELL
            case 3:
                self.win_condition_level = LevelName.BLUEBERRY_BAY
            case 4:
                self.win_condition_level = LevelName.RASPBERRY_ROOTS
            case 5:
                self.win_condition_level = LevelName.MANGO_MESA
            case 6:
                self.win_condition_level = LevelName.STARFRUIT_SUPERNOVA
            case 7:
                self.win_condition_level = LevelName.PASSIONFRUIT_PANTHEON
            case _:
                self.win_condition_level = LevelName.SUMMIT_A
        
        if options.include_beginner or options.start_level_set == LevelCategory.BEGINNER:
            self.levels_categories_in_play.add(LevelCategory.BEGINNER)
        if options.include_intermediate or options.start_level_set == LevelCategory.INTERMEDIATE:
            self.levels_categories_in_play.add(LevelCategory.INTERMEDIATE)
        if options.include_advanced or options.start_level_set == LevelCategory.ADVANCED:
            self.levels_categories_in_play.add(LevelCategory.ADVANCED)
        if options.include_expert or options.start_level_set == LevelCategory.EXPERT:
            self.levels_categories_in_play.add(LevelCategory.EXPERT)
        if options.include_grandmaster or options.start_level_set == LevelCategory.GRANDMASTER:
            self.levels_categories_in_play.add(LevelCategory.GRANDMASTER)
        if options.include_cracked_grandmaster:
            self.levels_categories_in_play.add(LevelCategory.CRACKED_GRANDMASTER)
        if options.include_b_sides:
            self.levels_categories_in_play.add(LevelCategory.B_SIDE)
        if options.include_c_sides:
            self.levels_categories_in_play.add(LevelCategory.C_SIDE)
            self.levels_categories_in_play.add(LevelCategory.B_SIDE)
        if options.include_farewell:
            self.levels_categories_in_play.add(LevelCategory.FAREWELL)
            
        LogicParser.calculate_strawberries(self)
                 
    def create_regions(self) -> None:
        LogicParser.parse_regions(self)
    
    def create_item(self, name: str) -> ModdedCelesteItem:
        classification = ItemClassification.filler
        try:
            if self.item_type_dict[name] in {ItemType.KEY_DOOR, ItemType.MECHANIC, ItemType.LEVEL}:
                classification = ItemClassification.progression
            elif self.item_type_dict[name] in {ItemType.CHECKPOINT, ItemType.CRYSTAL_HEART_SJ, ItemType.CRYSTAL_HEART_VANILLA, ItemType.STRAWBERRY, ItemType.MOON_BERRY, ItemType.SILVER_BERRY, ItemType.VICTORY, ItemType.GEM}:
                classification = ItemClassification.progression_skip_balancing
        except KeyError:
            raise KeyError(f"Tried to create item that does not exist in item table: {name}")
        return ModdedCelesteItem(name, classification, self.item_name_to_id[name], self.player)
        
    def create_items(self) -> None:
        LogicParser.create_items(self)
        
    def fill_slot_data(self):
        return {
            "start_level_set": self.options.start_level_set.value,
            "include_beginner": self.options.include_beginner.value,
            "include_intermediate": self.options.include_intermediate.value,
            "include_advanced": self.options.include_advanced.value,
            "include_expert": self.options.include_expert.value,
            "include_grandmaster": self.options.include_grandmaster.value,
            "include_cracked_grandmaster": self.options.include_cracked_grandmaster.value,
            "include_b_sides": self.options.include_b_sides.value,
            "include_c_sides": self.options.include_c_sides.value,
            "include_farewell": self.options.include_farewell.value,
            
            "randomize_checkpoints": self.options.randomize_checkpoints.value,
            "room_checks": self.options.room_checks.value,
            
            "include_heart_side_golden": self.options.include_heart_side_golden.value,
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
            
            "required_strawberries": self.required_strawberries
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