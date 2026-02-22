from worlds.celeste_modded.constants.LevelNames import LevelName
from worlds.celeste_modded.constants.LocationTypes import LocationType


def getCheckpointName(levelName: LevelName, checkpointName: str):
    return f"{levelName}: {checkpointName}"

def getRoomName(levelName: LevelName, roomName: str):
    return f"{levelName.value}:{roomName}"

def getLocationName(levelName: LevelName, roomName: str, location_type: LocationType, location_id: int = 0):
    name = _getLocationNameNoAlias(levelName, roomName, location_type, location_id)
    if name in _location_alias:
        return _location_alias[name]
    else:
        return name

def _getLocationNameNoAlias(levelName: LevelName, roomName: str, location_type: LocationType, location_id: int):
    name = ""
    if location_type == LocationType.LEVEL_CLEAR_MINI_HEART:
        name = f"{levelName} Clear Heart"
    elif location_type == LocationType.LEVEL_CLEAR:
        name = f"{levelName} Level Clear"
    elif location_type == LocationType.GOLDEN_BERRY:
        name = f"{levelName} Golden Berry"
    elif location_type == LocationType.SILVER_BERRY:
        name = f"{levelName} Silver Berry"
    elif location_type == LocationType.CASSETTE:
        name = f"{levelName} Cassette"
    elif location_type == LocationType.CRYSTAL_HEART:
        name = f"{levelName} Crystal Heart"
    else:
        name = f"{getRoomName(levelName, roomName)}:{location_type.value}{"" if not location_id else f":{location_id}"}"
    return name

def getKeyDoorName(levelName: LevelName, roomName: str, id: int):
    name = f"{levelName}:{roomName} Key Door #{id}"
    if name in _item_name_alias:
        return _item_name_alias[name]
    else:
        return name

_location_alias: dict[str, str] = {}
_item_name_alias: dict[str, str] = {}