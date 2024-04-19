""""""

import importlib
import importlib.abc
import importlib.machinery
import os
import pathlib
import sys

import package
from celestine.typed import (
    LS,
    OS,
    B,
    M,
    N,
    P,
    R,
    S,
)
from celestine.unicode import FULL_STOP

CELESTINE = "celestine"


def _package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


def _project_path() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


def magic(name: S) -> M:
    thing = _package(f"celestine.package._{name}")
    call = getattr(thing, "Package")
    module = call(name)
    return module


autoflake = magic("autoflake")
black = magic("black")
blender = magic("blender")
curses = magic("curses")
dearpygui = magic("dearpygui")
isort = magic("isort")
pillow = magic("pillow")
platformdirs = magic("platformdirs")
pydocstringformatter = magic("pydocstringformatter")
pygame = magic("pygame")
pyupgrade = magic("pyupgrade")
tkinterpy = magic("tkinter")
