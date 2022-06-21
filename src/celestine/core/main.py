import argparse

from celestine.data.exit import EXIT
from celestine.core.load import import_module


STORE = "store"
STORE_CONST = "store_const"
STORE_TRUE = "store_true"
STORE_FALSE = "store_false"
APPEND = "append"
APPEND_CONST = "append_const"
COUNT = "count"
HELP = "help"
VERSION = "version"
EXTEND = "extend"

ITERTOOLS = "itertools"
PILLOW = "pillow"

DEARPYGUI = "dearpygui"
CELESTINE = "celestine"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"

EXTENSION = [
    ITERTOOLS,
    PILLOW
]

PACKAGE = [
    DEARPYGUI,
    CELESTINE,
    CURSES,
    TKINTER,
    UNITTEST
]


def main(session):
    parser = argparse.ArgumentParser(
        prog="celestine"
    )

    parser.add_argument(
        "package",
        nargs="?",
        default=CELESTINE,
        choices=PACKAGE,
        help="Choose a mode to opperate in."
    )

    parse = parser.parse_args()

    package = parse.package

    if package == UNITTEST:
        return EXIT.TEST

    module = import_module("package", package)
    window = module.Window()

    from celestine.window.main import main as one
    two = one(session)
    window.run(two)

    return EXIT.SUCCESS
