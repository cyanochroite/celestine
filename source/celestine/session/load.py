"""Central place for loading and importing external files."""
import os.path
import sys

from celestine.string.unicode import FULL_STOP
from celestine.string.unicode import LOW_LINE

from celestine.string.all import CELESTINE


def attempt(name):
    """Attempt to load a package and return the result."""
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        pass
    return False


def module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *paths]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for _path in paths:
        file = getattr(file, _path)
    return file


def dictionary(_module):
    """
    Load from module all key value pairs and turn them into dictionary.
    """
    _dictionary = vars(_module)
    mapping = {
        key: value
        for key, value
        in _dictionary.items()
        if not key.startswith(LOW_LINE)
    }
    return mapping


def pathway(*paths):
    return os.path.join(sys.path[0], CELESTINE, *paths)


def argument_default(path):
    array = argument(path)
    result = None
    for item in array:
        try:
            module(path, item)
            result = item
        except (SyntaxError, ModuleNotFoundError):
            pass
    if not result:
        message = F"Failed to load any package in '{path}' directory."
        raise ReferenceError(message)
    return result


def argument(*paths):
    """
    Build a path to the selected package. Scan all items in directory.
    Return a list of items that are not private, such as '.private' or
    '_private'. (First letter is not a symbol.)
    Strip off all file extensions, if any.
    """
    directory = pathway(*paths)
    folder = os.listdir(directory)

    splitext = os.path.splitext
    result = [splitext(file)[0] for file in folder if file[0].isalpha()]

    result.sort()
    return result
