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
        # self.language
        return {
            DIRECTORY: Optional(
                os.getcwd(),
                "pick your nose",
            ),
        }


def main(page):
    """"""
    image = _setup(page)
    with page.line("head") as line:
        line.label("Settings", "no puppy. File Explorer using Tkinter")
    index_y = 0
    limit_y = min(len(image) // 4, 4)
    while index_y < limit_y:
        index_x = 0
        limit_x = min(len(image) - limit_y * index_y, 4)
        with page.line(F"line {index_x}") as line:
            while index_x < limit_x:
                imaged = image[index_y * 4 + index_x]
                line.image(F"{index_x}-{index_y}", imaged)
                index_x += 1
        index_y += 1
