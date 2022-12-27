""""""

import types
import typing

from celestine.session.argument import Argument
from celestine.window.page import Page


class Session():
    """"""

    @staticmethod
    def dictionary(_: types.ModuleType) -> typing.Dict[str, Argument]:
        """"""
        return {
        }


def one(page: Page) -> int:
    """"""
    with page.line("head") as line:
        line.label("title", "Page 1")
    with page.line("body") as line:
        line.button("past", "Page 0", 0)
        line.button("next", "Page 2", 2)
    return 1


def two(page: Page) -> int:
    """"""
    with page.line("head") as line:
        line.label("title", "Page 2")
    with page.line("body") as line:
        line.button("past", "Page 1", 1)
        line.button("next", "Page 0", 0)
    return 2


def zero(page: Page) -> int:
    """"""
    with page.line("head") as line:
        line.label("title", "Page 0")
    with page.line("body") as line:
        line.button("past", "Page 1", 1)
        line.button("next", "Page 2", 2)
    return 0

