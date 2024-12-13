"""Terminal handling for character-cell displays."""

from celestine.package import Abstract
from celestine.typed import (
    A,
    K,
    N,
    Z,
)

cbreak: A
color_pair: A
doupdate: A
echo: A
endwin: A
init_color: A
init_pair: A
initscr: A
KEY_CLICK: A
KEY_DOWN: A
KEY_EXIT: A
KEY_LEFT: A
KEY_RIGHT: A
KEY_UP: A
nocbreak: A
noecho: A
start_color: A


class Window:
    """"""

    def box(self) -> N:
        """"""
        raise NotImplementedError(self)

    def subwin(self, nlines: Z, ncols: Z, begin_y: Z, begin_x: Z) -> K:
        """"""
        raise NotImplementedError(self, nlines, ncols, begin_y, begin_x)


def newwin(nlines: Z, ncols: Z, begin_y: Z, begin_x: Z) -> Window:
    """"""
    raise NotImplementedError(nlines, ncols, begin_y, begin_x)


class Package(Abstract):
    """"""
