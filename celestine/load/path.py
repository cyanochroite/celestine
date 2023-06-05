"""Central place for loading and importing external files."""

import os
import pathlib
import sys

from celestine.data import CELESTINE
from celestine.typed import S
from celestine.unicode import NONE


def pathfinder() -> S:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


def pathway(*path: S) -> S:
    """"""
    _package = pathfinder()
    return os.path.join(_package, *path)


def python(*path: S) -> S:
    """"""
    return NONE.join([pathway(*path), PYTHON_EXTENSION])


#########


def asset(item: S) -> S:
    """"""
    return pathway("data", item)
