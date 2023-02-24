"""Package unittest."""

import unittest

from celestine.text import CELESTINE
from celestine.text.directory import APPLICATION

from celestine import load
from celestine.load import directory

from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.page import Page

ERROR = "error"
MODULE = "module"
TARGET = "_test.py"
TEST = "test"


class Session(SuperSession):
    """"""


def main(_: Page) -> N:
    """def main"""
    module = load.module(APPLICATION, TEST)
    paths = directory.find(TARGET)
    for path in paths:
        dictionary = load.dictionary(*path)
        for item, value in dictionary.items():
            setattr(module, item, value)

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
