""""""

import unittest

from celestine.typed import N
from celestine.window.cardinal import (
    Dyad,
    Math,
    Monad,
    Tetrad,
    Triad,
)


class TestMath(unittest.TestCase):
    """"""

    def test_arithmetic(self) -> N:
        """"""
        self.assertEqual(Math.add(1, 2), 3)
        self.assertEqual(Math.sub(5, 3), 2)
        self.assertEqual(Math.mul(2, 3), 6)
        self.assertEqual(Math.truediv(6, 2), 3)

    def test_rounding(self) -> N:
        """"""
        self.assertEqual(Math.ceil(1.5), 2)
        self.assertEqual(Math.floor(1.5), 1)
        self.assertEqual(Math.round(1.5), 2)
        self.assertEqual(Math.trunc(1.5), 1)


class TestCardinal(unittest.TestCase):
    """"""

    def test_arithmetic_operations(self) -> N:
        """"""
        c1 = Dyad(1.0, 2.0)
        c2 = Dyad(2.0, 3.0)

        self.assertEqual(float(c1 + c2), 8.0)
        self.assertEqual(float(c1 * c2), 8.0)
        self.assertEqual(float(-c1), -3.0)

    def test_binary(self) -> N:
        """"""
        item = Dyad(1, 2)
        one = 4
        two = (3, 5)
        tri = [7, 8, 9]
        tet = Tetrad(-4, -3, -2, -1)

        self.assertEqual((item + one).data, (5, 6))
        self.assertEqual((item + two).data, (4, 7))
        self.assertEqual((item + tri).data, (8, 10))
        self.assertEqual((item + tet).data, (-3, -1))

    def test_comparisons(self) -> N:
        """"""
        c1 = Dyad(1.0, 2.0)
        c2 = Dyad(2.0, 3.0)

        self.assertTrue(c1 < c2)
        self.assertFalse(c1 > c2)
        self.assertTrue(c1 <= c2)

    def test_conversions(self) -> N:
        """"""
        c = Dyad(1.5, 2.5)
        self.assertEqual(float(c), 4.0)
        self.assertEqual(float(c.ceil()), 5.0)
        self.assertEqual(float(c.floor()), 3.0)


class TestMonad(unittest.TestCase):
    """"""

    def test_initialization(self) -> N:
        """"""
        item = Monad(1)
        self.assertEqual(item.one, 1)
        self.assertEqual(item.data, (1,))

    def test_property_access(self) -> N:
        """"""
        item = Monad(+1)
        item.data = (-1,)
        self.assertEqual(item.one, -1)
        self.assertEqual(item.data, (-1,))

    def test_string_representation(self) -> N:
        """"""
        t = Monad(1)
        self.assertEqual(str(t), "(1)")
        self.assertEqual(repr(t), "Monad(1)")


class TestDyad(unittest.TestCase):
    """"""

    def test_initialization(self) -> N:
        """"""
        item = Dyad(1, 2)
        self.assertEqual(item.one, 1)
        self.assertEqual(item.two, 2)
        self.assertEqual(item.data, (1, 2))

    def test_property_access(self) -> N:
        """"""
        item = Dyad(+1, +2)
        item.data = (-1, -2)
        self.assertEqual(item.one, -1)
        self.assertEqual(item.two, -2)
        self.assertEqual(item.data, (-1, -2))

    def test_string_representation(self) -> N:
        """"""
        t = Dyad(1, 2)
        self.assertEqual(str(t), "(1, 2)")
        self.assertEqual(repr(t), "Dyad(1, 2)")


class TestTriad(unittest.TestCase):
    """"""

    def test_initialization(self) -> N:
        """"""
        item = Triad(1, 2, 3)
        self.assertEqual(item.one, 1)
        self.assertEqual(item.two, 2)
        self.assertEqual(item.tri, 3)
        self.assertEqual(item.data, (1, 2, 3))

    def test_property_access(self) -> N:
        """"""
        item = Triad(+1, +2, +3)
        item.data = (-1, -2, -3)
        self.assertEqual(item.one, -1)
        self.assertEqual(item.two, -2)
        self.assertEqual(item.tri, -3)
        self.assertEqual(item.data, (-1, -2, -3))

    def test_string_representation(self) -> N:
        """"""
        t = Triad(1, 2, 3)
        self.assertEqual(str(t), "(1, 2, 3)")
        self.assertEqual(repr(t), "Triad(1, 2, 3)")


class TestTetrad(unittest.TestCase):
    """"""

    def test_initialization(self) -> N:
        """"""
        item = Tetrad(1, 2, 3, 4)
        self.assertEqual(item.one, 1)
        self.assertEqual(item.two, 2)
        self.assertEqual(item.tri, 3)
        self.assertEqual(item.tet, 4)
        self.assertEqual(item.data, (1, 2, 3, 4))

    def test_property_access(self) -> N:
        """"""
        item = Tetrad(+1, +2, +3, +4)
        item.data = (-1, -2, -3, -4)
        self.assertEqual(item.one, -1)
        self.assertEqual(item.two, -2)
        self.assertEqual(item.tri, -3)
        self.assertEqual(item.tet, -4)
        self.assertEqual(item.data, (-1, -2, -3, -4))

    def test_string_representation(self) -> N:
        """"""
        t = Tetrad(1, 2, 3, 4)
        self.assertEqual(str(t), "(1, 2, 3, 4)")
        self.assertEqual(repr(t), "Tetrad(1, 2, 3, 4)")
