"""Terminal handling for character-cell displays."""

from celestine.package import Abstract
from celestine.typed import (
    TZ2,
    B,
    K,
    N,
    R,
    S,
    Z,
    ignore,
)


class Package(Abstract):
    """"""


class Window:
    """"""

    def addstr(self, y: Z, x: Z, string: S, /) -> N:
        """"""
        raise NotImplementedError(self, y, x, string)

    def box(self) -> N:
        """"""
        raise NotImplementedError(self)

    def getch(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def getmaxyx(self) -> TZ2:
        """"""
        raise NotImplementedError(self)

    def keypad(self, flag: B) -> N:
        """"""
        raise NotImplementedError(self, flag)

    def move(self, new_y: Z, new_x: Z) -> N:
        """"""
        raise NotImplementedError(self, new_y, new_x)

    def noutrefresh(self) -> N:
        """"""
        raise NotImplementedError(self)

    def refresh(self) -> N:
        """"""
        raise NotImplementedError(self)

    def subwin(self, nlines: Z, ncols: Z, begin_y: Z, begin_x: Z) -> K:
        """"""
        raise NotImplementedError(self, nlines, ncols, begin_y, begin_x)


def cbreak() -> N:
    """"""
    raise NotImplementedError()


def color_pair(pair_number: Z, **star: R) -> Z:
    """"""
    raise NotImplementedError(pair_number, **star)


def doupdate() -> N:
    """"""
    raise NotImplementedError()


def echo() -> N:
    """"""
    raise NotImplementedError()


def endwin() -> N:
    """"""
    raise NotImplementedError()


def initscr() -> Window:
    """"""
    raise NotImplementedError()


def init_color(color_number: Z, r: Z, g: Z, b: Z, **star: R) -> N:
    """"""
    raise NotImplementedError(color_number, r, g, b, star)


def init_pair(pair_number: Z, fg: Z, bg: Z, **star: R) -> N:
    """"""
    raise NotImplementedError(pair_number, fg, bg, star)


def newwin(nlines: Z, ncols: Z, begin_y: Z, begin_x: Z) -> Window:
    """"""
    raise NotImplementedError(nlines, ncols, begin_y, begin_x)


def nocbreak() -> N:
    """"""
    raise NotImplementedError()


def noecho() -> N:
    """"""
    raise NotImplementedError()


def start_color() -> N:
    """"""
    raise NotImplementedError()


ignore(
    Package,
    cbreak,
    color_pair,
    doupdate,
    echo,
    endwin,
    initscr,
    init_color,
    init_pair,
    newwin,
    nocbreak,
    noecho,
    start_color,
)
