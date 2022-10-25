"""Package unittest."""
import unittest


from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.unicode import FULL_STOP


from .core.test_text import test_text

from .extension.test_more_itertools import test_more_itertools

from .parser.test_operator import test_digit
from .parser.test_operator import test_unary
from .parser.test_operator import test_comparison

from .parser.test_translator import test_translator

ERROR = "error"
BLENDER = "blender"
MODULE = F"{CELESTINE}{FULL_STOP}{APPLICATION}{FULL_STOP}{BLENDER}.verify"


def argument(_argument):
    """Build up the argument."""
    return _argument


def attribute():
    """Build up the attribute file."""
    return ()


def default():
    """Build up the default file."""
    return ()


def image_format():
    return []


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
