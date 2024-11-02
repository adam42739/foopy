import pandas
import os
import tqdm


class IDMap:
    """
    Class for keeping track of IDs
    """

    def __init__(self):
        self.df = pandas.DataFrame()
        self.append_df = pandas.DataFrame()

    # ============
    # IO Functions
    # ============

    def load(self, dir_path: str, fname: str):
        """
        Load the `IDMap` from the given file path.
        """
        if isinstance(dir_path, str) and isinstance(fname, str):
            df_path = os.path.join(dir_path, fname + "-df.parq")
            append_path = os.path.join(dir_path, fname + "-append.parq")
            if os.path.exists(df_path) and os.path.exists(append_path):
                self.df = pandas.read_parquet(df_path)
                self.append_df = pandas.read_parquet(append_path)
            else:
                raise ValueError(f'Path "{df_path}" does not exist.')
        else:
            raise ValueError("Path must be a string")

    def dump(self, dir_path: str, fname: str):
        """
        Dump the `IDMap` to the given file path.
        """
        if isinstance(dir_path, str) and isinstance(fname, str):
            df_path = os.path.join(dir_path, fname + "-df.parq")
            append_path = os.path.join(dir_path, fname + "-append.parq")
            self.df.to_parquet(df_path)
            self.append_df.to_parquet(append_path)
        else:
            raise ValueError("Path must be a string")

    # ===========================
    # Data Manipulation Functions
    # ===========================

    def append(self, new_maps: pandas.DataFrame, part: int, total: int):
        """
        Append a `DataFrame` of new maps to the `IDMap`.

        Parameters
        ----------

        new_maps : DataFrame
            New maps to append.
        """
        pbar = tqdm.tqdm(total=7, desc=f"Appending {part} / {total}")
        self.append_df = pandas.concat([self.append_df, new_maps])
        pbar.update()
        dupes_mask = self.append_df.duplicated(keep=False)
        pbar.update()
        dupes = self.append_df[dupes_mask]
        pbar.update()
        dupes = dupes.drop_duplicates()
        pbar.update()
        self.append_df = self.append_df.drop_duplicates().reset_index(drop=True)
        pbar.update()
        new_maps = pandas.concat([new_maps, dupes]).drop_duplicates(keep=False)
        pbar.update()
        self.df = pandas.concat([self.df, new_maps]).reset_index(drop=True)
        pbar.update()
        pbar.close()

    # =================
    # Maptize Functions
    # =================

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

    def _maptize_by_column(self, column: str, number: int, total: int):
        """
        Maptize a single column given by `column`.
        """
        dupes_df = self._get_column_dupes_df(column)
        for id_value in tqdm.tqdm(
            dupes_df[column].unique(), desc=f"Maptizing {number} / {total}"
        ):
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
        count = 1
        for column in map_columns:
            self._maptize_by_column(column, count, len(map_columns))
            count += 1

    # =============
    # Magic Methods
    # =============

    def __str__(self) -> str:
        return self.df.head().to_string()
