import argparse

DEARPYGUI = "dearpygui"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"


PACKAGE = [
    DEARPYGUI,
    CURSES,
    TKINTER,
    UNITTEST,
    None
]






#parser = argparse.ArgumentParser(prog=CELESTINE)
parser = argparse.ArgumentParser()
parser.add_argument(
        "package",
        nargs="*",
        default=CURSES,
        choices=PACKAGE,
        help="Choose a mode to opperate in."
    )

parse = parser.parse_args()

package = parse.package[0]
