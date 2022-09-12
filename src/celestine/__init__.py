""""this is a package"""
from celestine.core import load
from celestine.session import Session

from celestine.keyword.all import CELESTINE
from celestine.keyword.unicode import FULL_STOP


def module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *paths]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for _path in paths:
        file = getattr(file, _path)
    return file


def main(directory, argv, exit_on_error):
    """Run the main program."""
    session = Session(directory, argv, exit_on_error)
    return session.main()
