# Purpose: constants for the project to improve readability and maintainability

# Libraries
import json
from pathlib import Path

# Import of types
from src.types import (
    VariableTypes,
    FillNAValues,
    ModelVariables
)

# Common paths for the project to improve readability
DATA_DIR = Path("data")
METADATA_DIR = Path("metadata")
PRODCESSED_DIR = Path(DATA_DIR, "processed")
MODELS_DIR = Path("models")

# Metadata
variable_types: VariableTypes = json.loads( Path(METADATA_DIR, "variables_types.json").resolve().read_text() )
fill_na_values: FillNAValues = json.loads( Path(METADATA_DIR, "fill_na_values.json").resolve().read_text() )
model_variables: ModelVariables = json.loads( Path(METADATA_DIR, "model_variables.json").resolve().read_text() )