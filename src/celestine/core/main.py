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
from celestine.core.load import extension


def has_package(name):
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        return False


def load_valid_packages():
    #package = next((a for a in sys.argv for p in PACKAGE if a == p), None)
    for argv in sys.argv:
        for package in PACKAGE:
            if argv == package:
                if has_package(package):
                    sys.argv.remove(package)
                    return package
    return CELESTINE


def main(session):
    package = load_valid_packages()

    if package != CELESTINE:
        # Clear argument list.
        sys.argv = [sys.argv[0]]

    if package == UNITTEST:
        return EXIT.TEST

    module = import_module("package", package)
    window = module.Window()

    from celestine.window.main import main as one
    two = one(session)
    window.run(two)

    return EXIT.SUCCESS
