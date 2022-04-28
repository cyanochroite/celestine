import argparse


def _import(module):
    try:
        __import__(module)
        return True
    except ModuleNotFoundError:
        return False


DEARPYGUI = "DEARPYGUI"
DESKTOP = "DESKTOP"
PILLOW = "PILLOW"
TERMINAL = "TERMINAL"
TKINTER = "TKINTER"
UNITTEST = "UNITTEST"


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

GUI = {
    TERMINAL.lower(): "CAT",
    DESKTOP.lower(): "HAT",
    TKINTER.lower(): "PIG",
    DEARPYGUI.lower(): "DOG"
}


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


def main():
    parser = argparse.ArgumentParser(
        prog="celestine"
    )
    parser.add_argument(
        "-g", "--gui",
        default="dearpygui",
        choices=GUI,
        help="Choose a gui to use."
    )
    parse = parser.parse_args()

    gui = parse.gui.upper()

    if check(gui, DEARPYGUI):
        import main_dearpygui

    if check(gui, TKINTER):
        import main_tkinter

    if check(gui, DESKTOP):
        pass

    if check(gui, TERMINAL):
        pass

