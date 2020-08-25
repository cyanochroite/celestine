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
    al = 6,
    no = 7


final_encoding = {
    enum_comparison.lt: str().join([LESS_THAN_SIGN]),
    enum_comparison.le: str().join([LESS_THAN_SIGN, EQUALS_SIGN]),
    enum_comparison.eq: str().join([EQUALS_SIGN, EQUALS_SIGN]),
    enum_comparison.ne: str().join([EXCLAMATION_MARK, EQUALS_SIGN]),
    enum_comparison.ge: str().join([GREATER_THAN_SIGN, EQUALS_SIGN]),
    enum_comparison.gt: str().join([GREATER_THAN_SIGN]),
    enum_comparison.al: "?",
    enum_comparison.no: "~"
}


all_encoding = {
    0x0: enum_comparison.eq,  # ____
    0x1: enum_comparison.gt,  # ___>
    0x2: enum_comparison.eq,  # __=_
    0x3: enum_comparison.ge,  # __=>
    0x4: enum_comparison.lt,  # _<__
    0x5: enum_comparison.ne,  # _<_>
    0x6: enum_comparison.le,  # _<=_
    0x7: enum_comparison.al,  # _<=>
    0x8: enum_comparison.ne,  # !___
    0x9: enum_comparison.le,  # !__>
    0xA: enum_comparison.ne,  # !_=_
    0xB: enum_comparison.lt,  # !_=>
    0xC: enum_comparison.ge,  # !<__
    0xD: enum_comparison.eq,  # !<_>
    0xE: enum_comparison.gt,  # !<=_
    0xF: enum_comparison.no,  # !<=>
    128: enum_comparison.lt
}


def add_token(array):
    a = EXCLAMATION_MARK in array
    b = LESS_THAN_SIGN in array
    c = EQUALS_SIGN in array
    d = GREATER_THAN_SIGN in array
    a = 8 if a else 0
    b = 4 if b else 0
    c = 2 if c else 0
    d = 1 if d else 0
    e = a + b + c + d
    f = all_encoding.get(e)
    g = final_encoding.get(f)
    return g


class check_comparison(unittest.TestCase):

    def setUp(self):
        self.NULL = 42
        self.empty = str()
        self.lt = str().join([LESS_THAN_SIGN])
        self.le = str().join([LESS_THAN_SIGN, EQUALS_SIGN])
        self.eq = str().join([EQUALS_SIGN, EQUALS_SIGN])
        self.ne = str().join([EXCLAMATION_MARK, EQUALS_SIGN])
        self.ge = str().join([GREATER_THAN_SIGN, EQUALS_SIGN])
        self.gt = str().join([GREATER_THAN_SIGN])
        self.al = "?"
        self.no = "~"

    def tearDown(self):
        self.empty = None
        self.lt = None
        self.le = None
        self.eq = None
        self.ne = None
        self.ge = None
        self.gt = None

    def test_EMPTY(self):
        t = []
        self.assertTrue(add_token(t) == self.eq)

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
        self.assertTrue(add_token(t) == self.no)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.gt)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.ge)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.al)

    def test_EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.le)

    def test_EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.ne)

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


