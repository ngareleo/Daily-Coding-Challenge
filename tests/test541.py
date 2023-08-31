import unittest
from problems.day_541 import encode


class TestEncoding(unittest.TestCase):

    def test_sample_string(self):
        self.assertEqual(encode("AAAABBBCCDAA"), "4A3B2C1D2A")
