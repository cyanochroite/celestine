import unittest

from celestine.parser.translator import *


class test_translator(unittest.TestCase):
    def test_translate(self):
        string = "cat hat"
        result = translator.translate(string)
        self.assertEqual(string, result)
