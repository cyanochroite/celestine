"""Run a bunch of auto formaters."""

import io

from celestine import load
from celestine.file import (
    normalize,
    text_load,
    text_save,
)
from celestine.typed import (
    N,
    R,
    S,
)

PACKAGE = "package"


def run(name: S) -> N:
    """"""
    module = load.module(PACKAGE, name)
    package = module.Linter(name)
    package.run()


def clean(*, ring: R, **star) -> N:
    """"""
    print("clean begin")
    ring.package.pyupgrade.run()
    ring.package.pydocstringformatter.run()
    ring.package.autoflake.run()
    ring.package.isort.run()
    ring.package.black.run()
    print("clean finish")


def licence(**star):
    """"""
    location = load.pathway.pathway("licence")
    files = load.many.file(location, [], [])
    for file in files:
        string = io.StringIO()
        with text_load(file) as lines:
            for line in lines:
                character = normalize.character(line)
                wrap = normalize.wrap_text(character)
                for text in wrap:
                    string.write(text)
        with text_save(file) as document:
            for line in string.getvalue():
                document.write(line)
