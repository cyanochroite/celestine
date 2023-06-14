"""Terminal handling for character-cell displays."""

from celestine.typed import A
from celestine.unicode import (
    ESCAPE,
    SPACE,
)

from . import Abstract


class Package(Abstract):
    """"""

    def window(self, column, row, width, height):
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return self.package.newwin(nlines, ncols, begin_y, begin_x)

    def subwindow(self, window, column, row, width, height):
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    def __getattr__(self, name) -> A:
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
            case _:
                result = getattr(self.package, name)
        return result
