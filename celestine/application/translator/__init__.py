"""Application for translating text to other languages."""

from celestine import language
from celestine.literal import NONE
from celestine.session.argument import Optional
from celestine.session.session import SuperSession
from celestine.typed import (
    DA,
    S,
    ignore,
)

from .data import (
    KEY,
    REGION,
    URL,
)


class Session(SuperSession):
    """"""

    directory: S

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
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
