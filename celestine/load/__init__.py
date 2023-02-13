"""Central place for loading and importing external files."""

import os
import sys

from celestine.text import CELESTINE

from celestine.text.stream import FILE_NAME_EXTENSION

from celestine.typed import B
from celestine.typed import D
from celestine.typed import L
from celestine.typed import MT
from celestine.typed import S

from celestine.unicode import FULL_STOP
from celestine.unicode import LOW_LINE
from celestine.unicode import NONE


from .function import function
from .function import function_name
from .function import function_value


def attempt(*path: S) -> B:
    """Attempt to load a package and return the result."""
    try:
        module(*path)
        return True
    except ModuleNotFoundError:
        pass
    return False


def module(*path: S) -> MT:
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *path]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for _path in path:
        file = getattr(file, _path)
    if "from" not in repr(file):
        raise ModuleNotFoundError(F"Module failed to load: {name}")
    return file


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
    """
    Load from module all key value pairs and turn them into dictionary.
    """
    _module = module(*path)
    _dictionary = vars(_module)
    mapping = {
        key: value
        for key, value
        in _dictionary.items()
        if not key.startswith(LOW_LINE)
    }
    return mapping


def pathfinder() -> S:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        package = os.path.join(path, CELESTINE)
        if os.path.exists(package):
            return package
    return sys.path[0]


def pathway(*path: S) -> S:
    """"""
    package = pathfinder()
    return os.path.join(package, *path)


def python(*path: S) -> S:
    """"""
    return NONE.join([pathway(*path), FILE_NAME_EXTENSION])


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
        message = F"Failed to load any package in '{path}' directory."
        raise ReferenceError(message)
    return result


def argument(*path: S) -> L[S]:
    """
    Build a path to the selected package. Scan all items in directory.
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


def module_to_name(_module: MT) -> S:
    """"""
    string = repr(_module)
    array = string.split("'")
    name = array[1]
    split = name.split(".")
    section = split[-1]
    return section
