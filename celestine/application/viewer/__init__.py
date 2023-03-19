""""""

# from celestine.application.viewer.core import os
import os

from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import S

from .text import DIRECTORY


class Session(SuperSession):
    """"""

    directory: S

    def dictionary(self) -> AD:
        """"""
        return {
            DIRECTORY: Optional(
                os.getcwd(),
                self._language.VIEWER_SESSION_DIRECTORY,
            ),
        }
