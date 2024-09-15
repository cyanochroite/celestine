"""Run a bunch of auto formaters."""

import datetime
import io

from celestine import (
    load,
    regex,
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

array = [
    (
        [
            "CITATION.cff",
        ],
        [
            "version: YYYY.MM.DD",
            "date-released: 'YYYY-0M-0D'",
        ],
    ),
    (
        [
            "pyproject.toml",
        ],
        [
            'version = "YYYY.MM.DD"',
        ],
    ),
    (
        [
            "celestine",
            "__init__.py",
        ],
        [
            '"version": (YYYY, MM, DD),',
        ],
    ),
    (
        [
            "celestine",
            "literal.py",
        ],
        [
            'VERSION_NUMBER = "YYYY.MM.DD"',
        ],
    ),
    (
        [
            "documentation",
            "conf.py",
        ],
        [
            'copyright = "YYYY, mem_dixy"',
            'release = "YYYY.MM.DD"',
            'version = "YYYY.MM.DD"',
        ],
    ),
]


def run(name: S) -> N:
    """"""
    module = load.module(PACKAGE, name)
    linter = module.Linter(name)
    linter.run()


@call
def version(**star: R) -> B:
    """"""
    print("MOO")
    return True


@call
def licence(**star: R) -> B:
    """"""
    print("test")
    location = load.pathway("licence")
    files = load.walk_file(location, [], [])
    for file in files:
        string = io.StringIO()
        with stream.text.reader(file) as lines:
            for line in lines:
                character = normalize.characters(line)
                wrap = normalize.wrap_text(character)
                for text in wrap:
                    string.write(text)
        with stream.text.writer(file) as document:
            for line in string.getvalue():
                document.write(line)
    return True

