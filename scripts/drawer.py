from typing import Tuple
from scripts.bitmap import Bitmap
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


class Drawer:
    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.fig, self.ax = plt.subplots(1, 1)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.array = np.zeros(self.size)
        self.cmapmine = ListedColormap(['w', 'black'], N=2)
        self.map = np.zeros(self.size)

    def on_click(self, event):
        xdata = event.xdata
        ydata = event.ydata
        self.array[round(ydata)][round(xdata)] = 1
        plt.clf()
        plt.imshow(self.array, cmap=self.cmapmine, vmin=0, vmax=1, picker=True, interpolation="nearest")  # inform matplotlib of the new data
        plt.draw()

    def draw_bitmap(self):
        plt.imshow(self.array, cmap=self.cmapmine, vmin=0, vmax=1, picker=True, interpolation="nearest")

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
    def start(self):
        x = [i for i in range(self.size[1])]
        for i in range(len(self.map)):
            self.map[i] = x
        self.draw_bitmap()
        plt.show()
        result = Bitmap(self.size)
        result.set_matrix(self.array)
        return result


