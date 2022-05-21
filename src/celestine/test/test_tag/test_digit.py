import unittest

from celestine.symbol.digit import Digit


class test_digit(unittest.TestCase):
    def test_new(self):
        digit = Digit(75)
        self.assertEqual(digit.value, 75)

