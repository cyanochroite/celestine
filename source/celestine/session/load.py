"""Central place for loading and importing external files."""
import os.path
import sys

from celestine.keyword.unicode import FULL_STOP
from celestine.keyword.unicode import LOW_LINE

from celestine.keyword.all import CELESTINE


def attempt(name):
    """Attempt to load a package and return the result."""
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        pass
    return False


def path(one, *paths):
    """Load a file from absolute path."""
    _path = os.path.join(one, *paths)
    return _path


def module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *paths]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for _path in paths:
        file = getattr(file, _path)
    return file


def directory(_path):
    """Load file contents from a directory."""
    print(_path)


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


def argument(*paths):
    """
    Build a path to the selected package. Scan all items in directory.
    Return a list of items that are not private, such as '.private' or
    '_private'. (First letter is not a symbol.)
    Strip off all file extensions, if any.
    """
    join = os.path.join
    listdir = os.listdir
    splitext = os.path.splitext

    folder = listdir(join(sys.path[0], *paths))
    result = [splitext(file)[0] for file in folder if file[0].isalpha()]
    result.sort()
    return result
