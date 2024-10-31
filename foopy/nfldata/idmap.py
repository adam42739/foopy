import pandas
import os
import tqdm


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
                self.df = pandas.read_csv(path, dtype=str)
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

    def _get_column_dupes_df(self, column: str) -> pandas.DataFrame:
        """
        Get the DataFrame containing all rows with values for `column` that are duplicated.
        """
        series = self.df[column]
        all_dupes = series.duplicated(keep=False) & series.notna()
        return self.df[all_dupes]

    def _get_id_value_df(
        self, dupes_df: pandas.DataFrame, column: str, id_value: str
    ) -> pandas.DataFrame:
        """
        Get the DataFrame with all rows where `column == id_value`. Returns an empty DataFrame if all IDs are not matching.
        """
        id_value_df = dupes_df[dupes_df[column] == id_value]
        if all((id_value_df.nunique() == 1) | (id_value_df.nunique() == 0)):
            return id_value_df
        else:
            return pandas.DataFrame()

    def _maptize_by_column(self, column: str):
        """
        Maptize a single column given by `column`.
        """
        dupes_df = self._get_column_dupes_df(column)
        for id_value in dupes_df[column].unique():
            id_value_df = self._get_id_value_df(dupes_df, column, id_value)
            if not id_value_df.empty:
                new_series = pandas.Series(
                    {column: None for column in id_value_df.columns}
                )
                for _, series in id_value_df.iterrows():
                    new_series = new_series.combine_first(series)
                for index in id_value_df.index:
                    self.df.loc[index] = new_series
        self.df = self.df.drop_duplicates()

    def maptize(self, map_columns: list[str]):
        """
        Maptize the `IDMap`.
        """
        for column in tqdm.tqdm(map_columns, desc="Maptizing"):
            self._maptize_by_column(column)

    # =============
    # Magic Methods
    # =============

    def __str__(self) -> str:
        return self.df.head().to_string()
