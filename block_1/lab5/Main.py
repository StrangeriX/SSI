from block_1.scripts.lab4a.strategy_mu_plus_lambda import MuPlusLambdaStrategy


def main():
    mulambda = MuPlusLambdaStrategy((0, 100), 2, 4, 10, 2, 10)
    mulambda.execute()


if __name__ == "__main__":
    main()
