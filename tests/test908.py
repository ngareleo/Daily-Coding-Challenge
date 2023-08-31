import unittest
from problems.day_908 import count_disordered_cols, globals


class TestProblem908(unittest.TestCase):

    def test_disordered_cols_counter_a(self):
        self.assertEqual(count_disordered_cols(globals.get("a")), 1)

    def test_disordered_cols_counter_b(self):
        self.assertEqual(count_disordered_cols(globals.get("b")), 0)

    def test_disordered_cols_counter_c(self):
        self.assertEqual(count_disordered_cols(globals.get("c")), 3)
