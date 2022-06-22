import sys
import os.path

current_directory = sys.path[0]
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

import celestine.core.load as load
from celestine.data.session import make
from celestine.window.main import main

DEARPYGUI = "dearpygui"
CELESTINE = "celestine"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"

PACKAGE = [
    DEARPYGUI,
    CELESTINE,
    CURSES,
    TKINTER,
    UNITTEST
]

package = next(  # need to message user when package not installed
    (
        argv
        for argv in sys.argv[1:]  # skip first argument
        for name in PACKAGE
        if argv == name and load.attempt(name)  # package is installed
    ),
    CELESTINE
)

if package != CELESTINE:
    sys.argv = [sys.argv[0]]  # clear argument list

if package == UNITTEST:
    # Import everything so we can find tests.
    # This can only be done from the top level, so that is why it is here.
    from celestine.package.unittest import *
    # Also we only attempt to import unittest if the user requested it.
    # This is because it could not be installed and would error otherwise.
    import unittest
    unittest.main()  # this function will terminate the program

module = load.package(package)
window = module.Window()

session = make(parent_directory)
run = main(session)
window.run(run)

sys.exit()
