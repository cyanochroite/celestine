import unittest

from celestine.parser.operator import *
from celestine.data.alphabet import *


class test_digit(unittest.TestCase):
    def test_new(self):
        self.assertEqual(Digit.DIGIT_7, Digit.DIGIT_7)


class test_unary(unittest.TestCase):
    def test_add_primary(self):
        token = set(
            [
                Unary.PLUS
            ]
        )
        self.assertSetEqual(token, add.primary)
        self.assertEqual(unary_parse(token), add)

    def test_add_secondary(self):
        token = set(
            [
            ]
        )
        self.assertSetEqual(token, add.secondary)
        self.assertEqual(unary_parse(token), add)

    def test_div_primary(self):
        token = set(
            [
                Unary.STAR,
                Unary.DASH
            ]
        )
        self.assertSetEqual(token, div.primary)
        self.assertEqual(unary_parse(token), div)

    def test_div_secondary(self):
        token = set(
            [
                Unary.STAR,
                Unary.DASH,
                Unary.PLUS
            ]
        )
        self.assertSetEqual(token, div.secondary)
        self.assertEqual(unary_parse(token), div)

    def test_mul_primary(self):
        token = set(
            [
                Unary.STAR
            ]
        )
        self.assertSetEqual(token, mul.primary)
        self.assertEqual(unary_parse(token), mul)

    def test_mul_secondary(self):
        token = set(
            [
                Unary.STAR,
                Unary.PLUS
            ]
        )
        self.assertSetEqual(token, mul.secondary)
        self.assertEqual(unary_parse(token), mul)

    def test_sub_primary(self):
        token = set(
            [
                Unary.DASH
            ]
        )
        self.assertSetEqual(token, sub.primary)
        self.assertEqual(unary_parse(token), sub)

    def test_sub_secondary(self):
        token = set(
            [
                Unary.DASH,
                Unary.PLUS
            ]
        )
        self.assertSetEqual(token, sub.secondary)
        self.assertEqual(unary_parse(token), sub)


class test_comparison(unittest.TestCase):
    def test_eq_primary(self):
        token = set(
            [
                Comparison.SAME
            ]
        )
        self.assertSetEqual(token, eq.primary)
        self.assertEqual(comparison_parse(token), eq)

    def test_eq_secondary(self):
        token = set(
            [
                Comparison.MARK,
                Comparison.MORE,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, eq.secondary)
        self.assertEqual(comparison_parse(token), eq)

    def test_ge_primary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.MORE
            ]
        )
        self.assertSetEqual(token, ge.primary)
        self.assertEqual(comparison_parse(token), ge)

    def test_ge_secondary(self):
        token = set(
            [
                Comparison.MARK,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, ge.secondary)
        self.assertEqual(comparison_parse(token), ge)

    def test_gt_primary(self):
        token = set(
            [
                Comparison.MORE
            ]
        )
        self.assertSetEqual(token, gt.primary)
        self.assertEqual(comparison_parse(token), gt)

    def test_gt_secondary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.MARK,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, gt.secondary)
        self.assertEqual(comparison_parse(token), gt)

    def test_le_primary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, le.primary)
        self.assertEqual(comparison_parse(token), le)

    def test_le_secondary(self):
        token = set(
            [
                Comparison.MARK,
                Comparison.MORE
            ]
        )
        self.assertSetEqual(token, le.secondary)
        self.assertEqual(comparison_parse(token), le)

    def test_lt_primary(self):
        token = set(
            [
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, lt.primary)
        self.assertEqual(comparison_parse(token), lt)

    def test_lt_secondary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.MARK,
                Comparison.MORE
            ]
        )
        self.assertSetEqual(token, lt.secondary)
        self.assertEqual(comparison_parse(token), lt)

    def test_ne_primary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.MARK
            ]
        )
        self.assertSetEqual(token, ne.primary)
        self.assertEqual(comparison_parse(token), ne)

    def test_ne_secondary(self):
        token = set(
            [
                Comparison.MORE,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, ne.secondary)
        self.assertEqual(comparison_parse(token), ne)

    def test_nn_primary(self):
        token = set(
            [
                Comparison.MARK
            ]
        )
        self.assertSetEqual(token, nn.primary)
        self.assertEqual(comparison_parse(token), nn)

    def test_nn_secondary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.MARK,
                Comparison.MORE,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, nn.secondary)
        self.assertEqual(comparison_parse(token), nn)

    def test_nu_primary(self):
        token = set(
            [
            ]
        )
        self.assertSetEqual(token, nu.primary)
        self.assertEqual(comparison_parse(token), nu)

    def test_nu_secondary(self):
        token = set(
            [
                Comparison.SAME,
                Comparison.MORE,
                Comparison.LESS
            ]
        )
        self.assertSetEqual(token, nu.secondary)
        self.assertEqual(comparison_parse(token), nu)
