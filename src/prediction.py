# Functions
from src.data_processing import preprocess

# Processing
import pandas as pd
import numpy as np

# Encoding and scaling
from category_encoders import OneHotEncoder
from sklearn.preprocessing import StandardScaler


def predict(
    data: pd.DataFrame,
    model,
    fill_na_values: dict,
    one_hot_encoder: OneHotEncoder,
    scaler: StandardScaler,
    variable_types: dict
) -> np.ndarray:
    """Function to predict the probability of fraud on new customers

    Args:
        data (pd.DataFrame): dataset to predict
        model (_type_): model used to make the predictions
        fill_na_values (dict): proccess to deal with NA values
        one_hot_encoder (OneHotEncoder): type of encoder
        scaler (StandardScaler): type of scaler
        variable_types (dict): type of variables

    Returns:
        np.ndarray: array with the probabilities of fraud
    """    

    # Joint of all the preprocessing steps
    transformed = preprocess(
        data=data,
        fill_na_values=fill_na_values,
        one_hot_encoder=one_hot_encoder,
        scaler=scaler,
        variable_types=variable_types
    )

    # Only use the variables known by the model
    transformed = transformed[model.feature_names_in_]

    # Make the predictions
    return model.predict(transformed)
