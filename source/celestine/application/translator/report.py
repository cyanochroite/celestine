""""""

import types
import typing

from celestine.session.argument import Argument
from celestine.window.page import Page

from .report import main as train


class Session():
    """"""

    @staticmethod
    def dictionary(
        _: types.ModuleType,
    ) -> typing.Dict[str, Argument]:
        """"""

        return {
        }


def report(page: Page):
    """"""
    with page.line("head") as line:
        line.label("title", "Page 0")
    label = train()
    for item in label:
        with page.line("body") as line:
            line.label(item, item)


def main(__: Session) -> list[typing.Callable[[Page], None]]:
    """"""
    return [
        report,
    ]
