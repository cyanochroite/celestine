import sys
import os.path

current_directory = sys.path[0]
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

import celestine.core.load as load
from celestine.data.session import Session
from celestine.window.main import main


# https://docs.python.org/3/library/argparse.html
import argparse
import sys



session = Session(parent_directory)
print(session.python)
print(session.python < 3.9)
print(session.python > 3.9)

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

def parse_package(package):
    if package == CELESTINE:
        package = [CELESTINE]
    for name in package:
        if load.attempt(name):
            return name
        print("Package '{0}' is not installed.".format(name))
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
        parser.ini
    case _ as package:
        module = load.package(package)
        window = module.Window()
        run = main(session)
        window.run(run)

sys.exit()
