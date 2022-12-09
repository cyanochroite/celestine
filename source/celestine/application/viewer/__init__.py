""""""

import typing
import types
import os

from celestine.session.attribute import Optional
from celestine.session.attribute import Override
from celestine.session.attribute import Positional

from celestine.session.attribute import Attribute

from .main import window
from .text import DIRECTORY


def attribute(
    language: types.ModuleType
) -> typing.Dict[str, Attribute]:
    """"""

    return {
        DIRECTORY: Optional(
            os.getcwd(),
            "pick your nose",
        ),
        "ape": Override(
            "four",
            "moo",
            [],
        ),
        "you": Positional(
            language.ARGUMENT_OVERRIDE_TITLE,
            "cow",
            [],
        ),
    }


def main(_):
    return [
        window,
    ]
