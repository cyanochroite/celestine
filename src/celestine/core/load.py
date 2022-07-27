"""Central place for loading and importing external files."""
import os.path

from celestine.keyword.unicode import FULL_STOP
from celestine.keyword.unicode import LOW_LINE

from celestine.keyword import language
from celestine.keyword.main import CELESTINE
import keyword


def attempt(name):
    """Attempt to load a package and return the result."""
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        pass
    return False


def path(*paths):
    """Load a file from absolute path."""
    path = os.path.join(*paths)
    return path


def module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *paths]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for path in paths:
        file = getattr(file, path)
    return file


def directory(path):
    pass


def dictionary(module):
    """Load from module all key value pairs and turn them into dictionary."""
    dictionary = vars(module)
    mapping = {
        key: value
        for key, value
        in dictionary.items()
        if not key.startswith(LOW_LINE)
    }
    return mapping
