""""""

import dataclasses
import os
import types
import typing

from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Positional

from celestine.session.argument import Argument

from .main import window
from .text import DIRECTORY


@dataclasses.dataclass(init=False)
class Session():
    """"""

    directory: str
    ape: str
    you: str

    @staticmethod
    def dictionary(
        language: types.ModuleType,
    ) -> typing.Dict[str, Argument]:
        """"""

        return {
            DIRECTORY: Optional(
                os.getcwd(),
                "pick your nose",
            ),
            "tape": Override(
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
    """"""
    return [
        window,
    ]
