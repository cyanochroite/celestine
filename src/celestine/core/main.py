import argparse

from celestine.data.exit import EXIT


def import_package(package, module):
    __import__(".".join(["celestine", "package", package, module]))


def import_module(module):
    __import__(".".join(["celestine", "module", module]))


class Package():
    def __init__(self, name, external, internal):
        self.name = name
        self.external = external
        self.internal = internal
        self.imported = True

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


DEARPYGUI = "dearpygui"
DESKTOP = "desktop"
FILE = "file"
PILLOW = "pillow"
PROGRAM = "program"
TERMINAL = "terminal"
TKINTER = "tkinter"
UNITTEST = "unittest"
VERIFICATION = "verification"


VERIFY = "verify"
DEARPYGUI = "dearpygui"
DESKTOP = "desktop"
TERMINAL = "terminal"
TKINTER = "tkinter"


PACKAGE = {
    DEARPYGUI: Package("DearPyGui", "dearpygui", "dearpygui"),
    PILLOW: Package("Pillow", "PIL", "pillow"),
    TKINTER: Package("tkinter", "tkinter", "tkinter"),
    UNITTEST: Package("unittest", "unittest", "unittest")
}


MODE = [
    DEARPYGUI,
    TERMINAL,
    TKINTER,
    VERIFY
]

GUI = [
    DEARPYGUI,
    DESKTOP,
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


def main():
    #raise MissingPackageError()

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
        default=TERMINAL,
        choices=MODE,
        help="Choose a mode to opperate in."
    )

    parser.add_argument(
        "-g", "--gui",
        default=TERMINAL,
        choices=GUI,
        help="Choose a mode to opperate in."
    )
    parse = parser.parse_args()

    mode = parse.mode

    if mode == VERIFY:
        return EXIT.TEST

    #import_package(mode, "main")

    # This next section is weird.
    # Revisit once we start parsing multiple parameters.

    gui = TERMINAL

    if mode == TERMINAL:
        gui = TERMINAL

    if mode == DEARPYGUI:
        gui = DEARPYGUI

    if mode == DESKTOP:
        gui = DESKTOP

    if mode == TKINTER:
        gui = TKINTER

    gui = import_module(gui)

    return EXIT.SUCCESS



