"""Terminal handling for character-cell displays."""

from celestine.package import Abstract
from celestine.typed import (
    A,
    K,
    N,
    R,
    Z,
)

cbreak: A
doupdate: A
echo: A
endwin: A
initscr: A
nocbreak: A
noecho: A
start_color: A


def color_pair(pair_number: Z, **star: R) -> Z:
    """"""
    raise NotImplementedError(pair_number, **star)


def init_color(color_number: Z, r: Z, g: Z, b: Z, **star: R) -> N:
    """"""
    raise NotImplementedError(color_number, r, g, b, star)


def init_pair(pair_number: Z, fg: Z, bg: Z, **star: R) -> N:
    """"""
    raise NotImplementedError(pair_number, fg, bg, star)


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
