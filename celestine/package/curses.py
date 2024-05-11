"""Terminal handling for character-cell displays."""

from celestine import load
from celestine.literal import (
    ESCAPE,
    SPACE,
)
from celestine.package import Abstract
from celestine.typed import (
    A,
    I,
    S,
)


class Package(Abstract):
    """"""

    def subwindow(self, window, column: I, row: I, width: I, height: I) -> A:
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    def window(self, column: I, row: I, width: I, height: I) -> A:
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return self.package.newwin(nlines, ncols, begin_y, begin_x)

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
