import os.path
from celestine.data.unicode import FULL_STOP


CELESTINE = "celestine"
EXTENSION = "extension"


def file(session, iterable):
    root = session["Application"]["directory"]
    carwash = [root, CELESTINE] + iterable
    return os.path.join(*tuple(carwash))
# return os.path.join([root, CELESTINE] + iterable)


def module(*paths):
    iterable = [CELESTINE] + list(paths)
    name = FULL_STOP.join(iterable)
    module = __import__(name)
    for path in paths:
        module = getattr(module, path)
    return module


def extension(name):
    try:
        return __import__(name)
    except ModuleNotFoundError:
        pass
    return module(EXTENSION, name)

def attempt(name):
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        pass
    return False

