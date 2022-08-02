"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import os.path

asset = sys.path[0]
directory = os.path.dirname(sys.path[0])

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import PYTHON


from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_celestine

from celestine.core import load

from celestine.main.argument import parser

PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"


CELESTINE = "celestine"
CURSES = "curses"
DEARPYGUI = "dearpygui"
TKINTER = "tkinter"
UNITTEST = "unittest"
TERMINAL = "terminal"


applications = [
    "configuration",
    CURSES,
    DEARPYGUI,
    TERMINAL,
    TKINTER,
    "verify",
    "language",
    None
]


default = configuration_celestine()

configuration = configuration_load(
    directory,
    CELESTINE,
    CONFIGURATION_CELESTINE
)


def load_application():
    try:
        argumentation = sys.argv[1]
        if argumentation not in applications:
            parser.parse_args()
    except IndexError:
        try:
            configuration = configuration_load(directory, CELESTINE, CONFIGURATION_CELESTINE)
            argumentation = configuration[CELESTINE][APPLICATION]
        except KeyError:
            configuration = configuration_celestine()
            argumentation = configuration[CELESTINE][APPLICATION]
    return load.module(APPLICATION, argumentation)


def load_python():
    try:
        python = load.module(PYTHON, PYTHON_3_6)
        python = load.module(PYTHON, PYTHON_3_7)
        python = load.module(PYTHON, PYTHON_3_8)
        python = load.module(PYTHON, PYTHON_3_9)
        python = load.module(PYTHON, PYTHON_3_10)
        python = load.module(PYTHON, PYTHON_3_11)
    except SyntaxError:
        pass
    return python


application = load_application()
python = load_python()


window = load.module("window", "main")

def cow():
    """pointless"""
    return 7 or 8

cow = cow()

print("CHANGE THIS")
language = load.module("language", "english")
