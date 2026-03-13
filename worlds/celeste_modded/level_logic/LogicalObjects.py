from dataclasses import dataclass
import dataclasses

from worlds.celeste_modded.constants.ItemNames import ItemName
from worlds.celeste_modded.constants.LevelNames import LevelCategory
from worlds.celeste_modded.constants.LocationTypes import LocationType


@dataclass(frozen=True)
class Location:
    location_type: LocationType
    ID: int = 0
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)

@dataclass(frozen=True)
class Transition:
    destination_room: str
    access_rule: list[list[ItemName]] = dataclasses.field(default_factory=list)
    
@dataclass(frozen=True)
class Room:
    room_id: int
    transitions: list[Transition]
    locations: list[Location] = dataclasses.field(default_factory=list)
    is_subregion_of: str = None
    start_room: bool = False
    checkpoint: str = None
    easter_egg: bool = False
    easter_egg_difficult: bool = False
    key_door_ids: list[int] = dataclasses.field(default_factory=list)
    
@dataclass(frozen=True)
class Level:
    rooms: dict[str, Room]
    level_category: LevelCategory
    level_id: int
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)
    
def CHearts(n: int):
    return f"#{n}"