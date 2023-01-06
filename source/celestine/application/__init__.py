""""""
from types import ModuleType as MT
from typing import Dict as D
from typing import TypeAlias as TA
import types
import typing

from celestine.session.argument import Argument
from celestine.window.page import Page

AD: TA = D[str, Argument]


class Session():
    """"""

    @staticmethod
    def dictionary(_: MT) -> AD:
        """"""
        return {
        }


def one(page: Page) -> None:
    """"""
    with page.line("head") as line:
        line.label("title", "Page one")
    with page.line("body") as line:
        line.button("past", "Page main", "main")
        line.button("next", "Page two", "two")


def two(page: Page) -> None:
    """"""
    with page.line("head") as line:
        line.label("title", "Page two")
    with page.line("body") as line:
        line.button("past", "Page one", "one")
        line.button("next", "Page main", "main")


def main(page: Page) -> None:
    """"""
    with page.line("head") as line:
        line.label("title", "Page main")
    with page.line("body") as line:
        line.button("past", "Page one", "one")
        line.button("next", "Page two", "two")
