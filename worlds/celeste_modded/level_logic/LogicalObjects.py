from dataclasses import dataclass
import dataclasses

from ..constants.ItemNames import ItemName
from ..constants.LevelNames import LevelCategory, LevelDifficulty
from ..constants.LocationTypes import LocationType


@dataclass(frozen=True)
class Location:
    location_type: LocationType
    ID: int = 0
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)
    access_hard: list[list[str]] = None
    access_insane: list[list[str]] = None
    access_extreme: list[list[str]] = None
    multi_room_berry: bool = False

@dataclass(frozen=True)
class Transition:
    destination_room: str
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)
    access_hard: list[list[str]] = None
    access_insane: list[list[str]] = None
    access_extreme: list[list[str]] = None
    hard_only: bool = False
    insane_only: bool = False
    
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
    trivial_access: bool = False
    
@dataclass(frozen=True)
class Level:
    rooms: dict[str, Room]
    level_category: LevelCategory
    level_id: int
    level_difficulty: LevelDifficulty = LevelDifficulty.NONE
    access_rule: list[list[str]] = dataclasses.field(default_factory=list)
    access_hard: list[list[str]] = None
    access_insane: list[list[str]] = None
    access_extreme: list[list[str]] = None
    heartside: bool = False
    puzzle: bool = False
    
def CHearts(n: int):
    return f"#{n}"