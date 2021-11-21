import random
import math
import numpy as np
from typing import Tuple
from block_1.scripts.Chart import Chart


class Strategy_1plus1:
    zakres_zmienności = [0.0, 100.0]
    def __init__(self, rozrzut: float, wsp_przyrostu: float, n: int):
        self.rozrzut = np.linspace(-rozrzut, rozrzut, 100)
        self.wsp_przyrostu = wsp_przyrostu
        self.n = n
    end_point: Tuple[float, float]
    points = []
    zakres = np.linspace(zakres_zmienności[0], zakres_zmienności[1])

    def start(self):
        x = random.choices(self.zakres)[0]
        y = self.get_function_value(x)
        self.points.append((x, y))
        for i in range(self.n):
            tmp = random.choices(self.rozrzut)[0]
            xPot = x + tmp
            if xPot > self.zakres_zmienności[1] or xPot < self.zakres_zmienności[0]:
            # do zmiany
            #    new_scope = np.linspace(xPot-0.5, xPot+0.5)
            #    xPot = random.choices(new_scope)[0]
                xPot = random.choices(self.zakres)[0]
            yPot = self.get_function_value(xPot)
            if yPot >= y:
                x, y = xPot, yPot
            else:
                self.rozrzut -= self.wsp_przyrostu
            self.points.append((xPot, yPot))
            print(f"{i}: ({x}, {y}), ({self.rozrzut[0]}, {self.rozrzut[-1]})")
        self.end_point = (xPot, yPot)
    def get_function_value(self, x):
        return math.sin(x/10) * math.sin(x/200)

    def show_chart(self):
        chart = Chart((1, 1))
        chart.labels("wartość X", "wartość Y")
        x = np.linspace(0, 100, 200)
        y = np.sin(x/10) * np.sin(x/200)
        chart.draw_function(x, y)
    #    for i in self.points:
    #       chart.draw_point(i[0], i[1])
        chart.draw_point(self.end_point[0], self.end_point[1], "y")
        chart.show()
