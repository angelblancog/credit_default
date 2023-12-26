import json
from pathlib import Path

from src.types import VariableTypes


# Paths comunes: data, models, etc
DATA_DIR = Path("data")
METADATA_DIR = Path("metadata")
PRODCESSED_DIR = Path(DATA_DIR, "processed")
MODELS_DIR = Path("models")

# Diccionario con metadata
variable_types: VariableTypes = json.loads( Path(METADATA_DIR, "variables_types.json").resolve().read_text() )
