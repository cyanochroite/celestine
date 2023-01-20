"""Package unittest."""

import unittest

from .text import MODULE
from .text import ERROR
from .text import CELESTINE

from celestine.application.verify.parser.test_operator import test_digit
from celestine.application.verify.parser.test_operator import test_unary
from celestine.application.verify.parser.test_operator import test_comparison

from celestine.application.verify.parser.test_translator import test_translator


from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.page import Page


class Session(SuperSession):
    """"""


def main(_):
    """def main"""
    module = "celestine.application.viewer.verify"
#    module = MODULE
    unittest.main(
        module,
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
