"""Application for translating text to other languages."""


from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S
from celestine.unicode import NONE
from celestine.window.container import Container as Page

from .main import _translate
from .report import _train
from .text import (
    KEY,
    REGION,
    URL,
)


class Session(SuperSession):
    """"""

    directory: S

    def dictionary(self) -> AD:
        """"""
        return {
            KEY: Optional(
                NONE,
                self._language.TRANSLATOR_SESSION_KEY,
            ),
            REGION: Optional(
                NONE,
                self._language.TRANSLATOR_SESSION_REGION,
            ),
            URL: Optional(
                NONE,
                self._language.TRANSLATOR_SESSION_URL,
            ),
        }


def main(page: Page):
    """"""
    with page.span("head") as line:
        line.label("title", "fish eat friends for food")
    _translate(page.session)


# TODO:figure out how to make actions not trigger on function load
def _report(page: Page):
    """"""
    with page.line("head") as line:
        line.label("title", "Page main")
    train = _train()
    for tag, text in train.items():
        with page.line("body") as line:
            line.label(tag, text)
