"""Package unittest."""

import unittest

from celestine import (
    language,
    load,
)
from celestine.data import (
    call,
    draw,
)
from celestine.data.directory import APPLICATION
from celestine.interface import View
from celestine.literal import CELESTINE
from celestine.session.session import SuperSession
from celestine.typed import (
    B,
    N,
    R,
)

ERROR = "error"
MODULE = "module"
TARGET = "_test.py"
TESTS = "test"


class Session(SuperSession):
    """"""


@call
def code(**star: R) -> B:
    """Run the unittest library."""
    module = load.module(APPLICATION, TESTS)
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

    return True


@draw
def main(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.button(
            "button",
            "code",
            text=language.TRANSLATOR_MAIN_BUTTON,
        )
