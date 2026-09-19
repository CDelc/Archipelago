from worlds.celeste_modded.constants.LevelNames import LevelCategory, LevelName
from worlds.celeste_modded.constants.LocationTypes import LocationType

def getCheckpointName(levelName: LevelName, checkpointName: str):
    return f"{levelName}: {checkpointName}"

def getRoomName(levelName: LevelName, roomName: str):
    return f"{levelName.value} | {roomName}"

def getLocationName(levelName: LevelName, roomName: str, location_type: LocationType, location_id: int = 0):
    name = _getLocationNameNoAlias(levelName, roomName, location_type, location_id)
    if name in _location_alias:
        return _location_alias[name]
    else:
        return name

def _getLocationNameNoAlias(levelName: LevelName, roomName: str, location_type: LocationType, location_id: int):
    name = ""
    if location_type == LocationType.LEVEL_CLEAR_MINI_HEART:
        name = f"Mini Heart: {levelName}"
    elif location_type == LocationType.LEVEL_CLEAR:
        name = f"{levelName} Level Clear"
    elif location_type == LocationType.GOLDEN_BERRY:
        name = f"{levelName} Golden Berry"
    elif location_type == LocationType.SILVER_BERRY:
        name = f"{levelName} Silver Berry"
    elif location_type == LocationType.CASSETTE:
        name = f"{levelName} Cassette"
    elif location_type == LocationType.CRYSTAL_HEART:
        name = f"Crystal Heart: {levelName}"
    else:
        name = f"{getRoomName(levelName, roomName)} - {location_type.value}{"" if not location_id else f":{location_id}"}"
    return name

def getKeyDoorName(levelName: LevelName, roomName: str, id: int):
    name = f"{levelName}:{roomName} Key Door #{id}"
    if name in _item_name_alias:
        return _item_name_alias[name]
    else:
        return name

_location_alias: dict[str, str] = {
    "Summit A-Side | a-06 - gem:110": "Summit 0M Gem",
    "Summit A-Side | b-02d - gem:109": "Summit 500M Gem",
    "Summit A-Side | c-06c - gem:333": "Summit 1000M Gem",
    "Summit A-Side | d-05b - gem:449": "Summit 1500M Gem",
    "Summit A-Side | e-01c - gem:8": "Summit 2000M Gem",
    "Summit A-Side | f-02b - gem:679": "Summit 2500M Gem",
    "Forsaken City A-Side | end - winged_golden_berry:4" : "Forsaken City A-Side | Winged Golden"
}

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
    "Cassette Cliffs:3 Key Door #10": "Cassette Cliffs Door 1",
    "Cassette Cliffs:7 Key Door #494": "Cassette Cliffs Door 2",
    "A Gift From the Stars:Timestop Intro Key Door #237": "A Gift from the Stars Time Crystal Door",
    "A Gift From the Stars:End Key Door #1090": "A Gift from the Stars Secret Door",
    "Paint:b-berry1 Key Door #4235": "Paint Secret Door",
    "Sleeping Under Stars:a_01 Key Door #1858": "Sleeping Under Stars Door 1",
    "Sleeping Under Stars:a_01 Key Door #1860": "Sleeping Under Stars Door 2",
    "Sleeping Under Stars:a_01 Key Door #1862": "Sleeping Under Stars Door 3",
    "Sleeping Under Stars:a_01 Key Door #1864": "Sleeping Under Stars Door 4",
    "Honeyzip Inc:rhub Key Door #225": "Honeyzip Inc Hub Door 1",
    "Honeyzip Inc:rhub Key Door #293": "Honeyzip Inc Hub Door 2",
    "Honeyzip Inc:rhub Key Door #292": "Honeyzip Inc Hub Door 3",
    "Honeyzip Inc:r9 Key Door #498": "Honeyzip Inc Berry Door",
    "Honeyzip Inc:endroomsecret Key Door #1350": "Honeyzip Inc Secret Door",
    "In Filtration:btd-09 Key Door #578": "In Filtration Door",
    "Raspberry Roots:cp2-3-glowwoomii Key Door #7656": "Raspberry Roots Honeyzip Inc Door",
    "Undergrowth:03-a Key Door #776": "Undergrowth Room 3 Door",
    "Undergrowth:06-a Key Door #2912": "Undergrowth End Door",
    "Lost Woods:oppen_intro Key Door #0": "Lost Woods Door 2",
    "Lost Woods:oppen_intro Key Door #1": "Lost Woods Door 1",
    "Lost Woods:oppen_intro Key Door #2": "Lost Woods Door 3",
    "The Lab:hub Key Door #487": "The Lab Hub Door 3",
    "The Lab:hub Key Door #488": "The Lab Hub Door 2",
    "The Lab:hub Key Door #489": "The Lab Hub Door 1",
    "Java's Crypt:3 Key Door #35": "Java's Crypt Small Door",
    "Java's Crypt:4 Key Door #297": "Java's Crypt Medium Door",
    "Java's Crypt:5 Key Door #759": "Java's Crypt Big Door",
    "Raindrops on Roses:1B Key Door #261": "Raindrops on Roses Starting Berry Door",
    "Raindrops on Roses:2 Key Door #1818": "Raindrops on Roses Room 2 Door",
    "Raindrops on Roses:7 Key Door #2971": "Raindrops on Roses Room 7 Mid Door",
    "Raindrops on Roses:7 Key Door #3342": "Raindrops on Roses Ending Door 1",
    "Raindrops on Roses:7 Key Door #3352": "Raindrops on Roses Ending Door Ledge",
    "Raindrops on Roses:8 Key Door #2980": "Raindrops on Roses Post-Heart Door 1",
    "Raindrops on Roses:8 Key Door #3754": "Raindrops on Roses Post-Heart Door 2",
    "Narrow Hollow:6 Key Door #333": "Narrow Hollow Berry Door",
    "Vinculum:a-06 Key Door #443": "Vinculum Door",
    "Cycle Madness B-Side:0 Key Door #1549": "Cycle Madness B-Side Entrance Door",
    "Cycle Madness B-Side:2 Key Door #5812": "Cycle Madness B-Side Huge Mess Door",
    "Ivory:Break My Ivory Tower 2 Key Door #2089": "Ivory True Ending Door",
    "summit:2501M-Berry Key Door #1598": "summit 2501M Berry Door",
    "Passionfruit Pantheon:c2_11-DeathKontrol Key Door #11920": "Passionfruit Pantheon Cycle Madness B-Side Door",
    "Summit A-Side | a-06 - gem:110": "Summit 0M Gem",
    "Summit A-Side | b-02d - gem:109": "Summit 500M Gem",
    "Summit A-Side | c-06c - gem:333": "Summit 1000M Gem",
    "Summit A-Side | d-05b - gem:449": "Summit 1500M Gem",
    "Summit A-Side | e-01c - gem:8": "Summit 2000M Gem",
    "Summit A-Side | f-02b - gem:679": "Summit 2500M Gem"
}