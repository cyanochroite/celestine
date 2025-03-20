""""""

import unittest

from celestine.application.viewer.parser.operator import (
    add,
    div,
    eq,
    ge,
    gt,
    le,
    lt,
    mul,
    ne,
    nn,
    nu,
    sub,
)
from celestine.application.viewer.parser.translator import (
    Comparison,
    Digit,
    Unary,
    parser,
    tokenizer,
)


def parse(token):
    """"""
    two = tokenizer.tokenize(token)
    three = parser.parse(two)
    return three[0]


class TestDigit(unittest.TestCase):
    """"""

    def test_new(self):
        """"""
        self.assertEqual(Digit.DIGIT_7, Digit.DIGIT_7)

    def test_newer(self):
        """"""
        self.assertEqual(Digit.DIGIT_7, Digit.DIGIT_7)


class TestUnary(unittest.TestCase):
    """"""

    def test_add_primary(self):
        """"""
        token = [Unary.PLUS]
        self.assertEqual(parse(token), add)

    def test_div_primary(self):
        """"""
        token = [Unary.STAR, Unary.DASH]
        self.assertEqual(parse(token), div)

    def test_div_secondary(self):
        """"""
        token = [Unary.STAR, Unary.DASH, Unary.PLUS]
        self.assertEqual(parse(token), div)

    def test_mul_primary(self):
        """"""
        token = [Unary.STAR]
        self.assertEqual(parse(token), mul)

    def test_mul_secondary(self):
        """"""
        token = [Unary.STAR, Unary.PLUS]
        self.assertEqual(parse(token), mul)

    def test_sub_primary(self):
        """"""
        token = [Unary.DASH]
        self.assertEqual(parse(token), sub)

    def test_sub_secondary(self):
        """"""
        token = [Unary.DASH, Unary.PLUS]
        self.assertEqual(parse(token), sub)


class TestComparison(unittest.TestCase):
    """"""

    def test_eq_primary(self):
        """"""
        token = [Comparison.SAME]
        self.assertEqual(parse(token), eq)

    def test_eq_secondary(self):
        """"""
        token = [Comparison.MARK, Comparison.MORE, Comparison.LESS]
        self.assertEqual(parse(token), eq)

    def test_ge_primary(self):
        """"""
        token = [Comparison.SAME, Comparison.MORE]
        self.assertEqual(parse(token), ge)

    def test_ge_secondary(self):
        """"""
        token = [Comparison.MARK, Comparison.LESS]
        self.assertEqual(parse(token), ge)

    def test_gt_primary(self):
        """"""
        token = [Comparison.MORE]
        self.assertEqual(parse(token), gt)

    def test_gt_secondary(self):
        """"""
        token = [Comparison.SAME, Comparison.MARK, Comparison.LESS]
        self.assertEqual(parse(token), gt)

    def test_le_primary(self):
        """"""
        token = [Comparison.SAME, Comparison.LESS]
        self.assertEqual(parse(token), le)

    def test_le_secondary(self):
        """"""
        token = [Comparison.MARK, Comparison.MORE]
        self.assertEqual(parse(token), le)

    def test_lt_primary(self):
        """"""
        token = [Comparison.LESS]
        self.assertEqual(parse(token), lt)

    def test_lt_secondary(self):
        """"""
        token = [Comparison.SAME, Comparison.MARK, Comparison.MORE]
        self.assertEqual(parse(token), lt)

    def test_ne_primary(self):
        """"""
        token = [Comparison.SAME, Comparison.MARK]
        self.assertEqual(parse(token), ne)

    def test_ne_secondary(self):
        """"""
        token = [Comparison.MORE, Comparison.LESS]
        self.assertEqual(parse(token), ne)

    def test_nn_primary(self):
        """"""
        token = [Comparison.MARK]
        self.assertEqual(parse(token), nn)

    def test_nn_secondary(self):
        """"""
        token = [
            Comparison.SAME,
            Comparison.MARK,
            Comparison.MORE,
            Comparison.LESS,
        ]
        self.assertEqual(parse(token), nn)

    def test_nu_secondary(self):
        """"""
        token = [Comparison.SAME, Comparison.MORE, Comparison.LESS]
        self.assertEqual(parse(token), nu)

    def test_strings(self):
        """"""
        self.assertEqual(str(eq), "=")
        self.assertEqual(repr(eq), "<Operator.EQ: '='>")
