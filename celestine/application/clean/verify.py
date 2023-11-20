"""Package unittest."""

import unittest

from celestine import load
from celestine.data import CELESTINE
from celestine.data.directory import APPLICATION
from celestine.session.session import SuperSession
from celestine.typed import N
from celestine.window.container import Container as Page
from celestine.load

ERROR = "error"
MODULE = "module"
TARGET = "_test.py"
TEST = "test"


class Session(SuperSession):
    """"""


def modularize(path: S, begin: S) -> T[S, ...]:
    """"""
    relative = os.path.relpath(path, begin)
    (root, _) = os.path.splitext(relative)
    pure = pathlib.PurePath(root)
    parts = pure.parts
    return parts


def find(target: S) -> L[T[S, ...]]:
    """Find all project directories with this name."""
    begin = load.pathway.celestine()

    array = [
        modularize(directory, begin)
        for directory in walk_file(begin)
        if directory.endswith(target)
    ]
    return array


def main(_: Page) -> N:
    """Run the unittest library."""
    module = load.module(APPLICATION, TEST)
    paths = find(TARGET)
    for path in paths:
        dictionary = load.dictionary(*path)
        for item, value in dictionary.items():
            setattr(module, item, value)

    unittest.main(
        module,
        None,
        [CELESTINE],
        None,
        unittest.defaultTestLoader,
        False,
        2,
        False,
        True,
        True,
        ERROR,
    )
