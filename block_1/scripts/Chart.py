from typing import List, Tuple, Optional
import matplotlib.pyplot as plot
import numpy as np


class Chart:
    def __init__(self, subplots: Tuple[int, int]):
        self.subplot_x, self.subplot_y = subplots
        self.fig, self.ax = plot.subplots(self.subplot_x, self.subplot_y)
        self.max_subplots = self.subplot_x * self.subplot_y
        plot.subplot(self.subplot_x, self.subplot_y, 1)
        self.current_subplot = 1
        self.style_number = 0

    def clear_axes(self):
        plot.cla()

    def show(self):
        plot.show()

    def grid(self):
        plot.grid()

    def title(self, title: str):
        plot.title(title)

    def labels(self, x: str, y: str):
        plot.xlabel(x)
        plot.ylabel(y)

    def get_style(self):
        styles = ['r--', 'b-', 'k-', 'g--', 'y-', 'co', 'm-', 'k--', 'b--', 'r-']
        return styles[self.style_number % 10]


    def next_subplot(self):
        if self.current_subplot >= self.max_subplots:
            self.current_subplot = 1
            plot.subplot(self.subplot_x, self.subplot_y, 1)
        else:
            self.current_subplot += 1
            plot.subplot(self.subplot_x, self.subplot_y, self.current_subplot)

    def draw_point(self, x: float, y: float, color: Optional[str] = None):
        if color:
            plot.scatter(x, y, c=color)
            plot.legend()
        else:
            plot.scatter(x, y)

        plot.draw()

    def draw_many_points(self, x: List[float], y: List[float], name: Optional[str] = None, point_name: Optional[List[str]] = None, color: Optional[str] = None, size: int = None):
        if name and color:
            if len(x) == len(y):
                plot.scatter(x, y, label=name, c=color, s=size)
                plot.legend()
                plot.draw()
            else:
                raise Exception("Number of x is not same as number of y")
        elif name:
            if len(x) == len(y):
                plot.scatter(x, y, c=color)
                plot.draw()
            else:
                raise Exception("Number of x is not same as number of y")
        else:
            if len(x) == len(y):
                plot.scatter(x, y, c=color)
                plot.draw()
            else:
                raise Exception("Number of x is not same as number of y")
        if point_name:
            plot.scatter(x, y)
            for i, txt in enumerate(point_name):
                plot.annotate(txt, (x[i], y[i]))

    def draw_line(self, start: Tuple[float, float], end: Tuple[float, float], style: str = ''):
        if not style:
            style = self.get_style()
            self.style_number += 1
        plot.plot([start[0], end[0]], [start[1], end[1]], style)
        plot.draw()

    def draw_function(self, scope, function):
        plot.plot(scope, function)
        plot.draw()

    def draw_face(self):
        pass