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

EXTENSION = [
    MORE_ITERTOOLS,
    PILLOW
]


DEARPYGUI = "dearpygui"
CELESTINE = "celestine"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"


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



EXTENSION = [
    MORE_ITERTOOLS,
    PILLOW
]

####

DEARPYGUI = "dearpygui"
CELESTINE = "celestine"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"

ENGLISH = "english"
FRENCH = "french"
GERMAN = "german"

PYTHON_3_6 = "3.6"
PYTHON_3_7 = "3.7"
PYTHON_3_8 = "3.8"
PYTHON_3_9 = "3.9"
PYTHON_3_10 = "3.10"
PYTHON_3_11 = "3.11"

PACKAGE = [
    CELESTINE,
    CURSES,
    DEARPYGUI,
    TKINTER,
    UNITTEST
]

LANGUAGE = [
    ENGLISH,
    FRENCH,
    GERMAN
]

PYTHON = [
    PYTHON_3_6,
    PYTHON_3_7,
    PYTHON_3_8,
    PYTHON_3_9,
    PYTHON_3_10,
    PYTHON_3_11
]

parser = argparse.ArgumentParser(prog=CELESTINE)

parser.add_argument(
    "package",
    nargs="*",
    default=CELESTINE,
    choices=[
        "celestine",
        "curses",
        "dearpygui",
        "tkinter",
        "unittest"
    ],
    help="Choose a mode to opperate in."
)

parser.add_argument(
    "-l, --language",
    default="english",
    choices=[
        "english",
        "french",
        "german"
    ],
    help="Choose a language.",
    dest="language"
)

parser.add_argument(
    "-p, --python",
    default="python_3_10",
    choices=[
        "python_3_6",
        "python_3_7",
        "python_3_8",
        "python_3_9",
        "python_3_10",
        "python_3_11"
    ],
    help="Tell me which python version you are using.",
    dest="python"
)

####

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
        return CELESTINE
    for name in _package:
        if load.attempt(name):
            return name
        print(F"Package '{name}' is not installed.")
    return CELESTINE


package = parse_package(parse.package)

package = load.module("package", parse.package)
python = load.module("python", parse.python)
language = load.module("language", parse.language)

if package == CELESTINE:
    pass

if package == UNITTEST:
    sys.argv = [sys.argv[0]]  # clear argument list
    # Import everything so we can find tests.
    # This can only be done from the top level, so that is why it is here.
    from celestine.package.unittest import *
    # Also we only attempt to import unittest if the user requested it.
    # This is because it could not be installed and would error otherwise.
    import unittest
    unittest.main()  # this function will terminate the progra

if package in [CURSES, DEARPYGUI, TKINTER]:
    module = load.package(package)
    window = module.Window()
    run = main(session)
    window.run(run)

sys.exit()
