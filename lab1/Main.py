import os
from scripts.DecisionSystem import DecisionSystem


def main():
    decision_system = DecisionSystem(name="iris")
    decision_system.read_data("data/iris-data", 'data/attributes')
    # decision_system.get_all_data()
    # print(decision_system.get_data(1))
    print(decision_system.get_value(0, 2))


if __name__ == "__main__":
    main()
