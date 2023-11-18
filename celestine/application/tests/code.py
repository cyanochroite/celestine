"""Package unittest."""

import unittest

from celestine import load
from celestine.data import CELESTINE
from celestine.data.directory import APPLICATION
from celestine.load import pathway
from celestine.load.many import python
from celestine.typed import (
    H,
    N,
    R,
)

from .data import (
    ERROR,
    TESTS,
)


def main(*, hold: H, **star: R) -> N:
    """Run the unittest library."""
    module = load.module(APPLICATION, TESTS)
    top = pathway.pathway()
    files = python(top, [], [])
    files = list(files)
    paths = [file for file in files if file.name.startswith("test")]
    for path in paths:
        #  This is a really bad hack to convert path names.
        text = str(path)
        ending = text.split(".py")
        split = ending[0].split("celestine")
        replace = split[1].replace("\\", "/")
        iterable = replace.split("/")
        done = filter(None, iterable)
        dictionary = load.dictionary(*done)
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
