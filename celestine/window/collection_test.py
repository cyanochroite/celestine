""""""

import unittest

from celestine.typed import (
    N,
    ignore,
)
from celestine.window.collection import (
    Digit,
    Line,
    Plane,
    Point,
)


class TestLine(unittest.TestCase):
    """"""

    def test_length(self) -> N:
        """"""
        # Test positive numbers
        line = Line(Digit(0), Digit(5))
        self.assertEqual(line.length, 5)

        # Test negative numbers
        line = Line(Digit(-3), Digit(2))
        self.assertEqual(line.length, 5)

        # Test zero length
        line = Line(Digit(1), Digit(1))
        self.assertEqual(line.length, 0)

    def test_midpoint(self) -> N:
        """"""
        # Test positive numbers
        line = Line(Digit(0), Digit(10))
        self.assertEqual(line.midpoint, 5)

        # Test negative numbers
        line = Line(Digit(-4), Digit(2))
        self.assertEqual(line.midpoint, -1)

        # Test same numbers
        line = Line(Digit(5), Digit(5))
        self.assertEqual(line.midpoint, 5)

    def test_contains(self) -> N:
        """"""
        line = Line(Digit(0), Digit(10))

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
        line = Line(Digit(0), Digit(5))
        self.assertEqual(line.one, 0)
        self.assertEqual(line.two, 5)

        # Test unordered numbers
        line = Line(Digit(5), Digit(0))
        self.assertEqual(line.one, 0)
        self.assertEqual(line.two, 5)

        # Test floating point
        line = Line(Digit(1.5), Digit(3.5))
        self.assertEqual(line.one, 1.5)
        self.assertEqual(line.two, 3.5)


class TestPlane(unittest.TestCase):
    """"""

    def setUp(self) -> N:
        """"""
        # Create standard test plane (0,0) to (10,10)
        self.plane = Plane(
            Line(Digit(0), Digit(10)), Line(Digit(0), Digit(10))
        )

    def test_initialization(self) -> N:
        """"""
        plane = Plane(
            Line(Digit(0), Digit(5)), Line(Digit(0), Digit(5))
        )
        self.assertEqual(plane.data, (0, 0, 5, 5))

    def test_center(self) -> N:
        """"""
        other = Plane(
            Line(Digit(5), Digit(15)), Line(Digit(5), Digit(15))
        )
        self.plane.center(other)
        self.assertEqual(self.plane.centroid.data, (10, 10))

    def test_centroid(self) -> N:
        """"""
        self.assertEqual(self.plane.centroid.data, (5, 5))

    def test_value(self) -> N:
        """"""
        self.assertEqual(self.plane.data, (0, 0, 10, 10))

    def test_create(self) -> N:
        """"""
        plane = Plane.create(10, 20)
        self.assertEqual(plane.data, (0, 0, 10, 20))

    def test_origin(self) -> N:
        """"""
        self.assertEqual(self.plane.origin.data, (0, 0))

    def test_size(self) -> N:
        """"""
        self.assertEqual(self.plane.size.data, (10, 10))

    def test_scale_to_max(self) -> N:
        """"""
        other = Plane(
            Line(Digit(0), Digit(20)), Line(Digit(0), Digit(10))
        )
        self.plane.scale_to_max(other)
        self.assertEqual(self.plane.size.data, (20, 20))

    def test_scale_to_min(self) -> N:
        """"""
        other = Plane(
            Line(Digit(0), Digit(20)), Line(Digit(0), Digit(10))
        )
        self.plane.scale_to_min(other)
        self.assertEqual(self.plane.size.data, (10, 10))

    def test_contains(self) -> N:
        """"""
        # Test point inside
        self.assertIn(Point(Digit(5), Digit(5)), self.plane)
        # Test point on boundary
        self.assertIn(Point(Digit(0), Digit(0)), self.plane)
        self.assertIn(Point(Digit(10), Digit(10)), self.plane)
        # Test point outside
        self.assertNotIn(Point(Digit(11), Digit(11)), self.plane)
        self.assertNotIn(Point(Digit(-1), Digit(-1)), self.plane)

    def test_edge_cases(self) -> N:
        """"""
        # Zero dimensions
        zero_plane = Plane(
            Line(Digit(0), Digit(0)), Line(Digit(0), Digit(0))
        )
        self.assertEqual(zero_plane.size.data, (0, 0))

        # Negative dimensions should be normalized
        neg_plane = Plane(
            Line(Digit(-5), Digit(5)), Line(Digit(-5), Digit(5))
        )
        self.assertEqual(neg_plane.size.data, (10, 10))


class TestPoint(unittest.TestCase):
    """"""

    def test_value_positive_numbers(self) -> N:
        """"""
        point = Point(Digit(1.0), Digit(2.0))
        self.assertEqual(point.data, (1, 2))

    def test_value_negative_numbers(self) -> N:
        """"""
        point = Point(Digit(-1.0), Digit(-2.0))
        self.assertEqual(point.data, (-1, -2))

    def test_value_zero(self) -> N:
        """"""
        point = Point(Digit(0.0), Digit(0.0))
        self.assertEqual(point.data, (0, 0))

    def test_value_mixed_numbers(self) -> N:
        """"""
        point = Point(Digit(-1.0), Digit(2.0))
        self.assertEqual(point.data, (-1, 2))

    def test_float_conversion(self) -> N:
        """"""
        point = Point(Digit(1.7), Digit(2.3))
        self.assertEqual(point.data, (1, 2))

    def test_initialization_order(self) -> N:
        """"""
        point = Point(Digit(5.0), Digit(3.0))
        self.assertEqual(point.one, 5.0)
        self.assertEqual(point.two, 3.0)


ignore(TestLine, TestPlane, TestPoint)
