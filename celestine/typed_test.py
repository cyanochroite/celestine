""""""

import unittest

from celestine.typed import (
    VS,
    VZ,
    B,
    F,
    N,
    S,
    Z,
    ignore,
    string,
)


class TestTypedFunctions(unittest.TestCase):
    """"""

    def test_ignore(self) -> N:
        """"""
        # Test with different argument types
        self.assertIsNone(ignore())  # type: ignore[func-returns-value]

        self.assertIsNone(ignore(1))  # type: ignore[func-returns-value]

        self.assertIsNone(
            ignore("str", 123, True)  # type: ignore[func-returns-value]
        )

    def test_string(self) -> N:
        """"""
        # Test basic string joining
        self.assertEqual(string("a", "b", "c"), "abc")

        # Test empty strings
        self.assertEqual(string("", "", ""), "")

        # Test single string
        self.assertEqual(string("test"), "test")

        # Test empty input
        self.assertEqual(string(), "")


class TestTypeAliases(unittest.TestCase):
    """"""

    def test_basic_types(self) -> N:
        """"""
        # Test bool type
        value_b: B = True
        self.assertIsInstance(value_b, bool)

        # Test float type
        value_f: F = 1.0
        self.assertIsInstance(value_f, float)

        # Test str type
        value_s: S = "test"
        self.assertIsInstance(value_s, str)

        # Test int type
        value_z: Z = 42
        self.assertIsInstance(value_z, int)

    def test_optional_types(self) -> N:
        """"""
        # Test Optional types
        value_s: VS = "test"
        self.assertIsInstance(value_s, str)

        value_z: VZ = 42
        self.assertIsInstance(value_z, int)
