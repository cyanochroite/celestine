"""
Pylint can't seem to find curses and so gives a bnuch of errors.
Putting alias here to contain errors to this file only.

Hidding everything in the __getattribute__ function.
"""

import typing

# https://dearpygui.readthedocs.io/en/latest/
import curses
import _curses

from celestine.unicode import ESCAPE
from celestine.unicode import SPACE


class Package:
    """"""

    def window(self, column, row, width, height):
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return package.newwin(nlines, ncols, begin_y, begin_x)

    def subwindow(self, window, column, row, width, height):
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    def __getattribute__(self, name) -> typing.Any:
        """"""
        one = [
            "noecho",
            "initscr",
            "cbreak",
            "start_color",
            "echo",
            "nocbreak",
            "endwin",
            "newwin",
        ]
        two = [
            "doupdate",
            "KEY_UP",
            "KEY_DOWN",
            "KEY_LEFT",
            "KEY_RIGHT",
        ]

        if name in one:
            return getattr(_curses, name)
        if name in two:
            return getattr(curses, name)

        match name:
            case "KEY_EXIT":
                return ord(ESCAPE)
            case "KEY_CLICK":
                return ord(SPACE)
            case "space":
                return 32
            case "quit":
                return 113
            case "down":
                return 258
            case "up":
                return 259
            case "left":
                return 260
            case "right":
                return 261

            case "window":
                return object.__getattribute__(self, name)
            case "subwindow":
                return object.__getattribute__(self, name)
            case "doupdate":
                return object.__getattribute__(self, name)


package = Package()
