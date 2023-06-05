"""Central place for loading and importing external files."""

import os
import sys

from celestine.data import CELESTINE
from celestine.typed import S
from celestine.unicode import NONE


def pathfinder() -> S:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        _package = os.path.join(path, CELESTINE)
        if os.path.exists(_package):
            return _package
    return sys.path[0]


def pathway(*path: S) -> S:
    """"""
    _package = pathfinder()
    return os.path.join(_package, *path)


def python(*path: S) -> S:
    """"""
    return NONE.join([pathway(*path), PYTHON_EXTENSION])


def asset(item: S) -> S:
    """"""
    return pathway("data", item)
