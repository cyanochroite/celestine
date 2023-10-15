""""""

import unittest

from celestine.window.point import Point


class TestPoint(unittest.TestCase):
    """"""

    def test_new(self):
        """"""
        point = Point(0, 1)
        self.assertEqual(point.one, 0)

    def test_old(self):
        """"""
        point = Point(0, 1)
        self.assertEqual(point.two, 1)
