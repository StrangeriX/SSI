from typing import Tuple, List
import numpy as np


class Bitmap:
    matrix = []

    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.matrix = np.zeros(shape=self.size, dtype=int)

    def get_matrix(self):
        return self.matrix

    def set_matrix(self, values: List[List[int]]):
        for i in range(len(values)):
            self.matrix[i] = values[i]

    def get_value(self, row: int, index: int):
        return self.matrix[row][index]

    def get_size(self):
        return self.matrix.shape
