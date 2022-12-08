""""""

import typing
import types
import os

from celestine.session.argument import Hats
from celestine.session.argument import Cats

from celestine.session.attribute import Optional
from celestine.session.attribute import Override
from celestine.session.attribute import Positional

from .main import window
from .text import DIRECTORY


attribute = {
    DIRECTORY: Optional(os.getcwd(), "pick your nose"),
    "ape": Override("four", "moo", []),
    "you": Positional("seves", "cow", []),
}


def main(_):
    return [
        window,
    ]
