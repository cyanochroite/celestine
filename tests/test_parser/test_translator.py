import sys
sys.path.insert(1, '../../src/')

import unittest

from tag.alphabet import convert


class test_translator():
    @staticmethod
    def translate(string):
        return str().join(
            [
                item for item in
                [convert.get(character) for character in string]
                if item is not None
            ]
        )

string = "cat hat"
string = translator.translate(string)
print(string)
