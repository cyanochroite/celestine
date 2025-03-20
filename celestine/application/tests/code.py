"""Package unittest."""

import unittest

from celestine import load
from celestine.data import (
    CELESTINE,
    call,
)
from celestine.data.directory import APPLICATION
from celestine.typed import (
    B,
    H,
    R,
)

from .data import (
    ERROR,
    TESTS,
)


@call
def main(hold: H, **star: R) -> B:
    """Run the unittest library."""
    module = load.module(APPLICATION, TESTS)
    top = load.pathway()
    files = load.walk_python(top, [], [])
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
        module = load.module(*done)
        dictionary = load.dictionary(module)
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
