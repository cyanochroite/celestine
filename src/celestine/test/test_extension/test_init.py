import unittest

from celestine.extension import *


class test_init(unittest.TestCase):
    def test_pass(self):
        self.assertIsNot(extension("os"), None)

    def test_fail(self):
        self.assertIs(extension("python"), None)
