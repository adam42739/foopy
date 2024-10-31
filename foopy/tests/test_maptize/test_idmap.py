from ...nfldata.idmap import IDMap
import pandas
from .create_tests import TEST_MAPS_DIR
import os


def test_maptize():
    map_ids = ["map1"]
    for map_id in map_ids:
        map = pandas.read_csv(os.path.join(TEST_MAPS_DIR, f"{map_id}-map.csv"))
        demap = pandas.read_csv(os.path.join(TEST_MAPS_DIR, f"{map_id}-demap.csv"))
        idmap = IDMap()
        idmap.append(demap)
        idmap.maptize()
        map = map.sort_values(by="id0")
        demap = map.sort_values(by="id0")
        assert map.equals(idmap.df)
