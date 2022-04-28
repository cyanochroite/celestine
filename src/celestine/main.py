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

PACKAGE = {
    DEARPYGUI: _import("dearpygui"),
    PILLOW: _import("PIL"),
    TKINTER: _import("tkinter"),
    UNITTEST: _import("unittest")
}

GUI = {
    TERMINAL: TERMINAL.lower(),
    DESKTOP: DESKTOP.lower(),
    TKINTER: TKINTER.lower(),
    DEARPYGUI: DEARPYGUI.lower()
}

GUI = [
    TERMINAL.lower(),
    DESKTOP.lower(),
    TKINTER.lower(),
    DEARPYGUI.lower()
]


print(PACKAGE)


__version__ = "0.1.2.3"

OK = 0
ERROR = 1



def main() -> int:
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
    print(parse.gui)

    return OK
