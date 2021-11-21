from block_1.scripts.lab2.DecisionSystem import DecisionSystem
from block_1.scripts.Chart import Chart


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
    decision_system = DecisionSystem(name="iris")
    decision_system.read_data("block_1/data/irys-data.txt", 'block_1/data/attributes.txt')
    # chart_samples()
    # decision_system.get_all_data()
    # print(decision_system.get_data(1))
    # print(decision_system.get_value(0, 2))
    decision_system.show_chart((2, 2))
    # print(decision_system.get_all_data())


if __name__ == "__main__":
    main()
