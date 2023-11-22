"""Run a bunch of auto formaters."""

import datetime
import io
import re

from celestine import stream
from celestine import load
from celestine.data import normalize
from celestine.typed import (
    H,
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
            "date-released: 'YYYY-0M-0D'",
        ],
    ),
    (
        [
            "documentation",
            "conf.py",
        ],
        [
            'copyright = "YYYY, mem_dixy"',
            'release = "YYYY-0M-0D"',
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


def clean(*, hold: H, **star: R) -> N:
    """"""
    # TODO: This is breaking the language files. Find out why.
    # hold.package.pyupgrade.run()
    hold.package.pydocstringformatter.run()
    hold.package.autoflake.run()
    hold.package.isort.run()
    hold.package.black.run()


def licence(**star: R):
    """"""
    location = load.pathway("licence")
    files = load.many_file(location, [], [])
    for file in files:
        string = io.StringIO()
        with stream.text.reader(file) as lines:
            for line in lines:
                character = normalize.character(line)
                wrap = normalize.wrap_text(character)
                for text in wrap:
                    string.write(text)
        with stream.text.writer(file) as document:
            for line in string.getvalue():
                document.write(line)


def version(**star: R):
    """"""
    date = datetime.datetime.now(datetime.UTC)

    year1 = str(date.year)
    month1 = str(date.month)
    day1 = str(date.day)

    month0 = month1.zfill(2)
    day0 = day1.zfill(2)

    for path, keys in array:
        file = load.pathway_root(*path)
        text = fuel.text.load(file)

        for key in keys:
            pattern = key

            pattern = pattern.replace("0Y", "YY")
            pattern = pattern.replace("0M", "MM")
            pattern = pattern.replace("0D", "DD")

            pattern = pattern.replace("(", r"\(")
            pattern = pattern.replace("YY", r"\d\d?")
            pattern = pattern.replace("MM", r"\d\d?")
            pattern = pattern.replace("DD", r"\d\d?")
            pattern = pattern.replace(")", r"\)")

            repl = key
            repl = repl.replace("YYYY", year1)
            repl = repl.replace("MM", month1)
            repl = repl.replace("DD", day1)

            repl = repl.replace("0M", month0)
            repl = repl.replace("0D", day0)

            string = text
            count = 1
            flags = 0

            text = re.sub(pattern, repl, string, count, flags)
            fuel.text.save(file, text)
