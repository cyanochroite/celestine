import unittest

from celestine.extension.more_itertools import *


class test_more_itertools(unittest.TestCase):
    def test_split_when(self):
        iterable = ["A", "B", 0, 1]
        def function(x, y): return type(x) is not type(y)
        return split_when(iterable, function)
