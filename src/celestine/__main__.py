"""This is the main file. It runs first."""
import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)


def load_module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = ["celestine"] + list(paths)
    name = ".".join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item



import argparse

from celestine.keyword.main import CELESTINE

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application



CELESTINE = "celestine"
CURSES = "curses"
DEARPYGUI = "dearpygui"
TKINTER = "tkinter"
UNITTEST = "unittest"
TERMINAL = "terminal"



application = [
    "configuration",
    CURSES,
    DEARPYGUI,
    TERMINAL,
    TKINTER,
    UNITTEST,
    "language",
    None
]


###############################

argument = sys.argv[1] if len(sys.argv) > 1 else None

if argument and argument not in application:
    raise ValueError(application)


session = load_module("main", "session").Session(directory, argument)
main = load_module("window", "main").main(session)

session.application.main(session=session, window=main)

sys.exit()
