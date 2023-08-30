

"""
This problem was asked by LinkedIn.
Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
_For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)]._
"""
from math import sqrt
import unittest


def find_distance(from_: [float, float], to: [float, float]) -> float:
    return sqrt((from_[0] - to[0]) ** 2 + (from_[1] - to[1]) ** 2)


# 0(n) time
def find_n_closest_from_x(x: (float, float), points: tuple, n=1) -> list:
    if n > len(points):
        raise ValueError(f"n is {n} but length of points is {len(points)}")
    distances = sorted([(find_distance(x, point), i)
                        for i, point in enumerate(points)])
    return [points[distance[1]] for distance in distances][0:n]


class TestDistance(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(find_n_closest_from_x(
            x=(1, 2),
            points=[(0, 0), (5, 4), (3, 1)],
            n=2
        ), [(0, 0), (3, 1)])

    def test_large_distances(self):
        self.assertEqual(find_n_closest_from_x(
            x=(0, 0),
            points=[(1, 0), (5, 4), (3, 1), (9, 9),
                    (-2, 4), (3, 0), (6, 7), (-1, -1)],
            n=2
        ), [(1, 0), (-1, -1)])

    @unittest.expectedFailure
    def test_invalid_arguments(self):
        find_n_closest_from_x(
            x=(0, 0), points=[(1, 1)], n=2)


if __name__ == "__main__":
    unittest.main()
