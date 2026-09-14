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

_item_name_alias: dict[str, str] = {
    "Celestial Resort A-Side:02-a Key Door #9": "Celestial Resort A-Side Hotel Hallway Door",
    "Celestial Resort A-Side:07-a Key Door #11": "Celestial Resort A-Side Door to Huge Mess",
    "Celestial Resort A-Side:09-b Key Door #2": "Celestial Resort A-Side Huge Mess Door",
    "Celestial Resort A-Side:04-c Key Door #17": "Celestial Resort A-Side Door near Cassette Room",
    "Celestial Resort A-Side:s3 Key Door #16": "Celestial Resort A-Side Hotel Entrance Door",
    "Mirror Temple A-Side:a-13 Key Door #1": "Mirror Temple A-Side Entrance Hallway Door",
    "Mirror Temple A-Side:b-06 Key Door #2": "Mirror Temple A-Side Bubble Hallway Door",
    "Mirror Temple A-Side:b-14 Key Door #3": "Mirror Temple A-Side Crystal Heart Door",
    "Mirror Temple A-Side:d-01 Key Door #310": "Mirror Temple A-Side Search Door 1",
    "Mirror Temple A-Side:d-01 Key Door #301": "Mirror Temple A-Side Search Door 2",
    "Mirror Temple A-Side:d-19 Key Door #531": "Mirror Temple A-Side Search Berry Door",
    "Mirror Temple B-Side:b-00 Key Door #145": "Mirror Temple B-Side Central Chamber Left Door",
    "Mirror Temple B-Side:b-02 Key Door #226": "Mirror Temple B-Side Central Chamber Bubble Blocking Door",
    "Summit A-Side:f-05 Key Door #700": "Summit A-Side Mirror Temple Door",
    "Farewell:d-00 Key Door #471": "Farewell Hub Door 5",
    "Farewell:d-00 Key Door #145": "Farewell Hub Door 4",
    "Farewell:d-00 Key Door #144": "Farewell Hub Door 3",
    "Farewell:d-00 Key Door #142": "Farewell Hub Door 2",
    "Farewell:d-00 Key Door #197": "Farewell Hub Door 1",
    "Cassette Cliffs (SJ Beginner):3 Key Door #10": "Cassette Cliffs Door 1",
    "Cassette Cliffs (SJ Beginner):7 Key Door #494": "Cassette Cliffs Door 2",
    "A Gift From the Stars (SJ Beginner):Timestop Intro Key Door #237": "A Gift from the Stars Time Crystal Door",
    "A Gift From the Stars (SJ Beginner):End Key Door #1090": "A Gift from the Stars Secret Door",
    "Paint (SJ Beginner):b-berry1 Key Door #4235": "Paint Secret Door",
    "Sleeping Under Stars (SJ Intermediate):a_01 Key Door #1858": "Sleeping Under Stars Door 1",
    "Sleeping Under Stars (SJ Intermediate):a_01 Key Door #1860": "Sleeping Under Stars Door 2",
    "Sleeping Under Stars (SJ Intermediate):a_01 Key Door #1862": "Sleeping Under Stars Door 3",
    "Sleeping Under Stars (SJ Intermediate):a_01 Key Door #1864": "Sleeping Under Stars Door 4",
    "Honeyzip Inc (SJ Intermediate):rhub Key Door #225": "Honeyzip Inc Hub Door 1",
    "Honeyzip Inc (SJ Intermediate):rhub Key Door #293": "Honeyzip Inc Hub Door 2",
    "Honeyzip Inc (SJ Intermediate):rhub Key Door #292": "Honeyzip Inc Hub Door 3",
    "Honeyzip Inc (SJ Intermediate):r9 Key Door #498": "Honeyzip Inc Berry Door",
    "Honeyzip Inc (SJ Intermediate):endroomsecret Key Door #1350": "Honeyzip Inc Secret Door",
    "In Filtration (SJ Intermediate):btd-09 Key Door #578": "In Filtration Door",
    "Raspberry Roots (SJ Intermediate Heartside):cp2-3-glowwoomii Key Door #7656": "Raspberry Roots Honeyzip Inc Door",
    "Undergrowth (SJ Advanced):03-a Key Door #776": "Undergrowth Room 3 Door",
    "Undergrowth (SJ Advanced):06-a Key Door #2912": "Undergrowth End Door",
    "Lost Woods (SJ Advanced):oppen_intro Key Door #0": "Lost Woods Door 2",
    "Lost Woods (SJ Advanced):oppen_intro Key Door #1": "Lost Woods Door 1",
    "Lost Woods (SJ Advanced):oppen_intro Key Door #2": "Lost Woods Door 3",
    "The Lab (SJ Advanced):hub Key Door #487": "The Lab Hub Door 3",
    "The Lab (SJ Advanced):hub Key Door #488": "The Lab Hub Door 2",
    "The Lab (SJ Advanced):hub Key Door #489": "The Lab Hub Door 1",
    "Java's Crypt (SJ Advanced):3 Key Door #35": "Java's Crypt Small Door",
    "Java's Crypt (SJ Advanced):4 Key Door #297": "Java's Crypt Medium Door",
    "Java's Crypt (SJ Advanced):5 Key Door #759": "Java's Crypt Big Door",
    "Raindrops on Roses (SJ Advanced):1B Key Door #261": "Raindrops on Roses Starting Berry Door",
    "Raindrops on Roses (SJ Advanced):2 Key Door #1818": "Raindrops on Roses Room 2 Door",
    "Raindrops on Roses (SJ Advanced):7 Key Door #2971": "Raindrops on Roses Room 7 Mid Door",
    "Raindrops on Roses (SJ Advanced):7 Key Door #3342": "Raindrops on Roses Ending Door 1",
    "Raindrops on Roses (SJ Advanced):7 Key Door #3352": "Raindrops on Roses Ending Door Ledge",
    "Raindrops on Roses (SJ Advanced):8 Key Door #2980": "Raindrops on Roses Post-Heart Door 1",
    "Raindrops on Roses (SJ Advanced):8 Key Door #3754": "Raindrops on Roses Post-Heart Door 2",
    "Narrow Hollow (SJ Expert):6 Key Door #333": "Narrow Hollow Berry Door",
    "Vinculum (SJ Expert):a-06 Key Door #443": "Vinculum Door",
    "Cycle Madness B-Side (SJ Grandmaster):0 Key Door #1549": "Cycle Madness B-Side Entrance Door",
    "Cycle Madness B-Side (SJ Grandmaster):2 Key Door #5812": "Cycle Madness B-Side Huge Mess Door",
    "Ivory (SJ Grandmaster):Break My Ivory Tower 2 Key Door #2089": "Ivory True Ending Door",
    "summit (SJ Grandmaster):2501M-Berry Key Door #1598": "summit (SJ Grandmaster) 2501M Berry Door",
    "Passionfruit Pantheon (SJ Grandmaster Heartside):c2_11-DeathKontrol Key Door #11920": "Passionfruit Pantheon Cycle Madness B-Side Door",
}