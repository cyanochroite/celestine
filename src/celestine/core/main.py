import argparse
import importlib

from celestine.data.exit import EXIT



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



def import_package(package, module):
    __import__(".".join(["celestine", "package", package, module]))


def import_module(package, module):
    return importlib.import_module(".".join(["celestine", package, module]))

import os.path

def import_file(directory):
    return os.path.join(directory, "celestine", "celestine.ini")




class Package():
    def __init__(self, name, external, internal):
        self.name = name
        self.external = external
        self.internal = internal
        self.imported = True


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

PACKAGE = {
    DEARPYGUI: Package("DearPyGui", "dearpygui", "dearpygui"),
    PILLOW: Package("Pillow", "PIL", "pillow"),
    TKINTER: Package("tkinter", "tkinter", "tkinter"),
    UNITTEST: Package("unittest", "unittest", "unittest")
}


MODE = [
    DEARPYGUI,
    CELESTINE,
    CURSES,
    TERMINAL,
    TKINTER,
    UNITTEST
]
__version__ = "0.1.2.3"


def check(gui, module):
    package = PACKAGE[gui]
    if gui != module:
        return False
    if not package.imported:
        name = package.name
        install = package.install
        message = "Package {0} not installed\nTry: {1}".format(name, install)
        raise SystemExit(message)
    return True


def check_package(name):
    package = PACKAGE[name]
    if not package.imported:
        name = package.name
        install = package.install
        message = "Package {0} not installed\nTry: {1}".format(name, install)
        raise SystemExit(message)


class Window():
    pass


import celestine.core.load as load
import os

image = {}
application = None
session = None


def setup(self):
    image1 = load.file(session, ["file", "anitest.gif"])
    image2 = load.file(session, ["file", "test4.gif"])
    image["image1"] = self.image_load(image1)
    image["image2"] = self.image_load(image2)


def view(self):
    self.image("00", image["image1"])
    self.image("01", image["image2"])
    self.label("Settings", "no puppy. File Explorer using Tkinter")
    self.filebox("set", "Settings")


def main(data, window):
    global session
    session = data
    window.run(setup, view)


def main(_session):
    global session
    session = _session
    
    parser = argparse.ArgumentParser(
        prog="celestine"
    )

    parser.add_argument(
        "package",
        nargs="?",
        default=TERMINAL,
        choices=MODE,
        help="Choose a mode to opperate in."
    )

    parse = parser.parse_args()

    package = parse.package

    if package == UNITTEST:
        return EXIT.TEST

    from celestine.package.main import main
    module = import_module("package", package)
    window = module.Window()
    window.run(setup, view)
    

    return EXIT.SUCCESS
