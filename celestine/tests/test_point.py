""""""

import unittest

from celestine.window.collection import (
    Grid,
    Line,
    Plane,
    Point,
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

    def test_quantize(self):
        """"""
        point = Point(3.4, 3.5)
        point.quantize()

        self.assertEqual(point.one, 3)
        self.assertEqual(point.two, 4)

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
        self.assertEqual(string, "Point(-3.0, -4.0)")

    def test_str(self):
        """"""
        point = Point(-3, -4)
        string = str(point)
        self.assertEqual(string, "(-3.0, -4.0)")

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

    def test_quantize(self):
        """"""
        line = Line(3.4, 3.5)
        line.quantize()

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
        self.assertEqual(string, "Line(3.0, 4.0)")

    def test_str(self):
        """"""
        line = Line(3, 4)
        string = str(line)
        self.assertEqual(string, "[3.0, 4.0]")


class TestPlane(unittest.TestCase):
    """"""

    def test_center(self):
        """"""
        one = Plane.make(32, 64)
        plane = Plane.make(16, 16)
        plane.center(one)

        self.assertEqual(plane.one.minimum, 8.0)
        self.assertEqual(plane.one.maximum, 24.0)
        self.assertEqual(plane.two.minimum, 24.0)
        self.assertEqual(plane.two.maximum, 40.0)

    def test_centroid(self):
        """"""
        plane = Plane(Line(5, 15), Line(15, 25))
        centroid = plane.centroid

        point = Point(10.0, 20.0)
        self.assertEqual(str(point), str(centroid))

    def test_clone(self):
        """"""
        one = Plane(Line(1, 2), Line(3, 4))
        two = Plane.clone(one)

        self.assertEqual(str(one), str(two))

    def test_copy(self):
        """"""
        one = Plane(Line(1, 2), Line(3, 4))
        two = one.copy()

        self.assertEqual(str(one), str(two))

    def test_make(self):
        """"""
        plane = Plane.make(4, 5)

        self.assertEqual(plane.one.minimum, 0)
        self.assertEqual(plane.one.maximum, 4)
        self.assertEqual(plane.two.minimum, 0)
        self.assertEqual(plane.two.maximum, 5)

    def test_scale_to_max(self):
        """"""
        one = Plane.make(32, 64)
        plane = Plane.make(16, 16)
        plane.scale_to_max(one)

        self.assertEqual(plane.one.minimum, 0)
        self.assertEqual(plane.one.maximum, 64)
        self.assertEqual(plane.two.minimum, 0)
        self.assertEqual(plane.two.maximum, 64)

    def test_scale_to_min(self):
        """"""
        one = Plane.make(32, 64)
        plane = Plane.make(16, 16)
        plane.scale_to_min(one)

        self.assertEqual(plane.one.minimum, 0)
        self.assertEqual(plane.one.maximum, 32)
        self.assertEqual(plane.two.minimum, 0)
        self.assertEqual(plane.two.maximum, 32)

    def test_quantize(self):
        """"""
        one = Line(-3.6, -3.4)
        two = Line(+3.4, +3.6)
        plane = Plane(one, two)
        plane.quantize()

        self.assertEqual(plane.one.minimum, -4)
        self.assertEqual(plane.one.maximum, -3)
        self.assertEqual(plane.two.minimum, +3)
        self.assertEqual(plane.two.maximum, +4)

    def test_size(self):
        """"""
        plane = Plane(Line(1, 2), Line(3, 4))
        size = plane.size
        point = Point(1, 1)

        self.assertEqual(str(point), str(size))

    def test_add(self):
        """"""
        one = Plane(Line(1, 2), Line(3, 4))
        plane = one + Point(2, 4)

        self.assertEqual(plane.one.minimum, 3)
        self.assertEqual(plane.one.maximum, 4)
        self.assertEqual(plane.two.minimum, 7)
        self.assertEqual(plane.two.maximum, 8)

    def test_contains(self):
        """"""
        one = Line(1, 3)
        two = 2
        line = two in one

        self.assertTrue(line)

        one = Plane(Line(2, 4), Line(6, 8))
        two = Point(3, 7)
        contains = two in one

        self.assertTrue(contains)

    def test_iadd(self):
        """"""
        plane = Plane(Line(1, 2), Line(3, 4))
        plane += Point(2, 4)

        self.assertEqual(plane.one.minimum, 3)
        self.assertEqual(plane.one.maximum, 4)
        self.assertEqual(plane.two.minimum, 7)
        self.assertEqual(plane.two.maximum, 8)

    def test_imul(self):
        """"""
        plane = Plane(Line(1, 2), Line(3, 4))
        plane *= 4

        self.assertEqual(plane.one.minimum, 4)
        self.assertEqual(plane.one.maximum, 8)
        self.assertEqual(plane.two.minimum, 12)
        self.assertEqual(plane.two.maximum, 16)

    def test_init(self):
        """"""
        plane = Plane(Line(1, 2), Line(3, 4))

        self.assertEqual(plane.one.minimum, 1)
        self.assertEqual(plane.one.maximum, 2)
        self.assertEqual(plane.two.minimum, 3)
        self.assertEqual(plane.two.maximum, 4)

    def test_mul(self):
        """"""
        one = Plane(Line(1, 2), Line(3, 4))
        two = one * 4
        plane = two

        self.assertEqual(plane.one.minimum, 4)
        self.assertEqual(plane.one.maximum, 8)
        self.assertEqual(plane.two.minimum, 12)
        self.assertEqual(plane.two.maximum, 16)

    def test_repr(self):
        """"""
        plane = Plane(Line(1, 2), Line(3, 4))
        string = "Plane(Line(1.0, 2.0), Line(3.0, 4.0))"
        self.assertEqual(string, repr(plane))

    def test_str(self):
        """"""
        plane = Plane(Line(1, 2), Line(3, 4))
        string = str(plane)
        self.assertEqual(string, "([1.0, 2.0], [3.0, 4.0])")


class TestGrid(unittest.TestCase):
    """"""

    def test_centroid(self):
        """"""
        grid = Grid(Line(1.0, 2.0), Line(1.0, 3.0))

        point = Point(2, 2)
        point.quantize()
        centroid = grid.centroid

        self.assertEqual(str(point), str(centroid))

    def test_scale_to_max(self):
        """"""
        plane = Plane.make(33.33, 66.66)
        grid = Grid.make(16, 16)
        grid.scale_to_max(plane)

        self.assertEqual(grid.one.minimum, 0)
        self.assertEqual(grid.one.maximum, 67)
        self.assertEqual(grid.two.minimum, 0)
        self.assertEqual(grid.two.maximum, 67)

    def test_scale_to_min(self):
        """"""
        plane = Plane.make(33.33, 66.66)
        grid = Grid.make(16, 16)
        grid.scale_to_min(plane)

        self.assertEqual(grid.one.minimum, 0)
        self.assertEqual(grid.one.maximum, 33)
        self.assertEqual(grid.two.minimum, 0)
        self.assertEqual(grid.two.maximum, 33)

    def test_init(self):
        """"""
        grid = Grid(Line(1.0, 2.49), Line(2.51, 4.0))

        self.assertEqual(grid.one.minimum, 1)
        self.assertEqual(grid.one.maximum, 2)
        self.assertEqual(grid.two.minimum, 3)
        self.assertEqual(grid.two.maximum, 4)
