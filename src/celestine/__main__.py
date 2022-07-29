"""This is the main file. It runs first."""
import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)


import argparse

from celestine.keyword.main import CELESTINE

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application

from celestine.keyword.main import application
from celestine.core import load


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
    UNITTEST,
    "language",
    None
]

application = sys.argv[1] if len(sys.argv) > 1 else None

if application and argument not in applications:
    raise ValueError(applications)


from celestine.core import load


session = load.module("main", "session")


#session = load.module("main", "session").Session(directory, application)
main = load.module("window", "main").main(session)

session.application.main(session=session, window=main)

sys.exit()
