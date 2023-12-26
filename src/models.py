"""
Module for read / write models operation
"""

from typing import Any
from pathlib import Path

import pickle

from src.const import (
    MODELS_DIR
)


def add_file_extension(name: str, extension: str = ".pkl") -> str:

    # So the extension is not forgotten    
    if not name.endswith(extension):
        name = f"{name}{extension}"

    return name


def write_model(model: Any, name: str, path: Path = MODELS_DIR) -> None:

    name = add_file_extension(name)
    file = Path(path, name)

    # Create the dir if not exit
    if not file.parent.exists():
        file.parent.mkdir(exist_ok=True, parents=True)

    # wb: write binary
    pickle.dump(model,  file.open("wb"))


def read_model(name: str, path: Path = MODELS_DIR) -> Any:

    name = add_file_extension(name)
    file = Path(path, name)

    # rb: read binary
    return pickle.loads( file.read_bytes() )


def read_all_models(path: Path = MODELS_DIR, extension: str = ".pkl") -> dict[str, Any]:

    # Load all files that end in .pkl
    return {
        file.name.removesuffix(extension): read_model( file.name )
            for file in path.glob(f"*{extension}")
    }
