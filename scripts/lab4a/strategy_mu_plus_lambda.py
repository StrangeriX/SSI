import numpy as np
from typing import Tuple
import copy
import random
from scripts.lab4a.sample import Sample
from scripts.Chart import Chart


class MuPlusLambdaStrategy:
    parents = []
    children = []

    def __init__(self, scope_range: Tuple[float, float], n: int, mu: int, lambda_value: int, tournament_size: int,
                 mutation_level: float, each_iteration: bool = True):
        self.n = n
        self.scope_range = np.linspace(scope_range[0], scope_range[1], 100)
        self.mu = mu
        self.lambda_value = lambda_value
        self.tournament_size = tournament_size
        self.mutation_level = scope_range[1] / mutation_level
        self.each_iteration = each_iteration

    def execute(self):

        for _ in range(self.mu):
            self.parents.append(self.create_new_sample())
        for i in range(self.n):
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
            print(self.get_best_value())
            if self.each_iteration:
                self.show_chart(self.parents, new_parents)
            self.parents = copy.deepcopy(new_parents)

    def create_new_sample(self) -> Sample:
        """Create new random sample
        :return: new Sample
        """
        x1 = random.choice(self.scope_range)
        x2 = random.choice(self.scope_range)
        parent = Sample(x1, x2)
        return parent

    def do_tournament(self, generation) -> Sample:
        """Return sample that won the tournament

        :param generation: List[Sample]
        :return: Sample
        """
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

    def show_chart(self, parents, children):
        """Show chart with parents and children of generation

        :param parents: List[Sample]
        :param children: List[Sample]
        :return: Chart
        """
        chart = Chart((1, 1))
        chart.clear_axes()
        chart.title(f"Best: {self.get_best_value()}")
        x1, x2 = np.meshgrid(self.scope_range, self.scope_range)
        y = np.sin(x1 * 0.05) + np.sin(x2 * 0.05) + 0.4 * np.sin(x1 * 0.15) * np.sin(x2 * 0.15)
        chart.ax.contour(x1, x2, y)
        c1 = []
        c2 = []
        for parent in parents:
            a, b = parent.get_coordinates()
            c1.append(a)
            c2.append(b)
        chart.draw_many_points(c1, c2, color='r', name='parents', size=60)
        c1.clear()
        c2.clear()
        for child in children:
            a, b = child.get_coordinates()
            c1.append(a)
            c2.append(b)
        chart.draw_many_points(c1, c2, color='b', name='children')
        chart.show()

    def get_best_value(self):
        """Return highest value of function of parents

        :return: int
        """
        best = 0
        for i in self.parents:
            if i.get_value() > best:
                best = i.get_value()
        return best
