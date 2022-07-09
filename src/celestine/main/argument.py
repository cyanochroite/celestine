"""Parse arguments."""
import argparse


from celestine.main.keyword import LANGUAGE

from celestine.main.keyword import ENGLISH
from celestine.main.keyword import FRENCH
from celestine.main.keyword import GERMAN


from celestine.main.keyword import PACKAGE

from celestine.main.keyword import CELESTINE
from celestine.main.keyword import CURSES
from celestine.main.keyword import DEARPYGUI
from celestine.main.keyword import TKINTER
from celestine.main.keyword import UNITTEST


from celestine.main.keyword import PYTHON

from celestine.main.keyword import PYTHON_3_6
from celestine.main.keyword import PYTHON_3_7
from celestine.main.keyword import PYTHON_3_8
from celestine.main.keyword import PYTHON_3_9
from celestine.main.keyword import PYTHON_3_10
from celestine.main.keyword import PYTHON_3_11


parser = argparse.ArgumentParser(
    prog=CELESTINE
)

parser.add_argument(
    "-l, --language",
    choices=[
        ENGLISH,
        FRENCH,
        GERMAN
    ],
    help="Choose a language.",
    dest=LANGUAGE
)

parser.add_argument(
    "-p, --package",
    choices=[
        CELESTINE,
        CURSES,
        DEARPYGUI,
        TKINTER,
        UNITTEST
    ],
    help="Choose a mode to opperate in.",
    dest=PACKAGE
)

parser.add_argument(
    "-v, --version",
    choices=[
        PYTHON_3_6,
        PYTHON_3_7,
        PYTHON_3_8,
        PYTHON_3_9,
        PYTHON_3_10,
        PYTHON_3_11
    ],
    help="Tell me which python version you are using.",
    dest=PYTHON
)

argument = parser.parse_args()
