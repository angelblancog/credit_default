import numpy as np
import pandas as pd


def impute_na(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Replace negative values with the median

    Args:
        data (pd.DataFrame): dataset to impute
        columns (list[str]): list of desired columns

    Returns:
        pd.DataFrame: the modifed data
    """

    data = data.copy()  # keep the outter dataframe intact

    if isinstance(columns, str):
        columns = [columns]

    for column in columns:

        # 1. Calculate the median (positive values)
        median = data.query(f"{column} > 0")[column].median()
        
        # 2. Replace the < 0 with that value
        data.loc[data.loc[:,column] < 0, column] = median

    return data


def create_na(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Replace negative values with the median

    Args:
        data (pd.DataFrame): dataset to impute
        columns (list[str]): list of desired columns

    Returns:
        pd.DataFrame: the modifed data
    """

    data = data.copy()  # keep the outter dataframe intact

    if isinstance(columns, str):
        columns = [columns]

    for column in columns:
        
        # Replace the < 0 with NA value
        data.loc[data.loc[:,column] < 0, column] = np.nan

    return data