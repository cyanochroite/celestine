import argparse


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


DEARPYGUI = "dearpygui"
DESKTOP = "desktop"
FILE = "file"
PILLOW = "pillow"
PROGRAM = "program"
TERMINAL = "terminal"
TKINTER = "tkinter"
UNITTEST = "unittest"
VERIFICATION = "verification"


class package():
    def __init__(self, name, module, install):
        self.name = name
        self.module = module
        self.install = install
        self.imported = self._import(module)

    def _import(self, module):
        try:
            __import__(module)
            return True
        except ModuleNotFoundError:
            return False


PACKAGE = {
    DEARPYGUI: package("DearPyGui", "dearpygui", "pip install dearpygui"),
    PILLOW: package("Pillow", "PIL", "pip install Pillow"),
    TKINTER: package("tkinter", "tkinter", "Installing it with python."),
    UNITTEST: package("unittest", "unittest", "Installing it with python.")
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
    

    if parse.package:
        pass

    if parse.verify:
        check_package(UNITTEST)
        import celestine.verify




    print(parse.package)
    if run == PROGRAM:
        pass
    elif run == VERIFICATION:
        pass


    if check(gui, DEARPYGUI):
        import dearpygui

    if check(gui, TKINTER):
        import tkinter

    if check(gui, DESKTOP):
        import desktop

    if check(gui, TERMINAL):
        import terminal

