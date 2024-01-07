import numpy as np
import pandas as pd
from category_encoders import OneHotEncoder
from sklearn.preprocessing import StandardScaler


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


def preprocess(
    data: pd.DataFrame,
    fill_na_values: dict,
    one_hot_encoder: OneHotEncoder,
    scaler: StandardScaler,
    variable_types: dict
    ) -> pd.DataFrame:

    data = data.copy()

    # Change negatvie values with NA
    data = create_na(data, [c for c in variable_types["numericals"] if c not in ["velocity_6h", "credit_risk_score"]])

    for column in data.columns:

        if data[column].isna().sum() > 0:
            value_to_impute = fill_na_values[column]

            print(f"WARNING: variable {column} is missing. Using {value_to_impute} as value to impute")

            data[column] = data[column].fillna(value=value_to_impute)


    numericals = data[variable_types["numericals"]]
    categoricals = data[variable_types["categoricals"]]
    binaries = data[variable_types["binary"]]

    transformed_numericals =  pd.DataFrame(scaler.transform(numericals), columns=numericals.columns)
    transformed_categoricals =  one_hot_encoder.transform(categoricals)
    
    # These do not undergo any transformation
    transofmer_binaries = binaries

    return pd.concat([transformed_numericals, transformed_categoricals, transofmer_binaries], axis=1)
