# https://docs.python.org/3/library/argparse.html
import argparse
import sys

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


DEARPYGUI = "dearpygui"
PILLOW = "pillow"
TKINTER = "tkinter"
UNITTEST = "unittest"

MAIN = "main"
VERIFY = "verify"

CURSES = "curses"
DEARPYGUI = "dearpygui"
TERMINAL = "terminal"
TKINTER = "tkinter"
UNITTEST = "unittest"
CELESTINE = "celestine"

option = [
    "a",
    "b",
    "list"
]

PACKAGE = [
    DEARPYGUI,
    CELESTINE,
    CURSES,
    TERMINAL,
    TKINTER,
    UNITTEST,
    "A"
]

x = ["A", "B", "C"]
y = [1, 2, 3, "A"]

sys.argv = x

z = next((a for a in sys.argv for p in PACKAGE if a == p), CELESTINE)
print(z)

def has_package(name):
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        return False

def angry():
    for argv in sys.argv:
        for package in PACKAGE:
            if argv == package:
                if has_package(package):
                    return package
    return None

angry()