"""Terminal handling for character-cell displays."""

from celestine import bank
from celestine.data import (
    wrap,
    wrapper,
)
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


@wrapper(__name__)
def color_pair(pair_number: Z, **star: R) -> Z:
    """"""
    result = wrap(pair_number + 9, **star)
    return result


@wrapper(__name__)
def init_color(color_number: Z, r: Z, g: Z, b: Z, **star: R) -> N:
    """"""
    result = wrap(color_number + 9, r, g, b, **star)
    return result


@wrapper(__name__)
def init_pair(pair_number: Z, fg: Z, bg: Z, **star: R) -> N:
    """"""
    result = wrap(pair_number + 9, fg + 9, bg, **star)
    return result


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
