"""
Module for creating cols files.
"""

import requests
import pandas
import io
import typing
from . import _create_globals


# ==============================
# NFL Verse Dictionary Functions
# ==============================


URL_BASE = "https://nflreadr.nflverse.com/articles/"

PBP_DICT_URL = URL_BASE + "dictionary_pbp.html"
NGS_DICT_URL = URL_BASE + "dictionary_nextgen_stats.html"
PARTICIPATION_DICT_URL = URL_BASE + "dictionary_participation.html"
SCHEDULES_DICT_URL = URL_BASE + "dictionary_schedules.html"
ROSTERS_DICT_URL = URL_BASE + "dictionary_rosters.html"
PLAYER_STATS_DICT_URL = URL_BASE + "dictionary_player_stats.html"
PLAYERS_DICT_URL = URL_BASE + "dictionary_ff_playerids.html"
DRAFTS_DICT_URL = URL_BASE + "dictionary_draft_picks.html"

ALL_DICT_URLS = [
    PBP_DICT_URL,
    NGS_DICT_URL,
    PARTICIPATION_DICT_URL,
    SCHEDULES_DICT_URL,
    ROSTERS_DICT_URL,
    PLAYER_STATS_DICT_URL,
    PLAYERS_DICT_URL,
    DRAFTS_DICT_URL,
]


def _table_convert_dict(table: list[list[str]]) -> dict[str, str]:
    """
    Convert a table in form `list[list[str]]` to form `dict[str, str]`.
    """
    dict_table = {}
    for i in range(len(table[0])):
        dict_table[table[0][i]] = table[1][i]
    return dict_table


def _get_nflverse_table(url: str) -> dict[str, str]:
    """
    Get the NFLVerse dictionary from the URL.
    """
    text = requests.get(url).text
    ind1 = text.find("[[")
    ind2 = text.find("]]")
    table = None
    if ind1 == -1 or ind2 == -1:
        df = pandas.read_html(io.StringIO(text))[0]
        table = df.T.values.tolist()
    else:
        table = eval(text[ind1 : ind2 + 2])
    if (
        table[1][0] == "character"
        or table[1][0] == "numeric"
        or table[1][0] == "integer"
    ):
        t1 = table[1]
        table[1] = table[2]
        table[2] = t1
    return _table_convert_dict(table)


def _get_all_nflverse_tables() -> list[dict[str, str]]:
    return [_get_nflverse_table(url) for url in ALL_DICT_URLS]


MISSING_DESCRIPTION_DOCSTRING = "No description available."


def _tables_find_column(tables: list[dict[str, str]], column: str) -> str:
    """
    Find the description associated with the column.
    """
    for table in tables:
        if column in table:
            return table[column]
    return MISSING_DESCRIPTION_DOCSTRING


# ================================
# Column Name Formatting Functions
# ================================


def _capitalize(column: str) -> str:
    """
    Capitalize the given column.
    """
    last = ""
    string = ""
    for char in column:
        if last == "" or last == "_":
            string += char.upper()
        elif char != "_":
            string += char
        last = char
    return string


def _format_column_class(column: str) -> str:
    """
    Format the column to a class name.
    """
    column = column.replace("&", "_")
    column = column.replace(" ", "_")
    column = column.replace(".", "_")
    column = column.replace("-", "_")
    return _capitalize(column)


# =========================
# Column File Creator Class
# =========================


COLUMN_PATH_BASE = "foopy/nfldata/cols/"

COLUMN_PLAYER_PATH = COLUMN_PATH_BASE + "player.py"
COLUMN_DRAFT_PATH = COLUMN_PATH_BASE + "draft.py"
COLUMN_PBP_PATH = COLUMN_PATH_BASE + "pbp.py"
COLUMN_SCHEDULE_PATH = COLUMN_PATH_BASE + "schedule.py"
COLUMN_ROSTER_PATH = COLUMN_PATH_BASE + "roster.py"
COLUMN_MAP_PATH = COLUMN_PATH_BASE + "map.py"

COLUMN_PATH_DICT = {
    "pbp": COLUMN_PBP_PATH,
    "draft": COLUMN_DRAFT_PATH,
    "player": COLUMN_PLAYER_PATH,
    "schedule": COLUMN_SCHEDULE_PATH,
    "roster": COLUMN_ROSTER_PATH,
    "map": COLUMN_MAP_PATH,
}

NFL_DATA_COLS = {
    "pbp": _create_globals.PBP_COLS,
    "draft": _create_globals.DRAFT_COLS,
    "roster": _create_globals.ROSTER_COLS,
    "player": _create_globals.PLAYER_COLS,
    "schedule": _create_globals.SCHEDULE_COLS,
    "map": _create_globals.MAP_COLS,
}


class ColumnCreator:
    def __init__(
        self, data_type: typing.Literal["pbp", "player", "draft", "schedule", "roster"]
    ):
        self.col_descs = {column: None for column in NFL_DATA_COLS[data_type]}

    def load_columns(self, tables: list[dict[str, str]]):
        for column in self.col_descs:
            self.col_descs[column] = _tables_find_column(tables, column)

    def write(self, file_path: str):
        with open(file_path, "w") as file:
            file.write(self.__str__())

    def __str__(self) -> str:
        lines = []
        for column in self.col_descs:
            lines.append("class " + _format_column_class(column) + ":")
            lines.append('\t"""')
            lines.append("\t" + self.col_descs[column])
            lines.append('\t"""')
            lines.append("\n")
            lines.append('\theader = "' + column + '"')
            lines.append("\n\n")
        return "\n".join(lines)


def create_cols(col_files: dict[str, set[str]] = NFL_DATA_COLS):
    tables = _get_all_nflverse_tables()
    for data_type in col_files:
        creator = ColumnCreator(data_type)
        creator.load_columns(tables)
        creator.write(COLUMN_PATH_DICT[data_type])
