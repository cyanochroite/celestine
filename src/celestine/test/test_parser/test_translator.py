import unittest

from celestine.parser.translator import *
from celestine.parser.operator import *


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

    def test_translate_not_defined(self):
        string = "(x)"
        expect = [
            Letter.LETTER_X
        ]
        result = translator.translate(string)
        self.assertEqual(expect, result)

    def test_translate_not_implemented(self):
        string = "xⶀx"
        expect = [
            Letter.LETTER_X,
            Letter.LETTER_X
        ]
        result = translator.translate(string)
        self.assertEqual(expect, result)

    def test_one(self):
        string = "ⶀ<>0#h i35 <m o7cat  $&dog"
        expect = [
            Comparison.LESS,
            Comparison.MORE,
            Digit.DIGIT_0,
            Letter.LETTER_H,
            Divider.WHITESPACE,
            Letter.LETTER_I,
            Digit.DIGIT_3,
            Digit.DIGIT_5,
            Divider.WHITESPACE,
            Comparison.LESS,
            Letter.LETTER_M,
            Divider.WHITESPACE,
            Letter.LETTER_O,
            Digit.DIGIT_7,
            Letter.LETTER_C,
            Letter.LETTER_A,
            Letter.LETTER_T,
            Divider.WHITESPACE,
            Divider.WHITESPACE,
            Letter.LETTER_D,
            Letter.LETTER_O,
            Letter.LETTER_G
        ]
        one = translator.translate(string)
        self.assertEqual(expect, one)

    def test_two(self):
        string = "ⶀ<>0#h i35 <m o7cat  $&dog"
        expect = [
            [
                Comparison.LESS,
                Comparison.MORE
            ],
            [
                Digit.DIGIT_0
            ],
            [
                Letter.LETTER_H
            ],
            [
                Divider.WHITESPACE
            ],
            [
                Letter.LETTER_I
            ],
            [
                Digit.DIGIT_3,
                Digit.DIGIT_5
            ],
            [
                Divider.WHITESPACE
            ],
            [
                Comparison.LESS
            ],
            [
                Letter.LETTER_M
            ],
            [
                Divider.WHITESPACE
            ],
            [
                Letter.LETTER_O
            ],
            [
                Digit.DIGIT_7
            ],
            [
                Letter.LETTER_C	,
                Letter.LETTER_A	,
                Letter.LETTER_T
            ],
            [
                Divider.WHITESPACE,
                Divider.WHITESPACE
            ],
            [
                Letter.LETTER_D	,
                Letter.LETTER_O	,
                Letter.LETTER_G
            ]
        ]
        one = translator.translate(string)
        two = tokenizer.tokenize(one)
        self.assertEqual(expect, two)

    def test_three(self):
        string = "ⶀ<>0#h i35 <m o7cat  $&dog"
        expect = [
            ne,
            number("0"),
            word("h"),
            tab(""),
            word("i"),
            number("35"),
            tab(""),
            lt,
            word("m"),
            tab(""),
            word("o"),
            number("7"),
            word("cat"),
            tab(""),
            word("dog")
        ]
#        [<OPERATOR.NE: '!='>, <OPERATOR.NUMBER: '0'>, <OPERATOR.WORD: 'h'>, <OPERATOR.TAB: ' '>, <OPERATOR.WORD: 'i'>, <OPERATOR.NUMBER: '35'>, <OPERATOR.TAB: ' '>, <OPERATOR.LT: '<'>, <OPERATOR.WORD: 'm'>, <OPERATOR.TAB: ' '>, <OPERATOR.WORD: 'o'>, <OPERATOR.NUMBER: '5'>, <OPERATOR.WORD: 'cat'>, <OPERATOR.TAB: ' '>, <OPERATOR.WORD: 'dog'>]
        one = translator.translate(string)
        two = tokenizer.tokenize(one)
        three = parser.parse(two)
        self.assertEqual(expect, three)
