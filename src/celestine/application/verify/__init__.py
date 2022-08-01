"""Package unittest."""
import unittest

from .keyword import CELESTINE
from .keyword import ERROR
from .keyword import MODULE


# unittest needs this exact vairable to run properly
# note that it is the same name as the package
verify = None  # pylint: disable=invalid-name


def main(_):
    """def main"""
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
