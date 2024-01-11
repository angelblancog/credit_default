# Purpose: Define types for the project to improve type annotations and readability

# Import the TypedDict class
from typing import TypedDict, Union

# Definition of the types
class VariableTypes(TypedDict):
    numericals: list[str]
    categoricals: list[str]
    binary: list[str]
    target: str

# 
FillNAValues = dict[str, Union[int, float, str]]

class ModelVariables(TypedDict):
    transformed: list[str]
    raw: list[str]
    all: list[str]

class DefaultValues(TypedDict):
    numericals: list[str]
    categoricals: list[str]
    binary: list[str]