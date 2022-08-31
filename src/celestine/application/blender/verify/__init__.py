"""Package unittest."""
from .core.test_text import test_text


from .extension.test_more_itertools import test_more_itertools


from .parser.test_operator import test_digit
from .parser.test_operator import test_unary
from .parser.test_operator import test_comparison

from .parser.test_translator import test_translator


def argument(argument):
    """Build up the argument."""
    return argument


def attribute():
    """Build up the attribute file."""
    return ()


def default():
    """Build up the default file."""
    return ()


def image_format():
    return []


import unittest

from .keyword import CELESTINE
from .keyword import ERROR
from .keyword import MODULE


def main(_):
    """def main"""
    unittest.main(
        MODULE,
        None,
        [CELESTINE],
        None,
        unittest.defaultTestLoader,
        False,
        2,
        False,
        True,
        True,
        ERROR,
    )
