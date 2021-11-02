from typing import List, Optional, Tuple
from numpy import sqrt
import random

from .Row import Row

class KMeans:
    __data: List[Row] = []
    def __init__(self, dataset):
        self.__data = dataset.data

    def metrics(self):
        pass

    def kMeans(self, m: Optional[int] = None, n: Optional[int] = None):
        group: List[Tuple(int, Row)] = []
        
        group.append((0, self.__data[2]))
        print(group)



    def show_chart(self):
        pass
