import unittest

from celestine.package.itertools import *


class test_itertools(unittest.TestCase):
    def test_split_when(self):
        iterable = ["A", "B", 0, 1]
        def function(x, y): return type(x) is not type(y)
        return split_when(iterable, function)

    def test_split_when_external(self):
        iterable = ["A", "B", 0, 1]
        def function(x, y): return type(x) is not type(y)
        return split_when_external(iterable, function)

    def test_split_when_internal(self):
        iterable = ["A", "B", 0, 1]
        def function(x, y): return type(x) is not type(y)
        return split_when_internal(iterable, function)

