"""Application for translating text to other languages."""

from celestine.window.page import Page
import typing
import types
from celestine.session.argument import Argument
from celestine.session.argument import Optional

from celestine.text.unicode import NONE

from .text import KEY
from .text import REGION
from .text import URL

from .report import _train


class Session():
    """"""

    @staticmethod
    def dictionary(
        _: types.ModuleType,
    ) -> typing.Dict[str, Argument]:
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


def report(page: Page):
    """"""
    with page.line("head") as line:
        line.label("title", "Page 0")
    label = _train()
    for item in label:
        with page.line("body") as line:
            line.label(item, item)
    return 0
