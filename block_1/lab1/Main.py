from scripts.lab1.decision_system import DecisionSystem


def main():
    decision_system = DecisionSystem(name="iris")
    decision_system.read_data("block_1/data/irys-data.txt", 'block_1/data/attributes.txt')
    # decision_system.get_all_data()
    # print(decision_system.get_data(1))
    print(decision_system.get_value(0, 2))


if __name__ == "__main__":
    main()
