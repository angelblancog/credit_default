"""
Module for read / write data operations
"""

from typing import Union
from pathlib import Path

import pandas as pd

from src.const import (
    PRODCESSED_DIR,
)


def read_csv(path: Union[str, Path]) -> pd.DataFrame:
    return pd.read_csv(path)


def read_train() -> tuple[pd.DataFrame, pd.DataFrame]:

    x_path = Path(PRODCESSED_DIR, "x_train_selected.csv")
    y_path = Path(PRODCESSED_DIR, "y_train.csv")

    return read_csv(x_path), read_csv(y_path)


def read_val() -> tuple[pd.DataFrame, pd.DataFrame]:

    x_path = Path(PRODCESSED_DIR, "x_val.csv")
    y_path = Path(PRODCESSED_DIR, "y_val.csv")

    return read_csv(x_path), read_csv(y_path)


def read_test() -> tuple[pd.DataFrame, pd.DataFrame]:

    x_path = Path(PRODCESSED_DIR, "x_test_selected.csv")
    y_path = Path(PRODCESSED_DIR, "y_test.csv")

    return read_csv(x_path), read_csv(y_path)


def write_csv(data: pd.DataFrame, path: Union[str, Path]) -> None:

    # Parse it to `Path` object
    if isinstance(path, str):
        path = Path(path)

    # Create the dir if it does not exist
    if not path.parent.exists():
        path.parent.mkdir(exist_ok=True, parents=True)

    # Always avoid writing the index
    data.to_csv(path, index=False)