"""Application for translating text to other languages."""


from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S
from celestine.unicode import NONE

from .data import (
    KEY,
    GROUP,
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
                core.language.TRANSLATOR_SESSION_KEY,
            ),
            GROUP: Optional(
                NONE,
                core.language.TRANSLATOR_SESSION_REGION,
            ),
        }
