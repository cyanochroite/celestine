import argparse

import celestine.core.load as load

from celestine.data.exit import EXIT


MORE_ITERTOOLS = "more_itertools"
PILLOW = "pillow"

DEARPYGUI = "dearpygui"
CELESTINE = "celestine"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"

EXTENSION = [
    MORE_ITERTOOLS,
    PILLOW
]

PACKAGE = [
    DEARPYGUI,
    CELESTINE,
    CURSES,
    TKINTER,
    UNITTEST
]

import sys


def main(session):
    package = next(
        (
            argv
            for argv in sys.argv
            for name in PACKAGE
            if argv == name and load.attempt(name)
        ),
        CELESTINE
    )

    if package != CELESTINE:
        # Clear argument list.
        sys.argv = [sys.argv[0]]

    print(sys.argv)
    if package == UNITTEST:
        return EXIT.TEST

    module = load.module("package", package)
    window = module.Window()

    from celestine.window.main import main as one
    two = one(session)
    window.run(two)

    return EXIT.SUCCESS
