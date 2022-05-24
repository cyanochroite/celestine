import unittest

from celestine.parser.translator import *


class test_translator(unittest.TestCase):
    def test_translate(self):
        string = "cat hat"
        expect = [
            Letter.LETTER_C,
            Letter.LETTER_A,
            Letter.LETTER_T,
            Divider.WHITESPACE,
            Letter.LETTER_H,
            Letter.LETTER_A,
            Letter.LETTER_T
        ]
        result = translator.translate(string)
        self.assertEqual(expect, result)
