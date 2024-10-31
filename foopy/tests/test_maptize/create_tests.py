from ...nfldata.idmap import IDMap
import random
import pandas
import os
import tqdm


def _create_map(N_id: int, N_row: int) -> pandas.DataFrame:
    """
    Create an ID map with `N_id` columns and `N_row` rows
    """
    map = pandas.DataFrame(
        {"id" + str(id_num): [str(i) for i in range(N_row)] for id_num in range(N_id)}
    )
    return map


def _demaptize(map: pandas.DataFrame) -> pandas.DataFrame:
    """
    Demaptize the given `map`.
    """
    for index, series in tqdm.tqdm(map.iterrows(), total=len(map), desc="Demaptizing"):
        for iteration in range(random.randrange(0, 5)):
            if iteration == 1 or 2:
                split_index = random.randrange(0, len(map.columns) - 1)
                left_series = series[["id" + str(i) for i in range(0, split_index + 1)]]
                right_series = series[
                    ["id" + str(i) for i in range(split_index, len(map.columns))]
                ]
                map.loc[index] = left_series
                map.loc[len(map)] = right_series
            elif iteration == 3 or 4:
                map.loc[len(map)] = map.loc[index].copy()
    return map


TEST_MAPS_DIR = os.path.join(os.path.dirname(__file__), "test_maps/")


def create_maptize_test(N_id: int, N_row: int, map_id: str):
    """
    Create a map and demap for a map of `N_id` columns and `N_row` rows. Store the two maps in the testing directory with filename `map_id`.
    """
    map = _create_map(N_id, N_row)
    map.to_csv(os.path.join(TEST_MAPS_DIR, f"{map_id}-map.csv"))
    demap = _demaptize(map)
    demap.to_csv(os.path.join(TEST_MAPS_DIR, f"{map_id}-demap.csv"))
