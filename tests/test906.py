import unittest
from problems.day_906 import find_2_closest_points, globals


class TestDay906(unittest.TestCase):

    def test_find_2_closest_point(self):
        set_a = globals.get("a")
        self.assertEqual(sorted(find_2_closest_points(
            set_a.get("1"))), sorted(set_a.get("2")))
