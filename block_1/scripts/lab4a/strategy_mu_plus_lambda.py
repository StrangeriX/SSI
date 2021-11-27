import numpy as np
from typing import Tuple
import copy
import random
from block_1.scripts.lab4a.sample import Sample
from block_1.scripts.Chart import Chart


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
        chart = Chart((1, 1))
        for _ in range(self.mu):
            self.parents.append(self.create_new_sample())
        for i in range(self.n):
            # wyświetlanie
            x1 = []
            x2 = []
            for i in self.parents:
                x1.append(i.x1)
                x2.append(i.x2)
            chart.draw_many_points(x1, x2, name="parent")
            # .........
            new_generation = []
            for _ in range(self.lambda_value):
                winner = self.do_tournament(self.parents)
                winner.mutate(self.mutation_level, (self.scope_range[0], self.scope_range[-1]))
                new_generation.append(winner)

            full_generation = self.parents + new_generation
            new_parents = []
            for _ in range(self.mu):
                new_parent = self.do_tournament(full_generation)
                new_parents.append(new_parent)

            # wyswietlanie
            x1 = []
            x2 = []
            for i in new_generation:
                x1.append(i.x1)
                x2.append(i.x2)
            chart.draw_many_points(x1, x2, "dzieci")
            chart.show()
            # .................
            self.parents = new_parents

    def create_new_sample(self):
        x1 = random.choice(self.scope_range)
        x2 = random.choice(self.scope_range)
        parent = Sample(x1, x2)
        return parent

    def do_tournament(self, generation):
        new_tournament = []
        for i in range(self.tournament_size):
            sample = random.choice(generation)
            child = copy.deepcopy(sample)
            new_tournament.append(child)
        winner = new_tournament[0]
        for i in new_tournament:
            if i.get_value() > winner.get_value():
                winner = i
        return winner

    def get_parents(self):
        for i in self.parents:
            print(i)
