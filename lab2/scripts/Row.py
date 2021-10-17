from typing import List


class Row:
    values: List[float]
    types: List[bool]
    attributes: List[str]

    def __init__(self, class_name: str, types: List[bool], values: List[float], attributes: List[str]):
        self.values = values
        self.types = types
        self.class_name = class_name
        self.attributes = attributes

    def set_value(self, value: float):
        self.values.append(value)

    def get_value(self, index: int):
        return self.values[index]

    def __str__(self):
        return f"Data: type = {str(self.types)}, value = {str(self.values)}, class = {self.class_name}"
