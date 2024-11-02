import json
import os
import datetime


# ==============
# Current Season
# ==============


def _current_season() -> int:
    today = datetime.datetime.today()
    if today.month <= 2 and today.date <= 20:
        return today.year - 1
    else:
        return today.year


CURRENT_SEASON = _current_season()


# =======================
# Global Years Dictionary
# =======================

# Length in weeks for regular and post season for each year.


YEARS = {}


def _load_years():
    """
    Load the `YEARS` global variable from `years.json`.
    """
    years = {}
    path = os.path.join(os.path.dirname(__file__), "years.json")
    with open(path, "r") as file:
        years = json.load(file)
    for key in years:
        YEARS[int(key)] = {
            "reg": int(years[key]["reg"]),
            "post": int(years[key]["post"]),
            "total": int(years[key]["reg"]) + int(years[key]["post"]),
        }


# Call _load_years() when the module is loaded.


_load_years()
MAX_YEAR = max(YEARS.keys())
MIN_YEAR = min(YEARS.keys())


def _years_get(year: int) -> dict[str, int]:
    """
    Get the dictionary from `YEARS` corresponding to the given `year`.
    """
    if year < MIN_YEAR:
        return YEARS[MIN_YEAR]
    elif year > MAX_YEAR:
        return YEARS[MAX_YEAR]
    else:
        return YEARS[year]


class NFLWeek:
    """
    =======
    NFLWeek
    =======

    Simple class for keeping track of NFL weeks.
    """

    # ========================
    # Initialization Functions
    # ========================

    def __init__(self, year: int, week: int):
        """
        Parameters
        ----------

        year : int
            Will be forced to >= 1970, the first year supported by `NFLWeek`.

        week : int
            Will be forced to >= 1 or <= (17, 19, 20, 21, 22) depending on `year`.
        """
        if not isinstance(year, int):
            raise ValueError("Argument passes for year invalid.")
        if not isinstance(week, int):
            raise ValueError("Argument passed for week invalid.")
        self.year = year
        self.week = week
        self._force_valid()

    def _force_valid(self):
        """
        Force the week to be valid by ensuring `year` >= 1970 and week between 1 and (17, 19, 20, 21, 22).
        """
        if self.year < 1970:
            self.year = 1970
        if self.week < 1:
            self.week = 1
        elif self.week > _years_get(self.year)["total"]:
            self.week = _years_get(self.year)["total"]

    # ============================
    # Class Manipulation Functions
    # ============================

    def _advance_single(self):
        """
        Advance the week by one week.
        """
        if self.week < _years_get(self.year)["total"]:
            self.week += 1
        else:
            self.year += 1
            self.week = 1

    def advance(self, weeks: int = 1):
        """
        Advance the week by the amount given. Will rollover the season if necessary

        Parameters
        ----------

        weeks : int = 1
            Number of weeks to advance.
        """
        for _ in range(weeks):
            self._advance_single()

    def _backward_single(self):
        """
        Go back by one week.
        """
        if self.week > 1:
            self.week -= 1
        elif self.year == 1970:
            pass
        else:
            self.year -= 1
            self.week = _years_get(self.year)["total"]

    def backward(self, weeks: int = 1):
        """
        Go back by the amount of weeks given. Will rollover the season if necessary

        Parameters
        ----------

        weeks : int = 1
            Number of weeks to go back.
        """
        for _ in range(weeks):
            self._backward_single()

    # =============
    # Magic Methods
    # =============

    def __str__(self) -> str:
        return f"NFLWeek(year = {self.year}, week = {self.week})"
