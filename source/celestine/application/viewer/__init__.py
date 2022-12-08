""""""

import typing
import types
import os

from celestine.session.argument import Argument
from celestine.session.argument import Hats
from celestine.session.argument import Cats

from .main import window
from .text import DIRECTORY


def add_argument(
    argument: Argument
) -> None:
    """"""

    argument.add_optional(
        DIRECTORY,
        "",
        os.getcwd(),
    )


attribute = {
    DIRECTORY: Cats(Hats.Optional, os.getcwd(), "pick your nose"),
    "ape": Cats(Hats.Optional, "four", "moo"),
    "you": Cats(Hats.Optional, "seves", "cow"),
}


def main(_):
    return [
        window,
    ]
