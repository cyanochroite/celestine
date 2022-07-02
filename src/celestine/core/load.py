"""Central place for loading and importing external files."""
import os.path

from celestine.data.unicode import FULL_STOP


CELESTINE = "celestine"
EXTENSION = "extension"
PACKAGE = "package"
LANGUAGE = "language"
PYTHON = "python"

def attempt(name):
    """Attempt to load a package and return the result."""
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        pass
    return False


def extension(name):
    """Load an internal module from the "extension" directory."""
    try:
        return __import__(name)
    except ModuleNotFoundError:
        pass
    return module(EXTENSION, name)


def file(session, iterable):
    """Load a file from absolute path."""
    root = session.directory
    path = [root, CELESTINE] + iterable
    return os.path.join(*tuple(path))


def _module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE] + list(paths)
    name = FULL_STOP.join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item


def package(name):
    """Load an internal module from the "package" directory."""
    return module(PACKAGE, name)
