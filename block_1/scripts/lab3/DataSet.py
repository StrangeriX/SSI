from typing import List, Tuple, Optional
from numpy import sqrt
import random
from .Row import Row
from block_1.scripts.Chart import Chart
import os


class DataSet:
    __data: List[Row] = []

    def __init__(self, name):
        self.name = name
        self.__data = []

    def read_data(self, values_file, index:Optional[Tuple[int,int]] = None):
        values = open(values_file, 'r')
        for i in values:
            value = i.split()
            if index:
                value = [value[index[0]], value[index[1]]]
                for i in range(len(value)):
                    value[i] = float(value[i].replace(',','.'))
                row = Row([value[0], value[1]])
                self.__data.append(row)
            else:
                for i in range(len(value)):
                    value[i] = float(value[i].replace(',','.'))

    # m - ilość klas, n - ilość iteracji
    def kmean(self, m: Optional[int] = None, n: Optional[int] = None):
        if m and n:
            pass
        if not m:
            m = random.randint(2, 6)
        if not n:
            n = random.randint(10, 30)
        # groups: lista(nr. grupy, (x środka, y środka))
        groups: List[Tuple[int, (float, float)]] = []
        # grouped_data: lista((grupa, próbka))
        grouped_data: List[Tuple[int, Row]] = []
        
        # Losowe wybranie środków grup
        for i in range(m):
            tmp = random.randrange(0, len(self.__data))
            groups.append((i, (self.__data[tmp].get_value(0), self.__data[tmp].get_value(1))))

        for _ in range(n):
            for i in self.__data:
                grouped_data.append((self.choose_group(i, groups), i))
            for i in groups:
                x_sum = 0
                y_sum = 0
                group_len = 0
                for j in grouped_data:
                    if j[0] == i[0]:
                        x_sum += j[1].get_value(0)
                        y_sum += j[1].get_value(1)
                        group_len += 1
                if group_len == 0:
                    pass
                else:
                    #print(f'{x_sum/group_len}')
                    groups[i[0]] = (i[0], (x_sum/group_len, y_sum/group_len))
        self.draw(groups, grouped_data)

    def euclidean_distance(self, p1: Row, p2):
        return sqrt(pow((p1.get_value(0) - p2[0]),2) + pow((p1.get_value(1) - p2[1]),2))

    def draw(self, groups, grouped_data):
        chart = Chart((1, 1))
        chart.labels("Wartości x", 'Wartości y')
        for group in groups:
            x, y = self.choose_samples(grouped_data, group[0])
            chart.draw_many_points(x, y, f"{group[0]}")
        for i in groups:
            chart.draw_point(i[1][0], i[1][1])
           # print(f"x: {i[1][0]}, y: {i[1][1]}\n")
        chart.show()
            
    def choose_samples(self, grouped_data, class_name):
        x = []
        y = []
        for i in grouped_data:
            if i[0] == class_name:
                x.append(i[1].get_value(0))
                y.append(i[1].get_value(1))
        return x, y

    def choose_group(self, sample: Row, groups):
        data_to_group = 900
        group: int = 0
        for i in groups:
            tmp = self.euclidean_distance(sample, i[1])
            if tmp < data_to_group:
                data_to_group = tmp
                group = i[0]
        return group