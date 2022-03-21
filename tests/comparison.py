import unittest
import sys
sys.path.insert(1, '../src/gui')


from mem_dixy.tag.comparison import *


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
