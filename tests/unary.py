import unittest
import sys
sys.path.insert(1, '../src/gui')

from mem_dixy.Unicode.U0000 import ASTERISK
from mem_dixy.Unicode.U0000 import HYPHEN_MINUS
from mem_dixy.Unicode.U0000 import PLUS_SIGN
from mem_dixy.tag.unary import unary


class check_unary(unittest.TestCase):
    def test(self):
        token = {}
        self.assertEqual(token, unary.add.secondary)
        self.assertIs(unary.parse(token), unary.add)

    def test__ASTERISK(self):
        token = {ASTERISK}
        self.assertEqual(token, unary.mul.primary)
        self.assertIs(unary.parse(token), unary.mul)

    def test__HYPHEN_MINUS(self):
        token = {HYPHEN_MINUS}
        self.assertEqual(token, unary.sub.primary)
        self.assertIs(unary.parse(token), unary.sub)

    def test__HYPHEN_MINUS__ASTERISK(self):
        token = {HYPHEN_MINUS, ASTERISK}
        self.assertEqual(token, unary.div.primary)
        self.assertIs(unary.parse(token), unary.div)

    def test__PLUS_SIGN(self):
        token = {PLUS_SIGN}
        self.assertEqual(token, unary.add.primary)
        self.assertIs(unary.parse(token), unary.add)

    def test__PLUS_SIGN__ASTERISK(self):
        token = {PLUS_SIGN, ASTERISK}
        self.assertEqual(token, unary.mul.secondary)
        self.assertIs(unary.parse(token), unary.mul)

    def test__PLUS_SIGN__HYPHEN_MINUS(self):
        token = {PLUS_SIGN, HYPHEN_MINUS}
        self.assertEqual(token, unary.sub.secondary)
        self.assertIs(unary.parse(token), unary.sub)

    def test__PLUS_SIGN__HYPHEN_MINUS__ASTERISK(self):
        token = {PLUS_SIGN, HYPHEN_MINUS, ASTERISK}
        self.assertEqual(token, unary.div.secondary)
        self.assertIs(unary.parse(token), unary.div)


if __name__ == '__main__':
    unittest.main()
