import unittest
import sys
sys.path.insert(1, '../src/gui')


from mem_dixy.tag.comparison import *


class test_comparison(unittest.TestCase):
    def test(self):
        token = set(())
        self.assertSetEqual(token, comparison.nu.primary)
        self.assertIs(comparison.parse(token), comparison.nu)

    def test__EQUALS_SIGN(self):
        token = set((EQUALS_SIGN))
        self.assertSetEqual(token, comparison.eq.primary)
        self.assertIs(comparison.parse(token), comparison.eq)

    def test__EQUALS_SIGN__EXCLAMATION_MARK(self):
        token = set((EQUALS_SIGN, EXCLAMATION_MARK))
        self.assertIs(self._add_token(token), ne)
        self.assertSetEqual(token, comparison.ne.secondary)
        self.assertIs(comparison.parse(token), comparison.ne)

    def test__EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        token = set((EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN))
        self.assertSetEqual(token, comparison.lt.secondary)
        self.assertIs(comparison.parse(token), comparison.lt)

    def test__EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        token = set((EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.nn.secondary)
        self.assertIs(comparison.parse(token), comparison.nn)

    def test__EQUALS_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        token = set((EQUALS_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.gt.secondary)
        self.assertIs(comparison.parse(token), comparison.gt)

    def test__EQUALS_SIGN__GREATER_THAN_SIGN(self):
        token = set((EQUALS_SIGN, GREATER_THAN_SIGN))
        self.assertSetEqual(token, comparison.ge.primary)
        self.assertIs(comparison.parse(token), comparison.ge)

    def test__EQUALS_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        token = set((EQUALS_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.nu.secondary)
        self.assertIs(comparison.parse(token), comparison.nu)

    def test__EQUALS_SIGN__LESS_THAN_SIGN(self):
        token = set((EQUALS_SIGN, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.le.primary)
        self.assertIs(comparison.parse(token), comparison.le)

    def test__EXCLAMATION_MARK(self):
        token = set((EXCLAMATION_MARK))
        self.assertSetEqual(token, comparison.nn.primary)
        self.assertIs(comparison.parse(token), comparison.nn)

    def test__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        token = set((EXCLAMATION_MARK, GREATER_THAN_SIGN))
        self.assertSetEqual(token, comparison.le.secondary)
        self.assertIs(comparison.parse(token), comparison.le)

    def test__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        token = set((EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.eq.secondary)
        self.assertIs(comparison.parse(token), comparison.eq)

    def test__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        token = set((EXCLAMATION_MARK, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.ge.secondary)
        self.assertIs(comparison.parse(token), comparison.ge)

    def test__GREATER_THAN_SIGN(self):
        token = set((GREATER_THAN_SIGN))
        self.assertSetEqual(token, comparison.gt.primary)
        self.assertIs(comparison.parse(token), comparison.gt)

    def test__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        token = set((GREATER_THAN_SIGN, LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.ne.secondary)
        self.assertIs(comparison.parse(token), comparison.ne)

    def test__LESS_THAN_SIGN(self):
        token = set((LESS_THAN_SIGN))
        self.assertSetEqual(token, comparison.lt.primary)
        self.assertIs(comparison.parse(token), comparison.lt)



if __name__ == '__main__':
    unittest.main()
