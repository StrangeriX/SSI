import math

from scripts.bitmap import Bitmap
from scripts.Chart import Chart
from typing import List


class GreedyPointer:
    reference_bitmaps: List[Bitmap] = []

    def __init__(self, reference_bitmaps: List[Bitmap] = None):
        if reference_bitmaps:
            self.reference_bitmaps = reference_bitmaps

    def classify(self, test: Bitmap, metric: str = 'e'):
        distances = []
        for reference in self.reference_bitmaps:
            dissimilarity1 = self.calculate_dissimilarity(test, reference, metric)
            dissimilarity2 = self.calculate_dissimilarity(reference, test, metric)
            distance = -dissimilarity1 - dissimilarity2
            distances.append(distance)
        most_similar = max(distances)
        print(f"bitmapa testowa jest najbardziej podobna do wzorca {distances.index(most_similar) + 1}")
        self.show_chart(test, self.reference_bitmaps[distances.index(most_similar)])


    def calculate_dissimilarity(self, reference_bitmap: Bitmap, test_bitmap: Bitmap, distance_metric: str):
        result = 0
        test_size = test_bitmap.size
        reference_size = reference_bitmap.size
        for test_row in range(test_size[0]):
            for test_value in range(test_size[1]):
                min_distance = float("inf")
                if test_bitmap.get_value(test_row, test_value) == 1:
                    for ref_row in range(reference_size[0]):
                        for ref_value in range(reference_size[1]):
                            if reference_bitmap.get_value(ref_row, ref_value) == 1:
                                if distance_metric == "e":
                                    distance = self.euclidean_distance((test_row, test_value), (ref_row, ref_value))
                                elif distance_metric == 'm':
                                    distance = self.manhattan_distance((test_row, test_value), (ref_row, ref_value))
                                min_distance = min(min_distance, distance)
                    result += min_distance
        return result

    @staticmethod
    def manhattan_distance(start, end):
        start_x, start_y = start
        end_x, end_y = end
        return abs(start_x - end_x) + abs(start_y - end_y)

    @staticmethod
    def euclidean_distance(start, end):
        start_x, start_y = start
        end_x, end_y = end
        return math.sqrt(math.pow((start_x - end_x), 2) + math.pow((start_y - end_y), 2))

    def add_reference_bitmap(self, values: List[List[int]]):
        x = len(values)
        y = len(values[0])
        new = Bitmap((x, y))
        new.set_matrix(values)
        self.reference_bitmaps.append(new)

    @staticmethod
    def show_chart(test: Bitmap, ref: Bitmap):
        chart = Chart((1, 2))
        chart.title("Reference bitmap")
        chart.draw_bitmap(ref)
        chart.next_subplot()
        chart.title("test bitmap")
        chart.draw_bitmap(test)
        chart.show()

