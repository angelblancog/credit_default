from typing import TypedDict


class VariableTypes(TypedDict):
    numericals: list[str]
    categoricals: list[str]
    binary: list[str]
    target: str