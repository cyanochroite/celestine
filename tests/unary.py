import unittest
import sys
sys.path.insert(1, '../src/gui')


from mem_dixy.tag.unary import *


class check_comparison(unittest.TestCase):
    @classmethod
    def _add_token(cls, token):  # +-*
        index = unary.parse(token)
        return cls.all_encoding.get(index)

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.all_encoding = {
            0x0: add,  # ___
            0x1: mul,  # __*
            0x2: sub,  # _-_
            0x3: div,  # _-*
            0x4: add,  # +__
            0x5: mul,  # +_*
            0x6: sub,  # +-_
            0x7: div,  # +-*
        }

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.all_encoding = {}

    def test(self):
        token = {}
        self.assertIs(self._add_token(token), add)

    def test__ASTERISK(self):
        token = {ASTERISK}
        self.assertIs(self._add_token(token), mul)

    def test__HYPHEN_MINUS(self):
        token = {HYPHEN_MINUS}
        self.assertIs(self._add_token(token), sub)

    def test__HYPHEN_MINUS__ASTERISK(self):
        token = {HYPHEN_MINUS, ASTERISK}
        self.assertIs(self._add_token(token), div)

    def test__PLUS_SIGN(self):
        token = {PLUS_SIGN}
        self.assertIs(self._add_token(token), add)

    def test__PLUS_SIGN__ASTERISK(self):
        token = {PLUS_SIGN, ASTERISK}
        self.assertIs(self._add_token(token), mul)

    def test__PLUS_SIGN__HYPHEN_MINUS(self):
        token = {PLUS_SIGN, HYPHEN_MINUS}
        self.assertIs(self._add_token(token), sub)

    def test__PLUS_SIGN__HYPHEN_MINUS__ASTERISK(self):
        token = {PLUS_SIGN, HYPHEN_MINUS, ASTERISK}
        self.assertIs(self._add_token(token), div)


if __name__ == '__main__':
    unittest.main()
