import unittest

from celestine.data.alphabet import Digit


class test_digit(unittest.TestCase):
    def test_new(self):
        self.assertEqual(Digit.DIGIT_7, Digit.DIGIT_7)

