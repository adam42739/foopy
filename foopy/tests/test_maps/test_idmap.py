from ...nfldata.idmap import IDMap
import pandas
from .create_tests import TEST_MAPS_DIR
import os


def test_maptize():
    map_ids = ["map1", "map2"]
    for map_id in map_ids:
        map = pandas.read_csv(
            os.path.join(TEST_MAPS_DIR, f"{map_id}-map.csv"), index_col=0, dtype=str
        )
        demap = pandas.read_csv(
            os.path.join(TEST_MAPS_DIR, f"{map_id}-demap.csv"), index_col=0, dtype=str
        )
        idmap = IDMap()
        idmap.append(demap)
        idmap.maptize(idmap.df.columns.to_list())
        map = map.sort_values(by="id0").reset_index(drop=True)
        demap = idmap.df.sort_values(by="id0").reset_index(drop=True)
        assert map.equals(demap)
