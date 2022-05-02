import sys
import argparse

def import_package(package):
    __import__("celestine." + package)

class Package():
    def __init__(self, name, external, internal, main):
        self.name = name
        self.external = external
        self.internal = internal
        self.imported = True
        self.main = main

    def _import(self):
        try:
            __import__(self.external)
            return True
        except ModuleNotFoundError:
            return False
    
    def import_package(self):
        if not self._import:
            raise MissingPackageError(self)
        self.main()


class MissingPackageError(ImportError):
    def __init__(self, package):
        self.package = package
        #self.message = message

    def __str__(self):
        print("Candy")
        return "This feature needs the package '{0}' installed.".format(
            self.package.name
        )
    


def _import(module):
    try:
        __import__(module)
        return True
    except ModuleNotFoundError:
        return False


DEARPYGUI = "DEARPYGUI"
DESKTOP = "DESKTOP"
FILE = "FILE"
PILLOW = "PILLOW"
PROGRAM = "PROGRAM"
TERMINAL = "TERMINAL"
TKINTER = "TKINTER"
UNITTEST = "UNITTEST"
VERIFICATION = "VERIFICATION"


FILE = "file"
PILLOW = "pillow"
PROGRAM = "program"
UNITTEST = "unittest"

VERIFY = "verify"
DEARPYGUI = "dearpygui"
DESKTOP = "desktop"
TERMINAL = "terminal"
TKINTER = "tkinter"


DEARPYGUI = "dearpygui"
DESKTOP = "desktop"
FILE = "file"
PILLOW = "pillow"
PROGRAM = "program"
TERMINAL = "terminal"
TKINTER = "tkinter"
UNITTEST = "unittest"
VERIFICATION = "verification"




def verify():
    #import unittest
    unittest = __import__("unittest")
    import celestine.verify
    unittest.main()

def dearpygui():
    import dearpygui

def tkinter():
    import tkinter

def desktop():
    import desktop

def terminal():
    import terminal



PACKAGE = {
    DEARPYGUI: Package("DearPyGui", "dearpygui", "dearpygui", dearpygui),
    PILLOW: Package("Pillow", "PIL", "pillow", ""),
    TKINTER: Package("tkinter", "tkinter", "tkinter", tkinter),
    UNITTEST: Package("unittest", "unittest", "unittest", verify)
}


GUI = [
    TKINTER,
    DEARPYGUI
]

CONSOLE = [
    TERMINAL,
    DESKTOP,
    FILE
]
RUN = [
    PROGRAM,
    VERIFICATION
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





def main():
    parser = argparse.ArgumentParser(
        prog="celestine"
    )
    parser.add_argument(
        "-p", "--package",
        action="store_true",
        help="List all installed packages."
    )
    parser.add_argument(
        "-v", "--verify",
        action="store_true",
        help="Run unit tests."
    )


    parser.add_argument(
        "-r", "--run",
        default=PROGRAM,
        choices=RUN,
        help="Choose what you want to run."
    )
    parser.add_argument(
        "-m", "--mode",
        default=TERMINAL,
        choices=CONSOLE,
        help="Choose a console mode."
    )
    parser.add_argument(
        "-g", "--gui",
        default=DEARPYGUI,
        choices=GUI,
        help="Choose a gui to use."
    )
    parse = parser.parse_args()

    run = parse.run
    mode = parse.mode
    gui = parse.gui
    print(gui)
    print(parse)
    print(vars(parse))
    
    cow = {a:b for a,b in vars(parse).items() if b}
    print(cow)

    print(parse.package)
    if run == PROGRAM:
        pass
    elif run == VERIFICATION:
        pass

    if parse.package:
        pass

    if parse.verify:
        verify()


    import_package(gui)

    if check(gui, DESKTOP):
        import desktop

    if check(gui, TERMINAL):
        import terminal


try:
    main()
except ModuleNotFoundError:
    raise MissingPackageError()
