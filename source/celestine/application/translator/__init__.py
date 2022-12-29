"""Application for translating text to other languages."""

import typing
import types

from types import ModuleType as MT
from typing import Dict as D
from typing import TypeAlias as TA

from celestine.session.argument import Argument
from celestine.session.argument import Optional
from celestine.window.page import Page

from celestine.text.unicode import NONE

from .text import KEY
from .text import REGION
from .text import URL

from .report import _train


AD: TA = D[str, Argument]


class Session():
    """"""

    @staticmethod
    def dictionary(application: MT, language: MT) -> AD:
        """"""
        return {
            KEY: Optional(
                NONE,
                "pick your nose",
            ),
            REGION: Optional(
                NONE,
                "pick your toes",
            ),
            URL: Optional(
                NONE,
                "pick your hoes",
            ),
        }


def main(page: Page):
    """"""
    with page.line("head") as line:
        line.label("title", "Page 0")
    line.label("fish are friends", "fish are food")
    return 0


def report(page: Page):
    """"""
    with page.line("head") as line:
        line.label("title", "Page main")
    train = _train()
    for (tag, text) in train.items():
        with page.line("body") as line:
            line.label(tag, text)
    return 1
