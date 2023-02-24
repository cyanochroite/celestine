"""Application for translating text to other languages."""


from celestine.window.page import Page

from celestine.session.argument import Optional

from celestine.session.session import SuperSession
from celestine.session.session import AD

from celestine.unicode import NONE

from celestine.typed import S

from .text import KEY
from .text import REGION
from .text import URL

from .report import _train
from .main import _translate


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
    with page.line("head") as line:
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
