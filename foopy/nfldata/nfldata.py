import nfl_data_py
import typing
import pandas
import json
import os
from . import cols


DATA_NAMES = typing.Literal["pbp", "draft", "roster", "player", "schedule"]
DATA_NAMES_VALUES = {"pbp", "draft", "roster", "player", "schedule"}
YEARS_DATA_NAMES = {"pbp", "draft", "roster", "schedule"}
NFL_DATA_FUNCS = {
    "pbp": nfl_data_py.import_pbp_data,
    "draft": nfl_data_py.import_draft_picks,
    "roster": nfl_data_py.import_weekly_rosters,
    "player": nfl_data_py.import_players,
    "schedule": nfl_data_py.import_schedules,
}

# =======================
# Configuration Functions
# =======================

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")


def _load_config_data() -> dict[str, str]:
    """
    Load the configuration data.
    """
    config_data = {}
    with open(CONFIG_PATH, "r") as file:
        config_data = json.load(file)
    return config_data


def _dump_config_data(config_data: dict[str, str]):
    """
    Dump the configuration data.
    """
    with open(CONFIG_PATH, "w") as file:
        json.dump(config_data, file)


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
            config_data = _load_config_data()
            config_data["cache_dir"] = path
            _dump_config_data(config_data)
        else:
            raise ValueError(f'Path "{path}" does not exist.')
    else:
        raise ValueError("Path must be a string.")


def _load_cache_path() -> str:
    """
    Load the cache path.
    """
    config_data = _load_config_data()
    return config_data["cache_dir"]


# =================
# Caching Functions
# =================


def _load_cached(fname: str) -> pandas.DataFrame:
    path = os.path.join(_load_cache_path(), fname + ".parq")
    df = pandas.read_parquet(path)
    return df


def _dump_cached(df: pandas.DataFrame, fname: str):
    path = os.path.join(_load_cache_path(), fname + ".parq")
    df.to_parquet(path)


# ==================
# Metadata Functions
# ==================


def _load_metadata(data_name: DATA_NAMES) -> dict[int, bool] | bool:
    """
    Load metadata for the given `data_name` provided.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
        `data_name` to get the function for.

    Returns
    -------

    out : dict
    """
    path = _load_cache_path() + "metadata.json"
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

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
        `data_name` to get the function for.

    mdata : dict[int, bool] | bool
        The metadata to dump.
    """
    path = os.path.join(_load_cache_path(), "metadata.json")
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

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
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

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
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
        for abbr in abbrs:
            TEAM_ABBRS[abbr] = abbrs[abbr]


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
        name.str.replace(" ", "")
        .str.replace(".", "")
        .str.replace("-", "")
        .str.replace("'", "")
    )
    df[cols.draft.DraftId.header] = (team.notna() & overall.notna() & name.notna()) * (
        team + overall + name
    )
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

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
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
    return df
