import random
import math
import numpy as np


class Strategy_1plus1:
    zakres_zmienności = [0.0,100.0]
    def __init__(self, rozrzut: float, wsp_przyrostu: float, n: int):
        self.rozrzut = rozrzut
        self.wsp_przyrostu = wsp_przyrostu
        self.n = n

    zakres = np.linspace(zakres_zmienności[0], zakres_zmienności[1])
    
    def start(self):
        x = random.choices(self.zakres)[0]
        y = self.get_function_value(x)
        for i in range(self.n):
            tmp = random.choices(range(self.rozrzut,self.rozrzut))
            xPot = x + tmp[0]
            if xPot > self.zakres_zmienności[1] or xPot < self.zakres_zmienności[0]:
                xPot = random.choices(range(0,100))[0]
            yPot = self.get_function_value(xPot)
            if yPot >= y:
                x,y = xPot,yPot
            else:
                self.rozrzut -= self.wsp_przyrostu
            print(f"{i}: ({x}, {y}), {self.rozrzut}")

    def get_function_value(self,x):
        return math.sin(x/10) * math.sin(x/200)