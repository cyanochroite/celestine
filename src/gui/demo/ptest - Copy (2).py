# coding=utf-8
import unittest

from mem_dixy.tag.alphabet import logical
from mem_dixy.Unicode.U0000 import *


from enum import Enum


class enum_comparison(Enum):
    lt = 0,
    le = 1,
    eq = 2,
    ne = 3,
    ge = 4,
    gt = 5,
    sa = 6,
    sn = 7


class operator():
    pass


class comparison(operator):
    def __init__(self, symbol):
        this.symbol, = symbol

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
    0x0: enum_comparison.sa,  # ____
    0x1: enum_comparison.gt,  # ___>
    0x2: enum_comparison.eq,  # __=_
    0x3: enum_comparison.ge,  # __=>
    0x4: enum_comparison.lt,  # _<__
    0x5: enum_comparison.ne,  # _<_>
    0x6: enum_comparison.le,  # _<=_
    0x7: enum_comparison.sa,  # _<=>
    0x8: enum_comparison.sn,  # !___
    0x9: enum_comparison.le,  # !__>
    0xA: enum_comparison.ne,  # !_=_
    0xB: enum_comparison.lt,  # !_=>
    0xC: enum_comparison.ge,  # !<__
    0xD: enum_comparison.eq,  # !<_>
    0xE: enum_comparison.gt,  # !<=_
    0xF: enum_comparison.sn,  # !<=>
    128: enum_comparison.lt
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
    def setUp(self):
        self.lt = enum_comparison.lt
        self.le = enum_comparison.le
        self.eq = enum_comparison.eq
        self.ne = enum_comparison.ne
        self.ge = enum_comparison.ge
        self.gt = enum_comparison.gt
        self.sa = enum_comparison.sa
        self.sn = enum_comparison.sn

    def tearDown(self):
        self.lt = None
        self.le = None
        self.eq = None
        self.ne = None
        self.ge = None
        self.gt = None
        self.sa = None
        self.sn = None

    def test_EMPTY(self):
        t = []
        self.assertTrue(add_token(t) == self.sa)

    def test_EQUALS_SIGN(self):
        t = [EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.eq)

    def test_EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.ne)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.lt)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK,
             GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.sn)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.gt)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.ge)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.sa)

    def test_EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.le)

    def test_EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.sn)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.le)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.eq)

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.ge)

    def test_GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.gt)

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.ne)

    def test_LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.lt)


def make():
    array = ["EXCLAMATION_MARK", "LESS_THAN_SIGN",
             "EQUALS_SIGN", "GREATER_THAN_SIGN"]
    array = ["EQUALS_SIGN", "EXCLAMATION_MARK",
             "GREATER_THAN_SIGN", "LESS_THAN_SIGN"]
    for a in array:
        print("def test_" + a + "(self):")
        print("    t = [" + a + "]")
        print("    self.assertTrue(add_token(t) == self.NULL)")
        for b in array:
            print("def test_" + a + "__" + b + "(self):")
            print("    t = [" + a + ", " + b + "]")
            print("    self.assertTrue(add_token(t) == self.NULL)")
            for c in array:
                print("def test_" + a + "__" + b + "__" + c + "(self):")
                print("    t = [" + a + ", " + b + ", " + c + "]")
                print("    self.assertTrue(add_token(t) == self.NULL)")


def function(array):
    one = ""
    two = ""
    first = True
    for item in array:
        if not first:
            one += "__"
            two += ", "
        one += item
        two += item
        first = False
    print("def test_" + one + "(self):")
    print("    t = [" + two + "]")
    print("    self.assertTrue(add_token(t) == self.NULL)")


def make2():
    array = [False, True]
    for a in array:
        for b in array:
            for c in array:
                for d in array:
                    e = []
                    if a:
                        e.append("EQUALS_SIGN")
                    if b:
                        e.append("EXCLAMATION_MARK")
                    if c:
                        e.append("GREATER_THAN_SIGN")
                    if d:
                        e.append("LESS_THAN_SIGN")
                    function(e)


if __name__ == '__main__':
    unittest.main()
    # make()
    # make2()


