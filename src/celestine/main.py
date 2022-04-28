import sys
import os
import textwrap

import argparse

DEARPYGUI = True
PILLOW = True
TKINTER = True
UNITTEST = True

try:
    import dearpygui
except ModuleNotFoundError as error:
    DEARPYGUI = False

try:
    import PIL
except ModuleNotFoundError as error:
    PILLOW = False

try:
    import tkinter
except ModuleNotFoundError as error:
    TKINTER = False

try:
    import unittest
except ModuleNotFoundError as error:
    UNITTEST = False

PACKAGE = [
    DEARPYGUI,
    PILLOW,
    TKINTER,
    UNITTEST
]

print(PACKAGE)



__version__ = "0.1.2.3"

OK = 0
ERR = 1
FAIL_UNDER = 2


COMMANDS = {
    'annotate': 1,
    'combine': 2,
    'debug': 3,
    'erase': 4,
    'help': 5,
    'html': 6,
    'json': 7,
    'lcov': 8,
    'report': 9,
    'run': 10,
    'xml': 11
}


HELP_TOPICS = {
    'help': """\
        Coverage.py, version {__version__} {extension_modifier}
        Measure, collect, and report on code coverage in Python programs.

        usage: {program_name} <command> [options] [args]

        Commands:
            annotate    Annotate source files with execution information.
            combine     Combine a number of data files.
            debug       Display information about the internals of coverage.py
            erase       Erase previously collected coverage data.
            help        Get help on using coverage.py.
            html        Create an HTML report.
            json        Create a JSON report of coverage results.
            lcov        Create an LCOV report of coverage results.
            report      Report coverage stats on modules.
            run         Run a Python program and measure code execution.
            xml         Create an XML report of coverage results.

        Use "{program_name} help <command>" for detailed help on any command.
    """,

    'minimum_help': """\
        Code coverage for Python, version {__version__} {extension_modifier}.  Use '{program_name} help' for help.
    """,

    'version': """\
        Coverage.py, version {__version__} {extension_modifier}
    """,
}


def show_help(error=None, topic=None, parser=None):
    """Display an error message, or the named topic."""
    assert error or topic or parser

    program_path = sys.argv[0]
    if program_path.endswith(os.path.sep + '__main__.py'):
        # The path is the main module of a package; get that path instead.
        program_path = os.path.dirname(program_path)
    program_name = os.path.basename(program_path)
    help_params = dict({"__version__": __version__, "__url__": "happy place dot com"})
    help_params['program_name'] = program_name
    help_params['extension_modifier'] = 'without C extension'

    if error:
        print(error, file=sys.stderr)
        print(f"Use '{program_name} help' for help.", file=sys.stderr)
    elif parser:
        print(parser.format_help().strip())
        print()
    else:
        help_msg = textwrap.dedent(HELP_TOPICS.get(topic, '')).strip()
        if help_msg:
            print(help_msg.format(**help_params))
        else:
            print(f"Don't know topic {topic!r}")
    print("Full documentation is at {__url__}".format(**help_params))

GUI = [
    "dearpygui",
    "terminal",
    "tkinter"
]

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
