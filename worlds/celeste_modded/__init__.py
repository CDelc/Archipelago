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

WORLD_VERSION = "0.9.0"

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
        options = self.options
        
        Options.map_options(self)
        
        # match self.options.start_level_set:
        #     case 0:
        #         self.start_level_set = LevelCategory.A_SIDE
        #     case 1:
        #         self.start_level_set = LevelCategory.BEGINNER
        #     case 2:
        #         self.start_level_set = LevelCategory.INTERMEDIATE
        #     case 3:
        #         self.start_level_set = LevelCategory.ADVANCED
        #     case 4:
        #         self.start_level_set = LevelCategory.EXPERT
        #     case 5:
        #         self.start_level_set = LevelCategory.GRANDMASTER
        #     case _:
        #         self.start_level_set = LevelCategory.A_SIDE
                
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
        
        self.start_level_set = LevelCategory.A_SIDE
        if options.include_beginner or self.start_level_set == LevelCategory.BEGINNER or self.win_condition_level == LevelName.BLUEBERRY_BAY or LogicParser.deathlessEnabled(LevelCategory.BEGINNER, self):
            self.levels_categories_in_play.add(LevelCategory.BEGINNER)
        if options.include_intermediate or self.start_level_set == LevelCategory.INTERMEDIATE or self.win_condition_level == LevelName.RASPBERRY_ROOTS or LogicParser.deathlessEnabled(LevelCategory.INTERMEDIATE, self):
            self.levels_categories_in_play.add(LevelCategory.INTERMEDIATE)
        if options.include_advanced or self.start_level_set == LevelCategory.ADVANCED or self.win_condition_level == LevelName.MANGO_MESA or LogicParser.deathlessEnabled(LevelCategory.ADVANCED, self):
            self.levels_categories_in_play.add(LevelCategory.ADVANCED)
        if options.include_expert or self.start_level_set == LevelCategory.EXPERT or self.win_condition_level == LevelName.STARFRUIT_SUPERNOVA or LogicParser.deathlessEnabled(LevelCategory.EXPERT, self):
            self.levels_categories_in_play.add(LevelCategory.EXPERT)
        if options.include_grandmaster or self.start_level_set == LevelCategory.GRANDMASTER or self.win_condition_level == LevelName.PASSIONFRUIT_PANTHEON or LogicParser.deathlessEnabled(LevelCategory.GRANDMASTER, self):
            self.levels_categories_in_play.add(LevelCategory.GRANDMASTER)
        if options.include_cracked_grandmaster or self.win_condition_level == LevelName.PASSIONFRUIT_PANTHEON or LogicParser.deathlessEnabled(LevelCategory.CRACKED_GRANDMASTER, self):
            self.levels_categories_in_play.add(LevelCategory.CRACKED_GRANDMASTER)
        if options.include_vanilla_levels >= 1 or self.start_level_set == LevelCategory.A_SIDE or self.win_condition_level == LevelName.SUMMIT_A or LogicParser.deathlessEnabled(LevelCategory.A_SIDE, self):
            self.levels_categories_in_play.add(LevelCategory.A_SIDE)
        if options.include_vanilla_levels >= 2 or self.win_condition_level == LevelName.SUMMIT_B or LogicParser.deathlessEnabled(LevelCategory.B_SIDE, self):
            self.levels_categories_in_play.add(LevelCategory.B_SIDE)
        if options.include_vanilla_levels >= 3 or LogicParser.deathlessEnabled(LevelCategory.C_SIDE, self):
            self.levels_categories_in_play.add(LevelCategory.C_SIDE)
        if options.include_farewell or self.win_condition_level == LevelName.FAREWELL or LogicParser.deathlessEnabled(LevelCategory.FAREWELL, self):
            self.levels_categories_in_play.add(LevelCategory.FAREWELL)
            self.levels_categories_in_play.add(LevelCategory.A_SIDE)
            self.levels_categories_in_play.add(LevelCategory.B_SIDE)
            
        LogicParser.calculate_strawberries(self)
                 
    def create_regions(self) -> None:
        LogicParser.parse_regions(self)
    
    def create_item(self, name: str) -> ModdedCelesteItem:
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
            
            "required_strawberries": self.required_strawberries,
            "apworld_version": WORLD_VERSION
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