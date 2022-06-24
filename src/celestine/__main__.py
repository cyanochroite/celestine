"""This is the main file. It runs first."""
# https://docs.python.org/3/library/argparse.html
import argparse
import sys
import os.path

current_directory = sys.path[0]
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

# pylint: disable=wrong-import-position, wildcard-import, unused-wildcard-import
# The parent directory must be added to the system path
# before attempting to load our package in.
# Also, getting unittest to work properly is hard
# and importing everything seems to make it work.
from celestine.core import load
from celestine.data.session import Session
from celestine.window.main import main


session = Session(parent_directory)

VERSION = 1


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
    CELESTINE,
    CURSES,
    DEARPYGUI,
    TKINTER,
    UNITTEST
]


parser = argparse.ArgumentParser(prog=CELESTINE)
parser.add_argument(
    "package",
    nargs="*",
    default=CELESTINE,
    choices=PACKAGE,
    help="Choose a mode to opperate in."
)

parser.add_argument(
    "-a", "--available",
    action="store_true",
    help="List all installed packages."
)


parser.add_argument(
    "-i", "--ini",
    action=STORE,
    nargs=1,
    help="List all installed packages."
)

parse = parser.parse_args()


def parse_package(_package):
    """Parses a package and tells you why it didn't work."""
    if _package == CELESTINE:
        _package = [CELESTINE]
    for name in _package:
        if load.attempt(name):
            return name
        print(F"Package '{name}' is not installed.")
    return CELESTINE


match parse_package(parse.package):
    case "unittest":
        sys.argv = [sys.argv[0]]  # clear argument list
        # Import everything so we can find tests.
        # This can only be done from the top level, so that is why it is here.
        from celestine.package.unittest import *
        # Also we only attempt to import unittest if the user requested it.
        # This is because it could not be installed and would error otherwise.
        import unittest
        unittest.main()  # this function will terminate the program
    case "celestine":
        pass
    case _ as package:
        module = load.package(package)
        window = module.Window()
        run = main(session)
        window.run(run)

sys.exit()
