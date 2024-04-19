"""Application for translating text to other languages."""


from celestine import language
from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S
from celestine.unicode import NONE

from .data import (
    KEY,
    REGION,
    URL,
)


class Session(SuperSession):
    """"""

    directory: S

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return {
            KEY: Optional(
                NONE,
                language.TRANSLATOR_SESSION_KEY,
            ),
            REGION: Optional(
                NONE,
                language.TRANSLATOR_SESSION_REGION,
            ),
            URL: Optional(
                NONE,
                language.TRANSLATOR_SESSION_URL,
            ),
        }
