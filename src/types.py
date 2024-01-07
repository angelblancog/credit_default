from typing import TypedDict, Union


class VariableTypes(TypedDict):
    numericals: list[str]
    categoricals: list[str]
    binary: list[str]
    target: str


FillNAValues = dict[str, Union[int, float, str]]

class ModelVariables(TypedDict):
    transformed: list[str]
    raw: list[str]
    all: list[str]
