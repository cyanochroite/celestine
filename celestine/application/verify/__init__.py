"""Package unittest."""

from .keyword import MODULE
from .keyword import ERROR
from .keyword import CELESTINE
import unittest
from celestine.application.verify.parser.test_operator import test_digit
from celestine.application.verify.parser.test_operator import test_unary
from celestine.application.verify.parser.test_operator import test_comparison

from celestine.application.verify.parser.test_translator import test_translator

from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.page import Page


class Session(SuperSession):
    """"""


"""Package unittest."""


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
