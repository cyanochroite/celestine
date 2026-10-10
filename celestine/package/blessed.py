"""Terminal handling for character-cell displays."""

from celestine.package import Package
from celestine.typed import (
    ACM,
    B,
    N,
    S,
    Z,
    ignore,
)


class Keystroke:
    """"""

    @property
    def code(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @property
    def is_sequence(self) -> B:
        """"""
        raise NotImplementedError(self)

    @property
    def name(self) -> S:
        """"""
        raise NotImplementedError(self)


class Self(Package):
    """"""


class Terminal:
    """"""

    KEY_DOWN: Z
    KEY_ENTER: Z
    KEY_ESCAPE: Z
    KEY_LEFT: Z
    KEY_RIGHT: Z
    KEY_UP: Z

    @property
    def clear(self) -> S:
        """"""
        raise NotImplementedError(self)

    @property
    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @property
    def home(self) -> S:
        """"""
        raise NotImplementedError(self)

    @property
    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)

    ###

    @property
    def white_on_blue(self) -> S:
        """"""
        raise NotImplementedError(self)

    def cbreak(self) -> ACM[N, N]:
        """"""
        raise NotImplementedError(self)

    def hidden_cursor(self) -> ACM[N, N]:
        """"""
        raise NotImplementedError(self)

    def fullscreen(self) -> ACM[N, N]:
        """"""
        raise NotImplementedError(self)

    def inkey(self) -> Keystroke:
        """"""
        raise NotImplementedError(self)

    def move_xy(self, x: Z, y: Z) -> S:
        """"""
        raise NotImplementedError(self, x, y)

    def move_yx(self, y: Z, x: Z) -> S:
        """"""
        raise NotImplementedError(self, y, x)

    @property
    def move_left(self) -> S:
        """"""
        raise NotImplementedError(self)

    @property
    def move_right(self):
        """"""
        raise NotImplementedError(self)

    @property
    def move_up(self):
        """"""
        raise NotImplementedError(self)

    @property
    def move_down(self):
        """"""
        raise NotImplementedError(self)


ignore(Self, Terminal)
