from src.data_processing import preprocess
import pandas as pd
import numpy as np
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
    

    transformed = preprocess(
        data=data,
        fill_na_values=fill_na_values,
        one_hot_encoder=one_hot_encoder,
        scaler=scaler,
        variable_types=variable_types
    )

    # only use the variables known by the model
    transformed = transformed[model.feature_names_in_]

    return model.predict(transformed)
