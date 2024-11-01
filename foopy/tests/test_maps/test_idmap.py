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


append1 = pandas.DataFrame({"A": [1, 2, 3], "B": [1, 2, 3]})
append2 = pandas.DataFrame(
    {"A": [1, 2, 4, 5], "B": [1, 2, 4, 5], "C": [None, None, 4, 5]}
)
map_value = pandas.DataFrame(
    {"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [None, None, None, 4, 5]}
)
append_value = pandas.DataFrame(
    {"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [None, None, None, 4, 5]}
)


def test_append():
    map = IDMap()
    map.append(append1)
    map.append(append2)
    assert map.df.equals(map_value)
    assert map.append_df.equals(append_value)
