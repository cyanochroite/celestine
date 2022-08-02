"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import os.path

asset = sys.path[0]
directory = os.path.dirname(sys.path[0])

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import PYTHON


from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION


from celestine.core import load


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










def load_application():
    try:
        argumentation = sys.argv[1]
        if argumentation not in applications:
            parser.parse_args()
    except IndexError:
        try:
            configuration = configuration.load(directory, CELESTINE, CONFIGURATION)
            argumentation = configuration[CELESTINE][APPLICATION]
        except KeyError:
            configuration = configuration.load_default()
            argumentation = configuration[CELESTINE][APPLICATION]
    return load.module(APPLICATION, argumentation)





print("CHANGE THIS")
language = load.module("language", "english")
window = load.module("window", "main")





from celestine.session.argument import Argument
from celestine.session.configuration import Configuration
from celestine.session.python import python

class Session():
    def __init__(self, directory):
        self.directory = directory

        self.argument = Argument()
        self.configuration = Configuration(directory)
        self.python = python()
        
        
        
        #pre
        self.application = load_application()
        self.window = load.module("window", "main")
        
