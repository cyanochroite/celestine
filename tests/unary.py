import unittest
import sys
sys.path.insert(1, '../src/')

from mem_dixy.tag.unary import unary
from mem_dixy.Unicode.U0000 import ASTERISK
from mem_dixy.Unicode.U0000 import HYPHEN_MINUS
from mem_dixy.Unicode.U0000 import PLUS_SIGN


class test_unary(unittest.TestCase):
    def test_add_primary(self):
        token = set(
            (
                PLUS_SIGN
            )
        )
        self.assertSetEqual(token, unary.add.primary)
        self.assertIs(unary.parse(token), unary.add)

    def test_add_secondary(self):
        token = set(
            (
            )
        )
        self.assertSetEqual(token, unary.add.secondary)
        self.assertIs(unary.parse(token), unary.add)

    def test_div_primary(self):
        token = set(
            (
                ASTERISK,
                HYPHEN_MINUS
            )
        )
        self.assertSetEqual(token, unary.div.primary)
        self.assertIs(unary.parse(token), unary.div)

    def test_div_secondary(self):
        token = set(
            (
                ASTERISK,
                HYPHEN_MINUS,
                PLUS_SIGN
            )
        )
        self.assertSetEqual(token, unary.div.secondary)
        self.assertIs(unary.parse(token), unary.div)

    def test_mul_primary(self):
        token = set(
            (
                ASTERISK
            )
        )
        self.assertSetEqual(token, unary.mul.primary)
        self.assertIs(unary.parse(token), unary.mul)

    def test_mul_secondary(self):
        token = set(
            (
                ASTERISK,
                PLUS_SIGN
            )
        )
        self.assertSetEqual(token, unary.mul.secondary)
        self.assertIs(unary.parse(token), unary.mul)

    def test_sub_primary(self):
        token = set(
            (
                HYPHEN_MINUS
            )
        )
        self.assertSetEqual(token, unary.sub.primary)
        self.assertIs(unary.parse(token), unary.sub)

    def test_sub_secondary(self):
        token = set(
            (
                HYPHEN_MINUS,
                PLUS_SIGN
            )
        )
        self.assertSetEqual(token, unary.sub.secondary)
        self.assertIs(unary.parse(token), unary.sub)


if __name__ == '__main__':
    unittest.main()
