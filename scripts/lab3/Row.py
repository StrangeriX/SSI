from typing import List, Tuple

class Row():
    __values: List[float]

    def __init__(self, values: List[float]):
        self.__values = values

    def get_value(self,index: int):
        return self.__values[index]

    def __str__(self):
        return f'{self.__values[0]}, {self.__values[1]}'