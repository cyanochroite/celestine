""""""

# from celestine.application.viewer.core import os
import os

from celestine.session.argument import Optional

from celestine.session.session import SuperSession
from celestine.session.session import AD

from celestine.typed import S

from .text import DIRECTORY

from .main import _setup


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


def main(page):
    """"""
    images = _setup(page)
    with page.grid("grid", 4) as grid:
        for image in images:
            grid.image("image", image)
