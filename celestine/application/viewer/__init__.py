""""""

# from celestine.application.viewer.core import os
import os

from celestine import language
from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S


class Session(SuperSession):
    """"""

    output: S

    @classmethod
    def dictionary(cls) -> AD:
        """"""
        return super().dictionary() | {
            "output": Optional(
                os.getcwd(),
                language.VIEWER_SESSION_DIRECTORY,
            ),
        }
