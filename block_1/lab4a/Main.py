from block_1.scripts.lab4a.strategy_mu_plus_lambda import MuPlusLambdaStrategy


def main():
    mulambda = MuPlusLambdaStrategy(scope_range=(0, 100), n=4, mu=4, lambda_value=10,
                                    tournament_size=2, mutation_level=10)
    mulambda.execute()


if __name__ == "__main__":
    main()
