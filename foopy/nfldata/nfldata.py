import nfl_data_py
import typing
import pandas
import json
import os
from . import cols
import copy


FIRST_SEASON = 2002


DATA_NAMES = typing.Literal["pbp", "draft", "roster", "player", "schedule", "map"]
DATA_NAMES_VALUES = {"pbp", "draft", "roster", "player", "schedule", "map"}
YEARS_DATA_NAMES = {"pbp", "draft", "roster", "schedule"}
NFL_DATA_FUNCS = {
    "pbp": nfl_data_py.import_pbp_data,
    "draft": nfl_data_py.import_draft_picks,
    "roster": nfl_data_py.import_weekly_rosters,
    "player": nfl_data_py.import_players,
    "schedule": nfl_data_py.import_schedules,
    "map": nfl_data_py.import_ids,
}

# =======================
# Configuration Functions
# =======================

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
CONFIG_DATA = {}


def _load_config_data():
    """
    Load the configuration data.
    """
    with open(CONFIG_PATH, "r") as file:
        config_data = json.load(file)
        global CONFIG_DATA
        CONFIG_DATA = copy.deepcopy(config_data)


_load_config_data()


def _dump_config_data():
    """
    Dump the configuration data.
    """
    with open(CONFIG_PATH, "w") as file:
        json.dump(CONFIG_DATA, file)


def set_cache_path(path: str):
    """
    Set the directory for cache to be stored in. Saved in the configuration file.

    Parameters
    ----------

    path : str
        Cache directory
    """
    if isinstance(path, str):
        if os.path.exists(path):
            CONFIG_DATA["cache_dir"] = path
            _dump_config_data()
        else:
            raise ValueError(f'Path "{path}" does not exist.')
    else:
        raise ValueError("Path must be a string.")


# =================
# Caching Functions
# =================


def _load_cached(fname: str) -> pandas.DataFrame:
    path = os.path.join(CONFIG_DATA["cache_dir"], fname + ".parq")
    df = pandas.read_parquet(path)
    return df


def _dump_cached(df: pandas.DataFrame, fname: str):
    path = os.path.join(CONFIG_DATA["cache_dir"], fname + ".parq")
    df.to_parquet(path)


# ==================
# Metadata Functions
# ==================


def _load_metadata(data_name: DATA_NAMES) -> dict[int, bool] | bool:
    """
    Load metadata for the given `data_name` provided.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule", "map"}
        `data_name` to get the function for.

    Returns
    -------

    out : dict
    """
    path = CONFIG_DATA["cache_dir"] + "metadata.json"
    if os.path.exists(path):
        full_mdata = {}
        with open(path, "r") as file:
            full_mdata = json.load(file)
        if data_name in full_mdata:
            if data_name in YEARS_DATA_NAMES:
                mdata = {}
                for year in full_mdata[data_name]:
                    mdata[int(year)] = full_mdata[data_name][year]
                return mdata
            else:
                return full_mdata[data_name]
        else:
            return {}
    else:
        return {}


def _dump_metadata(data_name: DATA_NAMES, mdata: dict[int, bool] | bool):
    """
    Dump the metadata to the given `data_name` provided.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule", "map"}
        `data_name` to get the function for.

    mdata : dict[int, bool] | bool
        The metadata to dump.
    """
    path = os.path.join(CONFIG_DATA["cache_dir"], "metadata.json")
    full_mdata = {}
    if os.path.exists(path):
        with open(path, "r") as file:
            full_mdata = json.load(file)
    full_mdata[data_name] = mdata
    with open(path, "w") as file:
        json.dump(full_mdata, file)


# ==================
# Load Sub-Functions
# ==================

# The load function calls one of these sub-function depending on the case.


def _load_years(
    data_name: DATA_NAMES,
    years: list[int],
    update: bool,
    mdata: dict[int],
) -> pandas.DataFrame:
    """
    Load the NFL data for years data functions.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule", "map"}
        `data_name` to get the data for.

    years : list[int]
        Years to get the data for.

    update : bool
        Whether or not the cached NFL data should be updated.

    mdata : bool
        Whether or not cached NFL data exists.
    """
    dfs = []
    for year in years:
        if year not in mdata or (year == max(mdata) and update):
            df = NFL_DATA_FUNCS[data_name]([year])
            _dump_cached(df, data_name + "-" + str(year))
            mdata[year] = True
            dfs.append(df)
        else:
            df = _load_cached(data_name + "-" + str(year))
            dfs.append(df)
        _dump_metadata(data_name, mdata)
    df = pandas.concat(dfs)
    return df


def _load_non_years(
    data_name: DATA_NAMES,
    update: bool,
    mdata: bool,
) -> pandas.DataFrame:
    """
    Load the NFL data for non-years data functions.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule", "map"}
        `data_name` to get the data for.

    update : bool
        Whether or not the cached NFL data should be updated.

    mdata : bool
        Whether or not cached NFL data exists.
    """
    if mdata and not update:
        df = _load_cached(data_name)
        return df
    else:
        df = NFL_DATA_FUNCS[data_name]()
        _dump_cached(df, data_name)
        _dump_metadata(data_name, True)
        return df


# =================================
# Load Function Argument Validation
# =================================

# Validate the arugments passed to load(); raise ValueError if invalid.


def _load_validate_data_name(data_name: DATA_NAMES):
    if data_name not in DATA_NAMES_VALUES:
        raise ValueError("data_name argument passed to load() invalid.")


def _load_validate_years(years: list[int] | None):
    if isinstance(years, list):
        for year in years:
            if not isinstance(year, int):
                raise ValueError("years argument passed to load() invalid.")
    elif years != None:
        raise ValueError("years argument passed to load() invalid.")


def _load_validate_update(update: bool):
    if not isinstance(update, bool):
        raise ValueError("update arguments passed to load() invalid.")


# ==========================
# Team Abbreviation Unifying
# ==========================

TEAM_ABBRS = {}
TEAM_ABBRS_PATH = os.path.join(os.path.dirname(__file__), "abbrs.json")


def _load_team_abbrs():
    """
    Load the team abbreviations dictionary to the global `TEAM_ABBRS` constant.
    """
    with open(TEAM_ABBRS_PATH, "r") as file:
        abbrs = json.load(file)
        global TEAM_ABBRS
        TEAM_ABBRS = copy.deepcopy(abbrs)


_load_team_abbrs()


def _get_team_abbr(abbr: str) -> str:
    if abbr in TEAM_ABBRS:
        return TEAM_ABBRS[abbr]
    else:
        return None


# =================
# Draft ID Creation
# =================


DRAFT_IDS_DATA_NAMES = typing.Literal["draft", "player", "roster"]
DRAFT_IDS_DATA_NAMES_VALUES = {"draft", "player", "roster"}


def _create_draft_id(
    data_name: DRAFT_IDS_DATA_NAMES, df: pandas.DataFrame
) -> pandas.DataFrame:
    """
    Create the draft ID. Not gauranteed to be unique or match (player names may be displayed differently depending on source).

    `[Team abbreviation][Overall draft number][Player name (no spaces, periods, hyphens, etc.)]`

    Example:

    * `CAR1BryceYoung`
    * `HOU2CJStroud`
    """
    team = None
    overall = None
    name = None
    if data_name == "draft":
        team = df[cols.draft.Team.header]
        round = df[cols.draft.Round.header].fillna(0)
        pick = df[cols.draft.Pick.header].fillna(0)
        overall = pick * round
        name = df[cols.draft.PfrPlayerName.header]
    elif data_name == "player":
        team = df[cols.player.DraftClub.header]
        overall = df[cols.player.DraftNumber.header].fillna(0)
        name = df[cols.player.DisplayName.header]
    elif data_name == "roster":
        team = df[cols.roster.DraftClub.header]
        overall = df[cols.roster.DraftNumber.header].fillna(0)
        name = df[cols.roster.PlayerName.header]
    team = team.apply(_get_team_abbr)
    overall = overall.astype(int).astype(str).replace("0", None)
    name = (
        name.str.replace(" ", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace("-", "", regex=False)
        .str.replace("'", "", regex=False)
    )
    df[cols.draft.DraftId.header] = (team.notna() & overall.notna() & name.notna()) * (
        team + overall + name
    )
    return df


# ==================
# ID Column Cleaning
# ==================

DRAFT_ID_COLUMNS = [
    "gsis_id",
    "pfr_player_id",
    "cfb_player_id",
    "draft_id",
]
ROSTER_ID_COLUMNS = [
    "player_id",
    "espn_id",
    "sportradar_id",
    "yahoo_id",
    "rotowire_id",
    "pff_id",
    "pfr_id",
    "fantasy_data_id",
    "sleeper_id",
    "esb_id",
    "gsis_it_id",
    "smart_id",
    "draft_id",
]
PLAYER_ID_COLUMNS = [
    "esb_id",
    "gsis_id",
    "current_team_id",
    "gsis_it_id",
    "smart_id",
    "draft_id",
]
SCHEDULE_ID_COLUMNS = [
    "game_id",
    "old_game_id",
    "nfl_detail_id",
    "away_qb_id",
    "home_qb_id",
    "stadium_id",
]
PBP_ID_COLUMNS = [
    "play_id",
    "game_id",
    "old_game_id_x",
    "td_player_id",
    "passer_player_id",
    "receiver_player_id",
    "rusher_player_id",
    "lateral_receiver_player_id",
    "lateral_rusher_player_id",
    "lateral_sack_player_id",
    "interception_player_id",
    "lateral_interception_player_id",
    "punt_returner_player_id",
    "lateral_punt_returner_player_id",
    "kickoff_returner_player_id",
    "lateral_kickoff_returner_player_id",
    "punter_player_id",
    "kicker_player_id",
    "own_kickoff_recovery_player_id",
    "blocked_player_id",
    "tackle_for_loss_1_player_id",
    "tackle_for_loss_2_player_id",
    "qb_hit_1_player_id",
    "qb_hit_2_player_id",
    "forced_fumble_player_1_player_id",
    "forced_fumble_player_2_player_id",
    "solo_tackle_1_player_id",
    "solo_tackle_2_player_id",
    "assist_tackle_1_player_id",
    "assist_tackle_2_player_id",
    "assist_tackle_3_player_id",
    "assist_tackle_4_player_id",
    "tackle_with_assist_1_player_id",
    "tackle_with_assist_2_player_id",
    "pass_defense_1_player_id",
    "pass_defense_2_player_id",
    "fumbled_1_player_id",
    "fumbled_2_player_id",
    "fumble_recovery_1_player_id",
    "fumble_recovery_2_player_id",
    "sack_player_id",
    "half_sack_1_player_id",
    "half_sack_2_player_id",
    "penalty_player_id",
    "safety_player_id",
    "nfl_api_id",
    "drive_play_id_started",
    "drive_play_id_ended",
    "stadium_id",
    "passer_id",
    "rusher_id",
    "receiver_id",
    "id",
    "fantasy_player_id",
    "fantasy_id",
    "nflverse_game_id",
    "old_game_id_y",
]
MAP_ID_COLUMNS = [
    "rotoworld_id",
    "cfbref_id",
    "ktc_id",
    "nfl_id",
    "gsis_id",
    "rotowire_id",
    "pfr_id",
    "pff_id",
    "yahoo_id",
    "fantasypros_id",
    "swish_id",
    "mfl_id",
    "sportradar_id",
    "sleeper_id",
    "fantasy_data_id",
    "espn_id",
    "stats_id",
    "cbs_id",
    "stats_global_id",
    "fleaflicker_id",
]

ID_COLUMNS = {
    "pbp": PBP_ID_COLUMNS,
    "draft": DRAFT_ID_COLUMNS,
    "roster": ROSTER_ID_COLUMNS,
    "schedule": SCHEDULE_ID_COLUMNS,
    "player": PLAYER_ID_COLUMNS,
    "map": MAP_ID_COLUMNS,
}


def _string_all_IDs(data_name: DATA_NAMES, df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Ensure all ID related columns are dtype string.
    """
    for column in ID_COLUMNS[data_name]:
        notna = df[column].notna()
        df.loc[notna, column] = df.loc[notna, column].astype(str)
    return df


# =============
# Load Function
# =============

# Core function for the nfldata.py module.


def load(
    data_name: DATA_NAMES, years: list[int] | None = None, update: bool = False
) -> pandas.DataFrame:
    """
    Load NFL data from `nfl_data_py` or cache if it exists

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule", "map"}
        `data_name` of the dataset to get.

    years : list[int] | None = None
        List of integers for the years to get the data for. `None` if the `nfl_data_py` function does not take years as a parameter.

        Required for:

        * `pbp`
        * `draft`
        * `roster`
        * `schedule`

    update : bool = False
        Whether or not to update the data in the cache.

    Returns
    -------

    out : pandas.DataFrame

    """
    _load_validate_data_name(data_name)
    _load_validate_years(years)
    _load_validate_update(update)
    mdata = _load_metadata(data_name)
    df = pandas.DataFrame()
    if years:
        df = _load_years(data_name, years, update, mdata)
    else:
        df = _load_non_years(data_name, update, mdata)
    if data_name in DRAFT_IDS_DATA_NAMES_VALUES:
        df = _create_draft_id(data_name, df)
    df = _string_all_IDs(data_name, df)
    return df
