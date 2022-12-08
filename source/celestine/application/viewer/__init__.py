""""""

import typing
import types
import os

from celestine.session.argument import Hats
from celestine.session.argument import Cats

from .main import window
from .text import DIRECTORY


attribute = {
    DIRECTORY: Cats(Hats.optional, os.getcwd(), "pick your nose", []),
    "ape": Cats(Hats.optional, "four", "moo", []),
    "you": Cats(Hats.optional, "seves", "cow", []),
}


def main(_):
    return [
        window,
    ]
