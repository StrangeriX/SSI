import math
import numpy as np
import random
from typing import Tuple


class Sample:
    x1: float
    x2: float
    value: float

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.value = self.calculate_value(x1, x2)
        self.correct_jump = 5

    @staticmethod
    def calculate_value(x1: float, x2: float):
        return math.sin(x1 * 0.05) + math.sin(x2 * 0.05) + 0.4 * math.sin(x1 * 0.15) * math.sin(x2 * 0.15)

    def get_value(self):
        return self.value

    def __str__(self):
        return f"(x1, x2) = ({self.x1}, {self.x2}), value = {self.value}\n"

    def mutate(self, mutation_level, scope_range):
        mutation = np.linspace(-mutation_level, mutation_level, 100)
        self.x1 += random.choice(mutation)
        if self.x1 > scope_range[1]:
            self.x1 -= self.correct_jump
        elif self.x1 < scope_range[0]:
            self.x1 += self.correct_jump
        self.x2 += random.choice(mutation)
        if self.x2 > scope_range[1]:
            self.x2 -= self.correct_jump
        elif self.x2 < scope_range[0]:
            self.x2 += self.correct_jump
        self.value = self.calculate_value(self.x1, self.x2)
