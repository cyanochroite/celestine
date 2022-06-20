import unittest

from celestine.mypackage import *


class test_init(unittest.TestCase):
    def test_pass(self):
        self.assertIsNot(package("os"), None)

    def test_fail(self):
        self.assertIs(package("python"), None)
