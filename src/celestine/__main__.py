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

parser = argparse.ArgumentParser(
    prog="celestine"
)

parser.add_argument(
    "-p, --package",
    default="celestine",
    choices=[
        "celestine",
        "curses",
        "dearpygui",
        "tkinter",
        "unittest"
    ],
    help="Choose a mode to opperate in.",
    dest="package"
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
    "-v, --version",
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

parse = parser.parse_args()

session = Session(parent_directory)

package = load.module("package", parse.package)
python = load.module("python", parse.python)
language = load.module("language", parse.language)

if package == "unittest":
    sys.argv = [sys.argv[0]]  # clear argument list
    # Import everything so we can find tests.
    # This can only be done from the top level, so that is why it is here.
    from celestine.package.unittest import *
    # Also we only attempt to import unittest if the user requested it.
    # This is because it could not be installed and would error otherwise.
    import unittest
    unittest.main()  # this function will terminate the program
    # this line never reached

window = package.Window()
session = Session(parent_directory)
run = main(session)
window.run(run)

sys.exit()
