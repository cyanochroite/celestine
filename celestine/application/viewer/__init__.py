""""""

# from celestine.application.viewer.core import os
import os

from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S

from .data import DIRECTORY


class Session(SuperSession):
    """"""

    output: S

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
            "output": Optional(
                os.getcwd(),
                core.language.VIEWER_SESSION_DIRECTORY,
            ),
        }
