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


PACKAGE = {
    DEARPYGUI: Package("DearPyGui", "dearpygui", "dearpygui"),
    PILLOW: Package("Pillow", "PIL", "pillow"),
    TKINTER: Package("tkinter", "tkinter", "tkinter"),
    UNITTEST: Package("unittest", "unittest", "unittest")
}


MODE = [
    MAIN,
    VERIFY
]

GUI = [
    DEARPYGUI,
    CURSES,
    TERMINAL,
    TKINTER
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

def main(session):
    parser = argparse.ArgumentParser(
        prog="celestine"
    )
    
    parser.add_argument(
        "-p", "--package",
        action="store_true",
        help="List all installed packages."
    )



    parser.add_argument(
        "-m", "--mode",
        default=MAIN,
        choices=MODE,
        help="Choose a mode to opperate in."
    )

    parser.add_argument(
        "-g", "--gui",
        default=TERMINAL,
        choices=GUI,
        help="Choose a mode to opperate in."
    )

    parser.add_argument(
        "ignore",
        nargs="*",
        help="Ignore."
    )

    parse = parser.parse_args()

    mode = parse.mode

    if mode == VERIFY:
        return EXIT.TEST


    import configparser
    

    

    from celestine.gui.main import main
    module = import_module("gui", parse.gui)
    window = module.Window()
    main(session, window)

#    window.run()
    

   
    
    return EXIT.SUCCESS
