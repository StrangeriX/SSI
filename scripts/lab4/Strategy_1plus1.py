import random
import math
import numpy as np
from typing import Tuple
from scripts.Chart import Chart


class OnePlusOneStrategy:

    def __init__(self, dispersion: float, increment_factor: float, scope_range: Tuple[float, float], n: int):
        self.dispersion = np.linspace(-dispersion, dispersion, 100)
        self.increment_factor = increment_factor
        self.n = n
        self.scope_range = scope_range

    end_point: Tuple[float, float]
    points_x = []
    points_y = []
    iterator = 0
    points_names = []

    def execute(self):
        scope = np.linspace(self.scope_range[0], self.scope_range[1], 100)
        x = random.choices(scope)[0]
        print(x)
        y = self.get_function_value(x)
        self.add_point(x, y)
        for i in range(self.n):
            tmp = random.choices(self.dispersion)[0]
            x_pot = x + tmp
            if x_pot > self.scope_range[1] or x_pot < self.scope_range[0]:
                new_scope = np.linspace(x_pot-0.5, x_pot+0.5)
                x_pot = random.choices(new_scope)[0]
            else:
                y_pot = self.get_function_value(x_pot)
                if y_pot >= y:
                    x, y = x_pot, y_pot
                    self.add_point(x, y)
                else:
                    self.dispersion -= self.increment_factor
            print(f"{i}: ({x}, {y}), ({self.dispersion[0]}, {self.dispersion[-1]})")
        self.end_point = (x, y)

    @staticmethod
    def get_function_value(x):
        """Calculates value of function for x

        :param x:
        :return: f(x)
        """
        return math.sin(x / 10) * math.sin(x / 200)

    def show_chart(self):
        """Creating chart for function and points

        :return: plot
        """
        chart = Chart((1, 1))
        chart.labels("wartość X", "wartość Y")
        x = np.linspace(0, 100, 200)
        y = np.sin(x / 10) * np.sin(x / 200)
        chart.draw_function(x, y)
        for i in range(len(self.points_x)):
            self.points_names.append(i)
        chart.draw_many_points(self.points_x, self.points_y, point_name=self.points_names)
        chart.show()

    def add_point(self, x, y):
        """Adding point values to lists

        :param x:
        :param y:
        :return:
        """
        self.points_x.append(x)
        self.points_y.append(y)
