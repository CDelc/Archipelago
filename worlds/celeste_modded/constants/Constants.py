from worlds.celeste_modded.constants.ItemTypes import ItemType
from worlds.celeste_modded.constants.LocationTypes import LocationType


game_name = "Celeste Modded"
base_id = 0x01000000

_group_id_mult_ = 0x01000000

_item_id_offset_basic = {
    ItemType.VICTORY: 0,
    ItemType.MECHANIC: 1,
    ItemType.CHECKPOINT: 2,
    ItemType.LEVEL: 3,
    ItemType.KEY: 4,
    ItemType.CRYSTAL_HEART_VANILLA: 5,
    ItemType.CRYSTAL_HEART_SJ: 6,
    ItemType.STRAWBERRY: 7,
    ItemType.MOON_BERRY: 8,
    ItemType.SILVER_BERRY: 9,
    ItemType.GEM: 10,
    ItemType.FILLER: 11
}

_location_id_offset_basic = {
    LocationType.STRAWBERRY: 1,
    LocationType.CASSETTE: 2,
    LocationType.LEVEL_CLEAR: 3,
    LocationType.LEVEL_CLEAR_MINI_HEART: 4,
    LocationType.CRYSTAL_HEART: 5,
    LocationType.CHECKPOINT: 6,
    LocationType.KEY: 7,
    LocationType.GOLDEN_BERRY: 8,
    LocationType.SILVER_BERRY: 9,
    LocationType.RAINBOW_BERRY: 10,
    LocationType.WINGED_GOLDEN: 11,
    LocationType.ROOM: 12,
    LocationType.GEM: 13
}

item_id_offset = {**{itemtype: _item_id_offset_basic[itemtype] * _group_id_mult_ for itemtype in _item_id_offset_basic}}
location_id_offset = {**{loc_type: _location_id_offset_basic[loc_type] * _group_id_mult_ for loc_type in _location_id_offset_basic}}