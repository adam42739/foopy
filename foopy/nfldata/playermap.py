from .idmap import IDMap
from .nfldata import CONFIG_DATA, FIRST_SEASON, DATA_NAMES, ID_COLUMNS, load
import os
import pandas
import json
from ..nflweek import CURRENT_SEASON


# ===================
# ID Alias Correcting
# ===================


ID_ALIAS = {
    "roster": {"player_id": "gsis_id"},
    "draft": {"pfr_player_id": "pfr_id", "cfb_player_id": "cfbref_id"},
}


def _correct_id_alias(data_name: DATA_NAMES, df: pandas.DataFrame) -> pandas.DataFrame:
    if data_name in ID_ALIAS:
        df = df.rename(ID_ALIAS[data_name], axis="columns")
    return df


# ================
# Player Map Class
# ================


class PlayerMap(IDMap):
    def __init__(self):
        self.metadata = {"draft": {}, "roster": {}}
        super().__init__()

    def load(self):
        """
        Load the `PlayerMap`.
        """
        path = os.path.join(CONFIG_DATA["cache_dir"], "playermap-metadata.csv")
        if os.path.exists(path):
            with open(path, "r") as file:
                self.metadata = json.load(file)
            super().load(CONFIG_DATA["cache_dir"], "playermap")
        else:
            self.df = pandas.DataFrame()
            self.append_df = pandas.DataFrame()
            self.metadata = {"draft": {}, "roster": {}}

    def dump(self):
        """
        Dump the `PlayerMap`.
        """
        path = os.path.join(CONFIG_DATA["cache_dir"], "playermap-metadata.csv")
        with open(path, "w") as file:
            json.dump(self.metadata, file)
        super().dump(CONFIG_DATA["cache_dir"], "playermap")

    def _update_years(self, data_name: DATA_NAMES, part: int, total: int):
        """
        Update the map with data from years functions.
        """
        years = []
        for year in range(FIRST_SEASON, CURRENT_SEASON + 1):
            if year not in self.metadata[data_name] or year == CURRENT_SEASON:
                self.metadata[data_name][year] = True
                years.append(year)
        df = load(data_name, years, True)[ID_COLUMNS[data_name]]
        df = _correct_id_alias(data_name, df)
        self.append(df, part, total)

    def _update_non_year(self, data_name: DATA_NAMES, part: int, total: int):
        """
        Update the map with data from non-years functions.
        """
        df = load(data_name, update=True)[ID_COLUMNS[data_name]]
        df = _correct_id_alias(data_name, df)
        self.append(df, part, total)

    def update(self):
        """
        Update the `PlayerMap` with the most current data.
        """
        self._update_years("draft", 1, 4)
        self._update_years("roster", 2, 4)
        self._update_non_year("player", 3, 4)
        self._update_non_year("map", 4, 4)
        self.maptize()

    def maptize(self):
        MAP_COLUMNS = ["esb_id", "gsis_id", "cfbref_id", "pfr_id", "draft_id"]
        super().maptize(MAP_COLUMNS)
