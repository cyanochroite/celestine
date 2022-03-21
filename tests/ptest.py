import sys
sys.path.insert(1, '../src/gui')

#import file
import unittest

from mem_dixy.tag.alphabet import logical
from mem_dixy.Unicode.U0000 import *


from enum import Enum


class enum_comparison(Enum):
    lt = 0, # less then
    le = 1, # less then or equal to
    eq = 2, # equal to
    ne = 3, # not equal to
    ge = 4, # greater then
    gt = 5, # greater then or equal to
    sa = 6, # select all
    sn = 7  # select none


class operator():
    pass


class comparison(operator):
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return this.symbol


class lt(comparison):
    def __init__(self):
        super().__init__(str().join([LESS_THAN_SIGN]))


class le(comparison):
    def __init__(self):
        super().__init__(str().join([LESS_THAN_SIGN, EQUALS_SIGN]))


class eq(comparison):
    def __init__(self):
        super().__init__(str().join([EQUALS_SIGN]))


class ne(comparison):
    def __init__(self):
        super().__init__(str().join([EXCLAMATION_MARK, EQUALS_SIGN]))


class ge(comparison):
    def __init__(self):
        super().__init__(str().join([GREATER_THAN_SIGN, EQUALS_SIGN]))


class gt(comparison):
    def __init__(self):
        super().__init__(str().join([GREATER_THAN_SIGN]))


class sa(comparison):
    def __init__(self):
        super().__init__(str().join(
            [LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN]))


class sn(comparison):
    def __init__(self):
        super().__init__(str().join([EXCLAMATION_MARK]))


final_encoding = {
    enum_comparison.lt: str().join([LESS_THAN_SIGN]),
    enum_comparison.le: str().join([LESS_THAN_SIGN, EQUALS_SIGN]),
    enum_comparison.eq: str().join([EQUALS_SIGN]),
    enum_comparison.ne: str().join([EXCLAMATION_MARK, EQUALS_SIGN]),
    enum_comparison.ge: str().join([GREATER_THAN_SIGN, EQUALS_SIGN]),
    enum_comparison.gt: str().join([GREATER_THAN_SIGN]),
    enum_comparison.sa: str().join([LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN]),
    enum_comparison.sn: str().join([EXCLAMATION_MARK]),


}


all_encoding = {
    0x0: sa(),  # ____
    0x1: gt(),  # ___>
    0x2: eq(),  # __=_
    0x3: ge(),  # __=>
    0x4: lt(),  # _<__
    0x5: ne(),  # _<_>
    0x6: le(),  # _<=_
    0x7: sa(),  # _<=>
    0x8: sn(),  # !___
    0x9: le(),  # !__>
    0xA: ne(),  # !_=_
    0xB: lt(),  # !_=>
    0xC: ge(),  # !<__
    0xD: eq(),  # !<_>
    0xE: gt(),  # !<=_
    0xF: sn(),  # !<=>
}


def add_token(array):
    index = 0
    index |= EXCLAMATION_MARK in array
    index <<= 1
    index |= LESS_THAN_SIGN in array
    index <<= 1
    index |= EQUALS_SIGN in array
    index <<= 1
    index |= GREATER_THAN_SIGN in array
    return all_encoding.get(index)


class check_comparison(unittest.TestCase):
    def test_EMPTY(self):
        t = []
        self.assertTrue(isinstance(add_token(t), sa))

    def test_EQUALS_SIGN(self):
        t = [EQUALS_SIGN]
        self.assertTrue(isinstance(add_token(t), eq))

    def test_EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(isinstance(add_token(t), ne))

    def test_EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), lt))

    def test_EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK,
             GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), sn))

    def test_EQUALS_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), gt))

    def test_EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), ge))

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), sa))

    def test_EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), le))

    def test_EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK]
        self.assertTrue(isinstance(add_token(t), sn))

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), le))

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), eq))

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), ge))

    def test_GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), gt))

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), ne))

    def test_LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN]
        self.assertTrue(isinstance(add_token(t), lt))

    def testEQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        array = [
            EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN
        ]
        token = add_token(array)
        self.assertTrue(isinstance(token, sn))


if __name__ == '__main__':
    unittest.main()

