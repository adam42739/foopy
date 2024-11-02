"""
========
NFL Data
========

Functions

* `set_cache_path()`

    Set the directory where cache will be stored.

* `load()`

    Load NFL data.

* class: `PlayerMap`

    Player ID mapping class.
"""

from .nfldata import set_cache_path, load
from .playermap import PlayerMap
