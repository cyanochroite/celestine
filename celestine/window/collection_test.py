""""""

import unittest

from celestine.typed import (
    N,
    ignore,
)
from celestine.window.collection import (
    Line,
    Plane,
    Point,
)


class TestLine(unittest.TestCase):
    """"""

    def test_length(self) -> N:
        """"""
        # Test positive numbers
        line = Line(0, 5)
        self.assertEqual(line.length, 5)

        # Test negative numbers
        line = Line(-3, 2)
        self.assertEqual(line.length, 5)

        # Test zero length
        line = Line(1, 1)
        self.assertEqual(line.length, 0)

    def test_midpoint(self) -> N:
        """"""
        # Test positive numbers
        line = Line(0, 10)
        self.assertEqual(line.midpoint, 5)

        # Test negative numbers
        line = Line(-4, 2)
        self.assertEqual(line.midpoint, -1)

        # Test same numbers
        line = Line(5, 5)
        self.assertEqual(line.midpoint, 5)

    def test_contains(self) -> N:
        """"""
        line = Line(0, 10)

        # Test inside
        self.assertIn(5, line)
        self.assertIn(2.5, line)

        # Test boundaries
        self.assertIn(0, line)
        self.assertIn(10, line)

        # Test outside
        self.assertNotIn(-1, line)
        self.assertNotIn(11, line)

    def test_initialization(self) -> N:
        """"""
        # Test ordered numbers
        line = Line(0, 5)
        self.assertEqual(line.one, 0)
        self.assertEqual(line.two, 5)

        # Test unordered numbers
        line = Line(5, 0)
        self.assertEqual(line.one, 0)
        self.assertEqual(line.two, 5)

        # Test floating point
        line = Line(1.5, 3.5)
        self.assertEqual(line.one, 1.5)
        self.assertEqual(line.two, 3.5)


class TestPlane(unittest.TestCase):
    """"""

    def setUp(self) -> N:
        """"""
        # Create standard test plane (0,0) to (10,10)
        self.plane = Plane(Line(0, 10), Line(0, 10))

    def test_initialization(self) -> N:
        """"""
        plane = Plane(Line(0, 5), Line(0, 5))
        self.assertEqual(plane.value, (0, 0, 5, 5))

    def test_center(self) -> N:
        """"""
        other = Plane(Line(5, 15), Line(5, 15))
        self.plane.center(other)
        self.assertEqual(self.plane.centroid.value, (10, 10))

    def test_centroid(self) -> N:
        """"""
        self.assertEqual(self.plane.centroid.value, (5, 5))

    def test_value(self) -> N:
        """"""
        self.assertEqual(self.plane.value, (0, 0, 10, 10))

    def test_create(self) -> N:
        """"""
        plane = Plane.create(10, 20)
        self.assertEqual(plane.value, (0, 0, 10, 20))

    def test_origin(self) -> N:
        """"""
        self.assertEqual(self.plane.origin.value, (0, 0))

    def test_size(self) -> N:
        """"""
        self.assertEqual(self.plane.size.value, (10, 10))

    def test_scale_to_max(self) -> N:
        """"""
        other = Plane(Line(0, 20), Line(0, 10))
        self.plane.scale_to_max(other)
        self.assertEqual(self.plane.size.value, (20, 20))

    def test_scale_to_min(self) -> N:
        """"""
        other = Plane(Line(0, 20), Line(0, 10))
        self.plane.scale_to_min(other)
        self.assertEqual(self.plane.size.value, (10, 10))

    def test_contains(self) -> N:
        """"""
        # Test point inside
        self.assertIn(Point(5, 5), self.plane)
        # Test point on boundary
        self.assertIn(Point(0, 0), self.plane)
        self.assertIn(Point(10, 10), self.plane)
        # Test point outside
        self.assertNotIn(Point(11, 11), self.plane)
        self.assertNotIn(Point(-1, -1), self.plane)

    def test_edge_cases(self) -> N:
        """"""
        # Zero dimensions
        zero_plane = Plane(Line(0, 0), Line(0, 0))
        self.assertEqual(zero_plane.size.value, (0, 0))

        # Negative dimensions should be normalized
        neg_plane = Plane(Line(-5, 5), Line(-5, 5))
        self.assertEqual(neg_plane.size.value, (10, 10))


class TestPoint(unittest.TestCase):
    """"""

    def test_value_positive_numbers(self) -> N:
        """"""
        point = Point(1.0, 2.0)
        self.assertEqual(point.value, (1, 2))

    def test_value_negative_numbers(self) -> N:
        """"""
        point = Point(-1.0, -2.0)
        self.assertEqual(point.value, (-1, -2))

    def test_value_zero(self) -> N:
        """"""
        point = Point(0.0, 0.0)
        self.assertEqual(point.value, (0, 0))

    def test_value_mixed_numbers(self) -> N:
        """"""
        point = Point(-1.0, 2.0)
        self.assertEqual(point.value, (-1, 2))

    def test_float_conversion(self) -> N:
        """"""
        point = Point(1.7, 2.3)
        self.assertEqual(point.value, (1, 2))

    def test_initialization_order(self) -> N:
        """"""
        point = Point(5.0, 3.0)
        self.assertEqual(point.one, 5.0)
        self.assertEqual(point.two, 3.0)


ignore(TestLine, TestPlane, TestPoint)
