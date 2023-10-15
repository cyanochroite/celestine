""""""

import unittest

from celestine.window.point import (
    Point,
    Line,
)


class TestPoint(unittest.TestCase):
    """"""

    def test_clone(self):
        """"""
        one = Point(4, 3)
        point = Point.clone(one)

        self.assertEqual(point.one, 4)
        self.assertEqual(point.two, 3)

    def test_copy(self):
        """"""
        one = Point(4, 3)
        point = one.copy()

        self.assertEqual(point.one, 4)
        self.assertEqual(point.two, 3)

    def test_init(self):
        """"""
        point = Point(-4, -8)
        self.assertEqual(point.one, -4)
        self.assertEqual(point.two, -8)

    def test_iter(self):
        """"""
        point = Point(1, 2)
        items = iter(point)
        self.assertEqual(next(items), 1)
        self.assertEqual(next(items), 2)

    def test_repr(self):
        """"""
        point = Point(-3, -4)
        string = repr(point)
        self.assertEqual(string, "Point(-3, -4)")

    def test_str(self):
        """"""
        point = Point(-3, -4)
        string = str(point)
        self.assertEqual(string, "(-3, -4)")

    def test_sub(self):
        """"""
        one = Point(1, 2)
        two = Point(3, 5)
        point = one - two

        self.assertEqual(point.one, -2)
        self.assertEqual(point.two, -3)

    def test_truediv(self):
        """"""
        one = Point(12, 6)
        two = Point(3, 2)
        point = one / two

        self.assertEqual(point.one, 4)
        self.assertEqual(point.two, 3)


class TestLine(unittest.TestCase):
    """"""

    def test_clone(self):
        """"""
        one = Line(3, 4)
        line = Line.clone(one)

        self.assertEqual(line.minimum, 3)
        self.assertEqual(line.maximum, 4)

    def test_copy(self):
        """"""
        one = Line(4, 3)
        line = one.copy()

        self.assertEqual(line.minimum, 3)
        self.assertEqual(line.maximum, 4)

    def test_length(self):
        """"""
        line = Line(-7, 3)
        length = line.length

        self.assertEqual(length, 10)

    def test_midpoint(self):
        """"""
        line = Line(1, 5)
        midpoint = line.midpoint

        self.assertEqual(midpoint, 3)

    def test_add(self):
        """"""
        one = Line(1, 2)
        two = 3
        line = one + two

        self.assertEqual(line.minimum, 4)
        self.assertEqual(line.maximum, 5)

    def test_contains(self):
        """"""
        one = Line(1, 3)
        two = 2
        line = two in one

        self.assertTrue(line)

    def test_iadd(self):
        """"""
        one = Line(1, 2)
        two = 3
        one += two
        line = one

        self.assertEqual(line.minimum, 4)
        self.assertEqual(line.maximum, 5)

    def test_imul(self):
        """"""
        line = Line(1, 2)
        other = 3
        line *= other

        self.assertEqual(line.minimum, 3)
        self.assertEqual(line.maximum, 6)

    def test_init(self):
        """"""
        line = Line(-4, -8)
        self.assertEqual(line.minimum, -8)
        self.assertEqual(line.maximum, -4)

    def test_mul(self):
        """"""
        one = Line(1, 2)
        two = 3
        line = one * two

        self.assertEqual(line.minimum, 3)
        self.assertEqual(line.maximum, 6)

    def test_repr(self):
        """"""
        line = Line(3, 4)
        string = repr(line)
        self.assertEqual(string, "Line(3, 4)")

    def test_str(self):
        """"""
        line = Line(3, 4)
        string = str(line)
        self.assertEqual(string, "[3, 4]")
