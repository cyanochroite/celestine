""""""
from types import ModuleType as MT
from typing import Dict as D
from typing import TypeAlias as TA

from celestine.application.viewer.core import os
import dataclasses
import os
import types
import typing

from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Positional

from celestine.session.argument import Argument

from .text import DIRECTORY

from .main import _setup

AD: TA = D[str, Argument]


@dataclasses.dataclass(init=False)
class Session():
    """"""

    directory: str
    ape: str
    you: str

    @staticmethod
    @staticmethod
    def dictionary(application: MT, language: MT) -> AD:
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


def main(page):
    image = _setup(page)
    with page.line("head") as line:
        line.label("Settings", "no puppy. File Explorer using Tkinter")
    index_y = 0
    limit_y = min(len(image) // 4, 4)
    while index_y < limit_y:
        index_x = 0
        limit_x = min(len(image) - limit_y * index_y, 4)
        with page.line(F"line {index_x}") as line:
            while index_x < limit_x:
                imaged = image[index_y * 4 + index_x]
                line.image(F"{index_x}-{index_y}", imaged)
                index_x += 1
        index_y += 1
