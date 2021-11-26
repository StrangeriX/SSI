import numpy as np
from typing import Tuple
import math
import random
from block_1.scripts.lab4a.sample import Sample


class MuPlusLambdaStrategy:
    parents = []

    def __init__(self, scope_range: Tuple[float, float], n: int, mu: int, lambda_value: int, tournament_size: int,
                 mutation_level: float):
        self.n = n
        self.scope_range = np.linspace(scope_range[0], scope_range[1], 100)
        self.mu = mu
        self.lambda_value = lambda_value
        self.tournament_size = tournament_size
        self.mutation_level = scope_range[1] / mutation_level

    def execute(self):
        for _ in range(self.mu):
            self.parents.append(self.create_new_sample())
        print("przed zmianami")
        self.get_parents()
        for i in range(self.n):
            new_generation = []
            for _ in range(self.lambda_value):
                winner = self.do_tournament()
                new_sample = winner.mutate(self.mutation_level)
                if new_sample not in new_generation:
                    new_generation.append(new_sample)
            full_generation = self.parents + new_generation
            new_parents = []
            for _ in range(self.mu):
                parent = full_generation[0]
                for sample in full_generation:
                    if sample.get_value() > parent.get_value():
                        parent = sample
                new_parents.append(parent)
                full_generation.remove(parent)
            self.parents = new_parents
            print("po zmianach")
            self.get_parents()

    def create_new_sample(self):
        x1 = random.choices(self.scope_range)[0]
        x2 = random.choices(self.scope_range)[0]
        parent = Sample(x1, x2)
        return parent

    def do_tournament(self):
        new_tournament = []
        for i in range(self.tournament_size):
            sample = random.choice(self.parents)
            if sample not in new_tournament:
                new_tournament.append(sample)
            else:
                i -= 1
        winner = new_tournament[0]
        for i in new_tournament:
            if i.get_value() > winner.get_value():
                winner = i
        return winner

    def get_parents(self):
        for i in self.parents:
            print(i)

