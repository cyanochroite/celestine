"""Parse arguments."""
import argparse


from celestine.main.keyword import LANGUAGE

from celestine.main.keyword import BULGARIAN
from celestine.main.keyword import CROATIAN
from celestine.main.keyword import CZECH
from celestine.main.keyword import DANISH
from celestine.main.keyword import DUTCH
from celestine.main.keyword import ENGLISH
from celestine.main.keyword import ESTONIAN
from celestine.main.keyword import FINNISH
from celestine.main.keyword import FRENCH
from celestine.main.keyword import GERMAN
from celestine.main.keyword import GREEK
from celestine.main.keyword import HUNGARIAN
from celestine.main.keyword import IRISH
from celestine.main.keyword import ITALIAN
from celestine.main.keyword import LATVIAN
from celestine.main.keyword import LITHUANIAN
from celestine.main.keyword import MALTESE
from celestine.main.keyword import POLISH
from celestine.main.keyword import PORTUGUESE
from celestine.main.keyword import ROMANIAN
from celestine.main.keyword import SLOVAK
from celestine.main.keyword import SLOVENIAN
from celestine.main.keyword import SPANISH
from celestine.main.keyword import SWEDISH


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
        BULGARIAN,
        CROATIAN,
        CZECH,
        DANISH,
        DUTCH,
        ENGLISH,
        ESTONIAN,
        FINNISH,
        FRENCH,
        GERMAN,
        GREEK,
        HUNGARIAN,
        IRISH,
        ITALIAN,
        LATVIAN,
        LITHUANIAN,
        MALTESE,
        POLISH,
        PORTUGUESE,
        ROMANIAN,
        SLOVAK,
        SLOVENIAN,
        SPANISH,
        SWEDISH
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
