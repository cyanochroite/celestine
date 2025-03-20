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

    directory: S

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
            DIRECTORY: Optional(
                os.getcwd(),
                core.language.VIEWER_SESSION_DIRECTORY,
            ),
        }
