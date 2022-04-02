import unittest
import sys
sys.path.insert(1, '../src/')

from mem_dixy.tag.comparison import comparison
from mem_dixy.Unicode.U0000 import EQUALS_SIGN
from mem_dixy.Unicode.U0000 import EXCLAMATION_MARK
from mem_dixy.Unicode.U0000 import GREATER_THAN_SIGN
from mem_dixy.Unicode.U0000 import LESS_THAN_SIGN


class test_comparison(unittest.TestCase):
    def test_eq_primary(self):
        token = set(
            (
                EQUALS_SIGN
            )
        )
        self.assertSetEqual(token, comparison.eq.primary)
        self.assertIs(comparison.parse(token), comparison.eq)

    def test_eq_secondary(self):
        token = set(
            (
                EXCLAMATION_MARK,
                GREATER_THAN_SIGN,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.eq.secondary)
        self.assertIs(comparison.parse(token), comparison.eq)

    def test_ge_primary(self):
        token = set(
            (
                EQUALS_SIGN,
                GREATER_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.ge.primary)
        self.assertIs(comparison.parse(token), comparison.ge)

    def test_ge_secondary(self):
        token = set(
            (
                EXCLAMATION_MARK,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.ge.secondary)
        self.assertIs(comparison.parse(token), comparison.ge)

    def test_gt_primary(self):
        token = set(
            (
                GREATER_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.gt.primary)
        self.assertIs(comparison.parse(token), comparison.gt)

    def test_gt_secondary(self):
        token = set(
            (
                EQUALS_SIGN,
                EXCLAMATION_MARK,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.gt.secondary)
        self.assertIs(comparison.parse(token), comparison.gt)

    def test_le_primary(self):
        token = set(
            (
                EQUALS_SIGN,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.le.primary)
        self.assertIs(comparison.parse(token), comparison.le)

    def test_le_secondary(self):
        token = set(
            (
                EXCLAMATION_MARK,
                GREATER_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.le.secondary)
        self.assertIs(comparison.parse(token), comparison.le)

    def test_lt_primary(self):
        token = set(
            (
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.lt.primary)
        self.assertIs(comparison.parse(token), comparison.lt)

    def test_lt_secondary(self):
        token = set(
            (
                EQUALS_SIGN,
                EXCLAMATION_MARK,
                GREATER_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.lt.secondary)
        self.assertIs(comparison.parse(token), comparison.lt)

    def test_ne_primary(self):
        token = set(
            (
                EQUALS_SIGN,
                EXCLAMATION_MARK
            )
        )
        self.assertSetEqual(token, comparison.ne.primary)
        self.assertIs(comparison.parse(token), comparison.ne)

    def test_ne_secondary(self):
        token = set(
            (
                GREATER_THAN_SIGN,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.ne.secondary)
        self.assertIs(comparison.parse(token), comparison.ne)

    def test_nn_primary(self):
        token = set(
            (
                EXCLAMATION_MARK
            )
        )
        self.assertSetEqual(token, comparison.nn.primary)
        self.assertIs(comparison.parse(token), comparison.nn)

    def test_nn_secondary(self):
        token = set(
            (
                EQUALS_SIGN,
                EXCLAMATION_MARK,
                GREATER_THAN_SIGN,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.nn.secondary)
        self.assertIs(comparison.parse(token), comparison.nn)

    def test_nu_primary(self):
        token = set(
            (
            )
        )
        self.assertSetEqual(token, comparison.nu.primary)
        self.assertIs(comparison.parse(token), comparison.nu)

    def test_nu_secondary(self):
        token = set(
            (
                EQUALS_SIGN,
                GREATER_THAN_SIGN,
                LESS_THAN_SIGN
            )
        )
        self.assertSetEqual(token, comparison.nu.secondary)
        self.assertIs(comparison.parse(token), comparison.nu)


if __name__ == '__main__':
    unittest.main()
