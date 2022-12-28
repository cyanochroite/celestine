"""Central place for loading and importing external files."""

import os
import sys
import types
import typing

from celestine.text import CELESTINE

from celestine.text.stream import FILE_NAME_EXTENSION

from celestine.text.unicode import FULL_STOP
from celestine.text.unicode import LOW_LINE
from celestine.text.unicode import NONE


def attempt(*path: str) -> bool:
    """Attempt to load a package and return the result."""
    try:
        module(*path)
        return True
    except ModuleNotFoundError:
        pass
    return False


def module(*path: str) -> types.ModuleType:
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *path]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for _path in path:
        file = getattr(file, _path)
    if "from" not in repr(file):
        raise ModuleNotFoundError(F"Module failed to load: {name}")
    return file


def module_fallback(*path: str) -> types.ModuleType:
    """
    Load an internal module from anywhere in the application.
    If the last item is none then load the package instead.
    """
    iterable = [*path]
    return module(*path) if iterable.pop(-1) else module(*iterable)


def dictionary(*path: str) -> typing.Dict[str, str]:
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


def function(_module: types.ModuleType) -> list[typing.Callable[[None], None]]:
    """
    Load from module all functions and turn them into dictionary.
    """
    _dictionary = vars(_module)
    mapping = [
        value
        for key, value
        in _dictionary.items()
        if repr(value).startswith("<function") and
        not key.startswith("_")
    ]
    return mapping


def pathway(*path: str) -> str:
    """"""
    return os.path.join(sys.path[0], CELESTINE, *path)


def python(*path: str) -> str:
    """"""
    return NONE.join([pathway(*path), FILE_NAME_EXTENSION])


def argument_default(path: str) -> str:
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


def argument(*path: str) -> list[str]:
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
