"""Package unittest."""

import unittest

from celestine import load
from celestine.data import call
from celestine.typed import (
    B,
    R,
)


@call
def test(**star: R) -> B:
    """Run the unittest library."""
    module = load.module("application", "make", "test")
    top = load.pathway()
    files = load.walk_python(top, [], [])
    paths = [file for file in files if file.stem.endswith("test")]
    for path in paths:
        #  This is a really bad hack to convert path names.
        text = str(path)
        ending = text.split(".py")
        split = ending[0].split("celestine")
        replace = split[1].replace("\\", "/")
        iterable = replace.split("/")
        done = filter(None, iterable)
        dictionary = load.dictionary(load.module(*done))
        for item, value in dictionary.items():
            setattr(module, item, value)

    unittest.main(
        module,
        None,
        ["celestine"],
        None,
        unittest.defaultTestLoader,
        False,
        2,
        False,
        True,
        True,
        "error",
    )

    return True
