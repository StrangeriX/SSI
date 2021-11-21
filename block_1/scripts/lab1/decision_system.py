from typing import List
from .Row import Row


class DecisionSystem:
    __data: List[Row]

    def __init__(self, name):
        self.__data = []
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
            if len(row) == len(attributes_types):
                class_name = row[-1]
                new_row = Row(class_name, attributes_types, row, attributes_names)
                self.__data.append(new_row)
            else:
                raise Exception("Data given not match attributes list")

    # funkcja czytające atrybuty i sprawdzająca czy są atrybutem klasowym
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
        for i in self.__data:
            print(i)

    def get_value(self, index: int, data: int):
        """Print value of sample

        :param index: int
        :param data: int
        :return:
        """
        print(self.__data[index].get_value(data))

    # funkcja wyświetlająca podaną próbkę
    def get_data(self, index: int):
        """Print sample data

        :param index:
        :return:
        """
        print(self.__data[index])

    def __str__(self):
        return f"DecisionSystem: name: {self.name}"
