"""Run a bunch of auto formaters."""

import datetime
import io
import re

from celestine import load
from celestine.file import (
    normalize,
    text_load,
    text_read,
    text_save,
    text_write,
)
from celestine.typed import (
    N,
    R,
    S,
)

PACKAGE = "package"


array = [
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
            "CITATION.cff",
        ],
        [
            "version: YYYY.MM.DD",
            "date-released: 'YYYY-MM-DD'",
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
    (
        [
            "celestine",
            "data",
            "__init__.py",
        ],
        [
            'VERSION_NUMBER = "YYYY.MM.DD"',
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
]


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


def version(**star):
    """"""

    def sub(string):
        pattern = ""
        repl = ""
        # string = ""
        count = 1
        flags = re.ASCII | re.MULTILINE

        date = "\\d{4}\\.\\d{2}\\.\\d{2}"
        now = "1234.56.78"

        find = 'version = "*"'

        pattern = find.replace("*", date)
        repl = find.replace("*", now)
        return re.sub(pattern, repl, string, count, flags)

    date = datetime.datetime.now(datetime.UTC)

    year = str(date.year).zfill(4)
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)

    for item in array:
        path, keys = item

        file = load.pathway.pathway_root(*path)
        text = text_read(file)

        for key in keys:
            pattern = key
            pattern = pattern.replace("YY", r"\d\d")
            pattern = pattern.replace("MM", r"\d\d")
            pattern = pattern.replace("DD", r"\d\d")

            pattern = pattern.replace("(", r"\(")
            pattern = pattern.replace(")", r"\)")

            repl = key
            repl = repl.replace("YYYY", year)
            repl = repl.replace("MM", month)
            repl = repl.replace("DD", day)

            string = text
            count = 1
            flags = 0

            text = re.sub(pattern, repl, string, count, flags)
            text_write(file, text)
