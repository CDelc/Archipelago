from BaseClasses import Item, Location
from worlds.celeste_modded.constants import Constants


class ModdedCelesteLocation(Location):
    game: str = Constants.game_name

class ModdedCelesteItem(Item):
    game: str = Constants.game_name