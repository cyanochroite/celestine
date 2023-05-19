"""Application for translating text to other languages."""


from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S
from celestine.unicode import NONE
from celestine.window.container import Container as Page


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
                self.language.TRANSLATOR_SESSION_KEY,
            ),
            REGION: Optional(
                NONE,
                self.language.TRANSLATOR_SESSION_REGION,
            ),
            URL: Optional(
                NONE,
                self.language.TRANSLATOR_SESSION_URL,
            ),
        }

