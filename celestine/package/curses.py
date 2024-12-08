"""Terminal handling for character-cell displays."""

from celestine import load
from celestine.literal import (
    ESCAPE,
    SPACE,
)
from celestine.package import Abstract
from celestine.typed import (
    A,
    K,
    N,
    S,
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

    def __getattr__(self, name: S) -> A:
        result = None
        match name:
            case "KEY_EXIT":
                result = ord(ESCAPE)
            case "KEY_CLICK":
                result = ord(SPACE)
            case "space":
                result = 32
            case "quit":
                result = 113
            case "down":
                result = 258
            case "up":
                result = 259
            case "left":
                result = 260
            case "right":
                result = 261
            case "initscr":
                # This a temporary fix for windows-curses.
                # https://github.com/zephyrproject-rtos/windows-curses/
                # issues/50#issuecomment-1840485627
                _curses = load.package("_curses")
                for key, value in _curses.__dict__.items():
                    if key[0:4] == "ACS_" or key in ("LINES", "COLS"):
                        setattr(self.package, key, value)
                result = _curses.initscr
            case _:
                result = getattr(self.package, name)
        return result
