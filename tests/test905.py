import unittest

from problems.day_905 import can_form_circle


class TestProblem905(unittest.TestCase):

    def test_word_circle_finder(self):
        self.assertEqual(can_form_circle(
            ['chair', 'height', 'racket', 'touch', 'tunic']),
            True
        )

    def test_word_circle_finder_no_loop(self):
        self.assertEqual(can_form_circle(
            ['chair', 'racket', 'touch', 'tunic']),
            False
        )

    def test_word_circle_finder_w_loop_large(self):
        self.assertEqual(can_form_circle(
            ['chair', 'height', 'racket', 'touch', 'tunic', 'cigar', 'typical', 'rat', 'loc']),
            True
        )
