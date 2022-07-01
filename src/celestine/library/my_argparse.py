"""Wrapper around argparse library."""
import argparse
import abc

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

MORE_ITERTOOLS = "more_itertools"
PILLOW = "pillow"


EXTENSION = [
    MORE_ITERTOOLS,
    PILLOW
]

####

PACKAGE = "package"

DEARPYGUI = "dearpygui"
CELESTINE = "celestine"
CURSES = "curses"
TKINTER = "tkinter"
UNITTEST = "unittest"


LANGUAGE = "language"

ENGLISH = "english"
FRENCH = "french"
GERMAN = "german"


PYTHON = "python"

PYTHON_3_6 = "3.6"
PYTHON_3_7 = "3.7"
PYTHON_3_8 = "3.8"
PYTHON_3_9 = "3.9"
PYTHON_3_10 = "3.10"
PYTHON_3_11 = "3.11"

PACKAGE = [
    CELESTINE,
    CURSES,
    DEARPYGUI,
    TKINTER,
    UNITTEST
]

LANGUAGE = [
    ENGLISH,
    FRENCH,
    GERMAN
]

PYTHON = [
    PYTHON_3_6,
    PYTHON_3_7,
    PYTHON_3_8,
    PYTHON_3_9,
    PYTHON_3_10,
    PYTHON_3_11
]

parser = argparse.ArgumentParser(prog=CELESTINE)

parser.add_argument(
    "package",
    nargs="*",
    default=CELESTINE,
    choices=PACKAGE,
    help="Choose a mode to opperate in."
)

parser.add_argument(
    "-l, --language",
    default=ENGLISH,
    choices=LANGUAGE,
    help="Choose a language."
)

parser.add_argument(
    "-p, --python",
    default=PYTHON_3_10,
    choices=PYTHON,
    help="Tell me which python version you are using."
)

####

parser.add_argument(
    "-a", "--available",
    action="store_true",
    help="List all installed packages."
)


parser.add_argument(
    "-i", "--ini",
    action=STORE,
    nargs=1,
    help="List all installed packages."
)

parse = vars(parser.parse_args())


def parse_package(_package):
    """Parses a package and tells you why it didn't work."""
    if _package == CELESTINE:
        return CELESTINE
    for name in _package:
        if load.attempt(name):
            return name
        print(F"Package '{name}' is not installed.")
    return CELESTINE


package = parse["package"]
language = parse["l, __language"]
python = parse["p, __python"]


class Parser():
    def __init__(self):
        self.argument = []

        parser = argparse.ArgumentParser(prog=CELESTINE)

        parser.add_argument(
            "package",
            nargs="*",
            default=CELESTINE,
            choices=PACKAGE,
            help="Choose a mode to opperate in."
        )

        parser.add_argument(
            "-l, --language",
            default=ENGLISH,
            choices=LANGUAGE,
            help="Choose a language."
        )

        parser.add_argument(
            "-p, --python",
            default=PYTHON_3_10,
            choices=PYTHON,
            help="Tell me which python version you are using."
        )

        self.parser = parser

    def parse(self):
        args = ["python", "language"]
        parse = vars(self.parser.parse_args())
        for argument in self.argument:
            a = argument.key
            b = argument.value
            c = parse[b]
            setattr(self, argument.key, parse[argument.value])

    def add_argument(self):
        parser.add_argument(
            "-i", "--ini",
            action=STORE,
            nargs=1,
            help="List all installed packages."
        )

    def add_argument(self, argument):
        self.argument.append(argument)


class Argument(abc.ABC):
    """argparse argument"""

    def __init__(self, name):
        parser.add_argument(
            self.name(name),
            action=STORE,
            nargs=1,
            help="List all installed packages."
        )

    def __init__(self, name):
        self.name = name

    @property
    def key(self):
        """Format name."""
        return self.name

    @property
    @abc.abstractmethod
    def value(self):
        """Format name."""
        raise NotImplementedError


class Positional(Argument):
    """argparse positional argument"""

    @property
    def value(self):
        return self.name


class Optional(Argument):
    """argparse optional argument"""

    @property
    def value(self):
        return F"{self.name[0]}, __{self.name}"


parser = Parser()

parser.add_argument(Positional("package"))
parser.add_argument(Optional("language"))
parser.add_argument(Optional("python"))

parser.parse()
print(parser.python)
print("done")



def parse_package(package, default):
    """Parses a package and tells you why it didn't work."""
    if package == default:
        return default
    for name in package:
        if load.attempt(name):
            return name
        print(F"Package '{name}' is not installed.")
    return default
