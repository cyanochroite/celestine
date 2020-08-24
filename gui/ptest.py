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
    gt = 5


invert_encoding = {
    enum_comparison.lt: enum_comparison.ge,
    enum_comparison.le: enum_comparison.gt,
    enum_comparison.eq: enum_comparison.ne,
    enum_comparison.ne: enum_comparison.eq,
    enum_comparison.ge: enum_comparison.lt,
    enum_comparison.gt: enum_comparison.le
}
    enum_comparison.le: str().join([LESS_THAN_SIGN, EQUALS_SIGN]),
    enum_comparison.eq: str().join([EQUALS_SIGN, EQUALS_SIGN]),
    enum_comparison.ne: str().join([EXCLAMATION_MARK, EQUALS_SIGN]),
    enum_comparison.ge: str().join([GREATER_THAN_SIGN, EQUALS_SIGN]),
    enum_comparison.gt: str().join([GREATER_THAN_SIGN])
}


def add_token(array):
    a = array.count(EXCLAMATION_MARK)
    b = array.count(LESS_THAN_SIGN)
    c = array.count(EQUALS_SIGN)
    d = array.count(LESS_THAN_SIGN)
    print(a, b, c, d)
    invert = a % 2

    symbol = None

    e = d - b
    if c <= 0:
        if e > 0:
            symbol = enum_comparison.lt
        elif e < 0:
            symbol = enum_comparison.gt
        else:
            symbol = enum_comparison.ne
    else:
        if e > 0:
            symbol = enum_comparison.le
        elif e < 0:
            symbol = enum_comparison.ge
        else:
            symbol = enum_comparison.eq

    if invert:
        symbol = invert_encoding[symbol]

    symbol = final_encoding[symbol]
    print(symbol)
    return symbol
    return str()

    if "<" in array:
        return "<"

    if ">" in array:
        return "<"

    if "!" in array:
        return "!="

    value = str().join(array)
    hold = []
    start = False
    end = False
    for character in value:
        start = character is not LOW_LINE
        end |= start
        if end:
            hold.append(character)

    value = str().join(hold)
    return value


class check_comparison(unittest.TestCase):

    def setUp(self):
        self.NULL = str()
        self.empty = str()
        self.lt = str().join([LESS_THAN_SIGN])
        self.le = str().join([LESS_THAN_SIGN, EQUALS_SIGN])
        self.eq = str().join([EQUALS_SIGN, EQUALS_SIGN])
        self.ne = str().join([EXCLAMATION_MARK, EQUALS_SIGN])
        self.ge = str().join([GREATER_THAN_SIGN, EQUALS_SIGN])
        self.gt = str().join([GREATER_THAN_SIGN])

    def tearDown(self):
        self.empty = None
        self.lt = None
        self.le = None
        self.eq = None
        self.ne = None
        self.ge = None
        self.gt = None

    def test_empty(self):
        t = []
        self.assertTrue(add_token(t) == self.empty)

    def test_EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EXCLAMATION_MARK__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK, EXCLAMATION_MARK, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EXCLAMATION_MARK__EQUALS_SIGN(self):
        t = [EXCLAMATION_MARK, EXCLAMATION_MARK, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN__EQUALS_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EQUALS_SIGN(self):
        t = [EXCLAMATION_MARK, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK, EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EQUALS_SIGN__EQUALS_SIGN(self):
        t = [EXCLAMATION_MARK, EQUALS_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN__EQUALS_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.lt)

    def test_LESS_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [LESS_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EXCLAMATION_MARK__EXCLAMATION_MARK(self):
        t = [LESS_THAN_SIGN, EXCLAMATION_MARK, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EXCLAMATION_MARK__EQUALS_SIGN(self):
        t = [LESS_THAN_SIGN, EXCLAMATION_MARK, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__LESS_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [LESS_THAN_SIGN, LESS_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__LESS_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, LESS_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__LESS_THAN_SIGN__EQUALS_SIGN(self):
        t = [LESS_THAN_SIGN, LESS_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__LESS_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, LESS_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EQUALS_SIGN(self):
        t = [LESS_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [LESS_THAN_SIGN, EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EQUALS_SIGN__EQUALS_SIGN(self):
        t = [LESS_THAN_SIGN, EQUALS_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__GREATER_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [LESS_THAN_SIGN, GREATER_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__GREATER_THAN_SIGN__EQUALS_SIGN(self):
        t = [LESS_THAN_SIGN, GREATER_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_LESS_THAN_SIGN__GREATER_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, GREATER_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN(self):
        t = [EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.eq)

    def test_EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.ne)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.eq)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.gt)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__EQUALS_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__LESS_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__LESS_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__LESS_THAN_SIGN__EQUALS_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__LESS_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__EQUALS_SIGN(self):
        t = [EQUALS_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__EQUALS_SIGN__EQUALS_SIGN(self):
        t = [EQUALS_SIGN, EQUALS_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__EQUALS_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_EQUALS_SIGN__GREATER_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.gt)

    def test_GREATER_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [GREATER_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EXCLAMATION_MARK__EXCLAMATION_MARK(self):
        t = [GREATER_THAN_SIGN, EXCLAMATION_MARK, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EXCLAMATION_MARK__EQUALS_SIGN(self):
        t = [GREATER_THAN_SIGN, EXCLAMATION_MARK, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN__EQUALS_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EQUALS_SIGN(self):
        t = [GREATER_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [GREATER_THAN_SIGN, EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EQUALS_SIGN__EQUALS_SIGN(self):
        t = [GREATER_THAN_SIGN, EQUALS_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__GREATER_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [GREATER_THAN_SIGN, GREATER_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__GREATER_THAN_SIGN__EQUALS_SIGN(self):
        t = [GREATER_THAN_SIGN, GREATER_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(add_token(t) == self.NULL)

    def test_GREATER_THAN_SIGN__GREATER_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, GREATER_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(add_token(t) == self.NULL)


def make():
    array = ["EXCLAMATION_MARK", "LESS_THAN_SIGN",
             "EQUALS_SIGN", "GREATER_THAN_SIGN"]
    for a in array:
        print("def test_" + a + "(self):")
        print("    t = [" + a + "]")
        print("    self.assertTrue(add_token(t)) == self.None")
        for b in array:
            print("def test_" + a + "__" + b + "(self):")
            print("    t = [" + a + ", " + b + "]")
            print("    self.assertTrue(add_token(t)) == self.None")
            for c in array:
                print("def test_" + a + "__" + b + "__" + c + "(self):")
                print("    t = [" + a + ", " + b + ", " + c + "]")
                print("    self.assertTrue(add_token(t)) == self.None")


if __name__ == '__main__':
    unittest.main()
    # make()
