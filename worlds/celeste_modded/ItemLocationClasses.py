from BaseClasses import Item, Location
from .constants import Constants


class ModdedCelesteLocation(Location):
    game: str = Constants.game_name

class ModdedCelesteItem(Item):
    game: str = Constants.game_name