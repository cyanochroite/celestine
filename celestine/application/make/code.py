"""Run a bunch of auto formaters."""

import io

from celestine import (
    load,
    stream,
)
from celestine.data import (
    call,
    normalize,
)
from celestine.package import (
    autoflake,
    black,
    isort,
    pydocstringformatter,
    pyupgrade,
)
from celestine.typed import (
    B,
    N,
    R,
    S,
)

PACKAGE = "package"


def run(name: S) -> N:
    """"""
    module = load.module(PACKAGE, name)
    linter = module.Linter(name)
    linter.run()


@call
def clean(**star: R) -> B:
    """"""
    pyupgrade.run()
    pydocstringformatter.run()
    autoflake.run()
    isort.run()
    black.run()
    return True


@call
def unicode(**star: R) -> B:
    """"""
    path = load.pathway()
    include = [
        ".py",
        ".txt",
    ]
    exclude = [
        ".git",
        ".github",
        ".mypy_cache",
        ".ruff_cache",
        "__pycache__",
    ]
    files = load.walk_file(path, include, exclude)
    for file in files:
        string_builder = io.StringIO()
        with stream.text.reader(file) as lines:
            for line in lines:
                character = normalize.characters(line)
                wrap = normalize.wrap_text(character)
                for text in wrap:
                    string_builder.write(text)
        with stream.text.writer(file) as document:
            for line in string_builder.getvalue():
                document.write(line)
    return True
