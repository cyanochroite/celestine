# coding=utf-8
import unittest

from mem_dixy.tag.alphabet import logical
from mem_dixy.Unicode.U0000 import *


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("hi")
        # self.widget = Widget('The widget')

    def tearDown(self):
        print("bye")
        # self.widget.dispose()

    def test_upper(self):
        add_token("H")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


def parse(string):
    is_letter = False
    was_letter = False
    is_comparison = False
    was_comparison = False
    for character in bird:
        was_letter = is_letter
        is_letter = character in letter
        if was_letter and not is_letter:
            add_token()

        was_comparison = is_comparison
        is_comparison = character in comparison
        if was_comparison and not is_comparison:
            add_token()

        if character in all_token:
            tigger.append(character)

        if character in one_token:
            add_token()


def add_token(array):
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
        self.assertTrue(self.empty == add_token([]))

    def test_EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK]
        self.assertTrue(self.empty == add_token(t))

    def test_EXCLAMATION_MARK__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK, EXCLAMATION_MARK]
        self.assertTrue(self.empty == add_token(t))

    def test_EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_EXCLAMATION_MARK__EQUALS_SIGN(self):
        t = [EXCLAMATION_MARK, EQUALS_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_LESS_THAN_SIGN__EXCLAMATION_MARK(self):
        t = [LESS_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(self.empty == add_token(t))

    def test_LESS_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_LESS_THAN_SIGN__EQUALS_SIGN(self):
        t = [LESS_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_LESS_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [LESS_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_EQUALS_SIGN(self):
        t = [EQUALS_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertTrue(self.empty == add_token(t))

    def test_EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_EQUALS_SIGN__EQUALS_SIGN(self):
        t = [EQUALS_SIGN, EQUALS_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_GREATER_THAN_SIGNK__EXCLAMATION_MARK(self):
        t = [GREATER_THAN_SIGN, EXCLAMATION_MARK]
        self.assertTrue(self.empty == add_token(t))

    def test_GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_GREATER_THAN_SIGN__EQUALS_SIGN(self):
        t = [GREATER_THAN_SIGN, EQUALS_SIGN]
        self.assertTrue(self.empty == add_token(t))

    def test_GREATER_THAN_SIGN__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, GREATER_THAN_SIGN]
        self.assertTrue(self.empty == add_token(t))


if __name__ == '__main__':
    unittest.main()


[EXCLAMATION_MARK]
[EXCLAMATION_MARK, EXCLAMATION_MARK]
[EXCLAMATION_MARK, LESS_THAN_SIGN]
[EXCLAMATION_MARK, EQUALS_SIGN]
[EXCLAMATION_MARK, GREATER_THAN_SIGN]

[LESS_THAN_SIGN]
[LESS_THAN_SIGN, EXCLAMATION_MARK]
[LESS_THAN_SIGN, LESS_THAN_SIGN]
[LESS_THAN_SIGN, EQUALS_SIGN]
[LESS_THAN_SIGN, GREATER_THAN_SIGN]

[EQUALS_SIGN]
[EQUALS_SIGN, EXCLAMATION_MARK]
[EQUALS_SIGN, LESS_THAN_SIGN]
[EQUALS_SIGN, EQUALS_SIGN]
[EQUALS_SIGN, GREATER_THAN_SIGN]

[GREATER_THAN_SIGN]
[GREATER_THAN_SIGN, EXCLAMATION_MARK]
[GREATER_THAN_SIGN, LESS_THAN_SIGN]
[GREATER_THAN_SIGN, EQUALS_SIGN]
[GREATER_THAN_SIGN, GREATER_THAN_SIGN]


