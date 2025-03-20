""""""

import os

from celestine import language
from celestine.session.argument import Optional
from celestine.session.session import SuperSession
from celestine.typed import (
    DA,
    S,
    ignore,
)


class Session(SuperSession):
    """"""

    output: S

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            "output": Optional(
                os.getcwd(),
                language.VIEWER_SESSION_DIRECTORY,
            ),
        }
