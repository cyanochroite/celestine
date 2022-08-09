"""Package unittest."""
import unittest

from .keyword import CELESTINE
from .keyword import ERROR
from .keyword import MODULE


def main(_):
    """def main"""
    MODULE = "celestine.application.verify.parser.test_translator"
    unittest.main(
        MODULE,
        None,
        [CELESTINE],
        None,
        unittest.defaultTestLoader,
        True,
        2,
        False,
        True,
        True,
        ERROR,
    )
