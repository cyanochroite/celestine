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
def clean(**star: R) -> B:
    """"""
    pyupgrade.run()
    pydocstringformatter.run()
    autoflake.run()
    isort.run()
    black.run()
    return True


@call
def licence(**star: R) -> B:
    """"""
    location = load.pathway("licence")
    files = load.walk_file(location, [], [])
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


@call
def version(**star: R) -> B:
    """"""
    date = datetime.datetime.now(datetime.UTC)

    year = str(date.year)
    month = str(date.month)
    day = str(date.day)

    month_fill = month.zfill(2)
    day_fill = day.zfill(2)

    for path, keys in array:
        file = load.pathway_root(*path)
        text = stream.text.load(file)

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
            repl = repl.replace("YYYY", year)
            repl = repl.replace("MM", month)
            repl = repl.replace("DD", day)

            repl = repl.replace("0M", month_fill)
            repl = repl.replace("0D", day_fill)

            text = regex.replace(pattern, repl, text)

        stream.text.save(text, file)
    return True
