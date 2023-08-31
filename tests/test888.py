import unittest

from problems.day_888 import find_n_closest_from_x


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
