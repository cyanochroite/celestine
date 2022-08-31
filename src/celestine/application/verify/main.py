"""Package unittest."""
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
