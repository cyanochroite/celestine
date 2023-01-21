"""Package unittest."""

import unittest
import pathlib

from celestine import load
from celestine.load import directory

from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.page import Page

from .text import CELESTINE
from .text import ERROR
from .text import PATH
from .text import TEST


class Session(SuperSession):
    """"""


def main(_: Page) -> N:
    """def main"""
    module = load.module(*PATH)
    cats = directory.find(TEST)
    for cat in cats:
        dog = pathlib.PurePath(cat)
        car = load.dictionary(*dog.parts)
        for (item, value) in car.items():
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
