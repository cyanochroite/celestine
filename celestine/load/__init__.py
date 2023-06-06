"""Central place for loading and importing external files."""

import os
import sys

from celestine.data import CELESTINE
from celestine.typed import (
    CA,
    MT,
    TA,
    B,
    D,
    L,
    N,
    S,
)
from celestine.unicode import (
    FULL_STOP,
    LOW_LINE,
)

FN: TA = CA[[N], N]

FUNCTION = "<function"
PACKAGE = "package"

from . import path

path = path

from . import many

many = many


########################################################################


def package(base: S, *path: S) -> MT:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for item in path:
        file = getattr(file, item)
    if "from" not in repr(file):
        raise ModuleNotFoundError(f"Module failed to load: {name}")
    return file


def module(*path: S) -> MT:
    """Load an internal module from anywhere in the application."""
    return package(CELESTINE, *path)


########################################################################


def functions(_module: MT) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    _dictionary = vars(_module)
    items = _dictionary.items()
    iterable = {
        key: value
        for key, value in items
        if repr(value).startswith(FUNCTION)
    }
    return iterable


def attempt(*path: S) -> B:
    """Attempt to load a package and return the result."""
    try:
        module(*path)
        return True
    except ModuleNotFoundError:
        pass
    return False


def module_fallback(*path: S) -> MT:
    """
    Load an internal module from anywhere in the application.

    If the last item is none then load the package instead.
    """
    iterable = [*path]
    pop = iterable.pop(-1)
    fallback = module(*path) if pop else module(*iterable)
    return fallback


def dictionary(*path: S) -> D[S, S]:
    """Load from module all key value pairs and make it a dictionary."""
    _module = module(*path)
    _dictionary = vars(_module)
    mapping = {
        key: value
        for key, value in _dictionary.items()
        if not key.startswith(LOW_LINE)
    }
    return mapping


def argument_default(path: S) -> S:
    """"""
    array = argument(path)
    result = None
    for item in array:
        try:
            _ = module(path, item)
            result = item
        except ModuleNotFoundError:
            pass
    if not result:
        message = f"Failed to load any package in '{path}' directory."
        raise ReferenceError(message)
    return result


def module_to_name(_module: MT) -> S:
    """"""
    string = repr(_module)
    array = string.split("'")
    name = array[1]
    split = name.split(".")
    section = split[-1]
    return section


####


def method(name: S, *path: S):
    """"""
    return getattr(module(*path), name)


####


def argument(*path: S) -> L[S]:
    """
    Build a path to the selected package.

    Scan all items in directory.
    Return a list of items that are not private, such as '.private' or
    '_private'. (First letter is not a symbol.)
    Strip off all file extensions, if any.
    """
    directory = pathway(*path)
    try:
        folder = os.listdir(directory)
    except FileNotFoundError:
        return []

    splitext = os.path.splitext
    result = [splitext(file)[0] for file in folder if file[0].isalpha()]

    result.sort()
    return result


def pathway(*path: S) -> S:
    """"""
    _package = pathfinder()
    return os.path.join(_package, *path)


def pathfinder() -> S:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        _package = os.path.join(path, CELESTINE)
        if os.path.exists(_package):
            return _package
    return sys.path[0]


def package_dependency(name: S, fail) -> MT:
    """Attempt to make loading packages easier."""
    try:
        flag = package(CELESTINE, PACKAGE, name)
    except ModuleNotFoundError:
        flag = fail
    return flag
