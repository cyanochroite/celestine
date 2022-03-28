import unittest
import sys
sys.path.insert(1, '../src/gui')

from mem_dixy.Unicode.U0000 import ASTERISK
from mem_dixy.Unicode.U0000 import HYPHEN_MINUS
from mem_dixy.Unicode.U0000 import PLUS_SIGN
from mem_dixy.tag.unary import unary


class check_unary(unittest.TestCase):
    @classmethod
    def _add_token(cls, token):  # +-*
        index = unary.parse(token)
        return cls.all_encoding.get(index)

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.all_encoding = {
            0x0: unary.add,  # ___
            0x1: unary.mul,  # __*
            0x2: unary.sub,  # _-_
            0x3: unary.div,  # _-*
            0x4: unary.add,  # +__
            0x5: unary.mul,  # +_*
            0x6: unary.sub,  # +-_
            0x7: unary.div,  # +-*
        }

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.all_encoding = {}

    def test(self):
        token = {}
        self.assertIs(self._add_token(token), unary.add)

    def test__ASTERISK(self):
        token = {ASTERISK}
        self.assertIs(self._add_token(token), unary.mul)

    def test__HYPHEN_MINUS(self):
        token = {HYPHEN_MINUS}
        self.assertIs(self._add_token(token), unary.sub)

    def test__HYPHEN_MINUS__ASTERISK(self):
        token = {HYPHEN_MINUS, ASTERISK}
        self.assertIs(self._add_token(token), unary.div)

    def test__PLUS_SIGN(self):
        token = {PLUS_SIGN}
        self.assertIs(self._add_token(token), unary.add)

    def test__PLUS_SIGN__ASTERISK(self):
        token = {PLUS_SIGN, ASTERISK}
        self.assertIs(self._add_token(token), unary.mul)

    def test__PLUS_SIGN__HYPHEN_MINUS(self):
        token = {PLUS_SIGN, HYPHEN_MINUS}
        self.assertIs(self._add_token(token), unary.sub)

    def test__PLUS_SIGN__HYPHEN_MINUS__ASTERISK(self):
        token = {PLUS_SIGN, HYPHEN_MINUS, ASTERISK}
        self.assertIs(self._add_token(token), unary.div)


    def test__add(self):
        self.assertEqual(unary.add.primary, "+")
        self.assertEqual(unary.add.secondary, "")

    def test__div(self):
        self.assertEqual(unary.div.primary, "-*")
        self.assertEqual(unary.div.secondary, "+-*")

    def test__mul(self):
        self.assertEqual(unary.mul.primary, "*")
        self.assertEqual(unary.mul.secondary, "+*")

    def test__sub(self):
        self.assertEqual(unary.sub.primary, "-")
        self.assertEqual(unary.sub.secondary, "+-")


if __name__ == '__main__':
    unittest.main()
