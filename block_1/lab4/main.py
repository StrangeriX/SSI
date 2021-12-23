from scripts.lab4.Strategy_1plus1 import OnePlusOneStrategy


def main():
    one_plus_one = OnePlusOneStrategy(10.0, 1.1, (0, 100), 100)
    one_plus_one.execute()
    one_plus_one.show_chart()


if __name__ == "__main__":
    main()
