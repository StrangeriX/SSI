from typing import List, Tuple
from .Row import Row
from scripts.Chart import Chart


class DecisionSystem:
    __data: List[Row]

    def __init__(self, name):
        self.__data = []
        self.__classes = []
        self.name = name

    def read_data(self, values_file: str, attributes_file: str):
        """Read data from file and prepare data set

                :param values_file:
                :param attributes_file:
                :return:
                """
        values_list = open(values_file, 'r')
        attributes_list = open(attributes_file, 'r')
        attributes_types: List[bool] = []
        attributes_names: List[str] = []
        self.__read_attributes(attributes_list, attributes_types, attributes_names)
        for value in values_list:
            row = value.split()
            for i in range(len(row)-1):
                row[i] = float(row[i].replace(',', '.'))
            if len(row) == len(attributes_types):
                class_name = row[-1]
                new_row = Row(class_name, attributes_types, row, attributes_names)
                self.__data.append(new_row)
                if class_name not in self.__classes:
                    self.__classes.append(class_name)
            else:
                raise Exception("Data given not match attributes list")

    def __read_attributes(self, attributes_list: str, attributes_types: List[bool], attributes_names: List[str]):
        """Check if attributes are class attributes

                :param attributes_list: List
                :param attributes_types: List
                :param attributes_names: List
                :return:
                """
        for att in attributes_list:
            attribute = att.split()
            attributes_names.append(attribute[0])
            if attribute[1] == 's':
                attributes_types.append(True)
            else:
                attributes_types.append(False)

    def get_all_data(self) -> List[Row]:
        """Print all samples

        :return: data
        """
        return self.__data

    def get_data_by_class(self, class_name: str):
        samples = []
        for i in self.__data:
            if i.class_name == class_name:
                samples.append(i.values)
        return samples

    def get_value(self, index: int, data: int):
        """Print value of sample

        :param index: int
        :param data: int
        :return:
        """
        print(self.__data[index].get_value(data))

    def get_data(self, index: int):
        """Print sample data

        :param index:
        :return:
        """
        print(self.__data[index])

    def show_chart(self, subplots: Tuple[int, int]):
        """Create chart of samples

        :param subplots:
        :return: plot
        """
        classes = self.__classes
        chart = Chart(subplots)
        chart.labels("Atrybut 3-go próbek", "Atrybut 4-go próbek")
        for i in classes:
            name = f"Class {i}"
            x, y = self.choose_samples(3, 4, i)
            chart.draw_many_points(x, y, name)
        chart.next_subplot()
        chart.labels("Atrybut 2-go próbek", "Atrybut 4-go próbek")
        for i in classes:
            name = f"Class {i}"
            x, y = self.choose_samples(2, 4, i)
            chart.draw_many_points(x, y, name)
        chart.next_subplot()
        chart.labels("Atrybut 1-go próbek", "Atrybut 4-go próbek")
        for i in classes:
            name = f"Class {i}"
            x, y = self.choose_samples(1, 4, i)
            chart.draw_many_points(x, y, name)
        chart.next_subplot()
        chart.labels("Atrybut 2-go próbek", "Atrybut 3-go próbek")
        for i in classes:
            name = f"Class {i}"
            x, y = self.choose_samples(2, 3, i)
            chart.draw_many_points(x, y, name)
        chart.next_subplot()
        chart.show()

    def choose_samples(self, os_x, os_y, class_name):
        """Choose sample that belongs to class
        :param os_x:
        :param os_y:
        :param class_name:
        :return: values of x and y of chosen samples
        """
        x = []
        y = []
        for sample in self.__data:
            if sample.class_name == class_name:
                x.append(sample.get_value(os_x-1))
                y.append(sample.get_value(os_y-1))
        return x, y

    def __str__(self):
        return f"DecisionSystem: name: {self.name}"
