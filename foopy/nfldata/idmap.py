import pandas
import os


class IDMap:
    """
    Class for keeping track of IDs
    """

    def __init__(self):
        self.df = pandas.DataFrame()

    # ============
    # IO Functions
    # ============

    def load(self, path: str):
        """
        Load the `IDMap` from the given file path.
        """
        if isinstance(path, str):
            if os.path.exists(path):
                self.df = pandas.read_csv(path)
            else:
                raise ValueError(f'Path "{path}" does not exist.')
        else:
            raise ValueError("Path must be a string")

    def dump(self, path: str):
        """
        Dump the `IDMap` to the given file path.
        """
        if isinstance(path, str):
            if os.path.exists(path):
                self.df.to_csv(path)
            else:
                raise ValueError(f'Path "{path}" does not exist.')
        else:
            raise ValueError("Path must be a string")

    # ===========================
    # Data Manipulation Functions
    # ===========================

    def append(self, new_maps: pandas.DataFrame):
        """
        Append a `DataFrame` of new maps to the `IDMap`.

        Parameters
        ----------

        new_maps : DataFrame
            New maps to append.
        """
        self.df = pandas.concat([self.df, new_maps])

    def maptize(self):
        pass

    # =============
    # Magic Methods
    # =============

    def __str__(self) -> str:
        return self.df.head().to_string()
