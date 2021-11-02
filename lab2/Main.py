from scripts.DecisionSystem import DecisionSystem
from scripts.Chart import Chart
import os


def chart_samples():
    chart = Chart((3, 2))
    chart.grid()
    x = [1, 2, 3]
    y = [1, 3, 4]
    chart.draw_many_points(x, y)
    chart.title("tytuł testowy")
    chart.labels('wartości x', 'wartości y')
    x = [2.3, 4.2, 5]
    y = [3, 4.5, 5.2]
    chart.draw_many_points(x, y)
    x = 1
    y = 10
    chart.draw_point(x, y)
    chart.next_subplot()
    chart.draw_line((1, 1), (3, 4))
    chart.draw_line((2,1), (4,3))
    chart.draw_line((2.1,11), (4,5.6))
    chart.draw_line((3,2), (5,1))
    chart.next_subplot()
    chart.clear_axes()
    chart.show()

def main():
    print(os.listdir('lab2'))
    decision_system = DecisionSystem(name="iris")
    decision_system.read_data("lab2/data/iris-data", 'lab2/data/attributes')
    # chart_samples()
    # decision_system.get_all_data()
    # print(decision_system.get_data(1))
    # print(decision_system.get_value(0, 2))
    decision_system.show_chart((2, 2))
    # print(decision_system.get_all_data())


if __name__ == "__main__":
    main()
