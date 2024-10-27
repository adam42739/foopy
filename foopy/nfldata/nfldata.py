import nfl_data_py
import typing
import pandas
import json
import os


DATA_NAMES = typing.Literal["pbp", "draft", "roster", "player", "schedule"]
DATA_NAMES_VALUES = {"pbp", "draft", "roster", "player", "schedule"}

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
            raise ValueError(f"Path \"{path}\" does not exist.")
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
            mdata = {}
            for year in full_mdata[data_name]:
                mdata[int(year)] = full_mdata[data_name][year]
            return mdata
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


# ========================
# NFL Data Function Getter
# ========================


def _nfl_func(
    data_name: DATA_NAMES,
) -> typing.Callable[[list[int] | None], pandas.DataFrame]:
    """
    Get the `nfl_data_py` function corresponding to `data_name`.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
        `data_name` to get the function for.

    Returns
    -------

    out : ((list[int] | None) -> DataFrame)
    """
    if data_name == "pbp":
        return nfl_data_py.import_pbp_data
    elif data_name == "draft":
        return nfl_data_py.import_draft_picks
    elif data_name == "roster":
        return nfl_data_py.import_weekly_rosters
    elif data_name == "player":
        return nfl_data_py.import_players
    elif data_name == "schedule":
        return nfl_data_py.import_schedules


# ==================
# Load Sub-Functions
# ==================

# The load function calls one of these sub-function depending on the case.


def _load_years(
    data_name: DATA_NAMES,
    nfl_func: typing.Callable[[list[int]], pandas.DataFrame],
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

    nfl_func : ((list[int] | None) -> DataFrame)
        The function associated with `data_name`

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
            df = nfl_func([year])
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
    nfl_func: typing.Callable[[], pandas.DataFrame],
    update: bool,
    mdata: bool,
) -> pandas.DataFrame:
    """
    Load the NFL data for non-years data functions.

    Parameters
    ----------

    data_name : {"pbp", "draft", "roster", "player", "schedule"}
        `data_name` to get the data for.

    nfl_func : ((list[int] | None) -> DataFrame)
        The function associated with `data_name`

    update : bool
        Whether or not the cached NFL data should be updated.

    mdata : bool
        Whether or not cached NFL data exists.
    """
    if mdata and not update:
        df = _load_cached(data_name)
        return df
    else:
        df = nfl_func()
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
    func = _nfl_func(data_name)
    if years:
        return _load_years(data_name, func, years, update, mdata)
    else:
        return _load_non_years(data_name, func, update, mdata)
