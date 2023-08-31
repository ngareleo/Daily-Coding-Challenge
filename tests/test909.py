import unittest

from problems.day_909 import find_smallest_overlap


class TestSmallestOverLap(unittest.TestCase):

    def test_smallest_overlap(self):
        self.assertEqual(find_smallest_overlap([0, 3], [2, 5]), [3, 4])

    def test_smallest_overlap_b(self):
        self.assertEqual(find_smallest_overlap([1, 10], [3, 20]), [10, 11])

    def test_smallest_overlap_c(self):
        self.assertEqual(find_smallest_overlap([6, 9], [8, 15]), [8, 9])

    def test_smallest_overlap_d(self):
        self.assertEqual(find_smallest_overlap([0, 3], [3, 10]), [3, 4])

    def test_smallest_overlap_e(self):
        self.assertEqual(find_smallest_overlap([11, 9], [1, 2]), [2, 9])
