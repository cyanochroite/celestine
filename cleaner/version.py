"""Run a bunch of auto formaters."""

import datetime

from celestine import (
    load,
    regex,
    stream,
)
from celestine.typed import (
    B,
    R,
    ignore,
)
from celestine.window.decorator import call

DIGIT = r"\d\d?"
array = [
    (
        [
            "CITATION.cff",
        ],
        [
            "date-released: 'YYYY-0M-0D'",
            "version: YYYY.MM.DD",
        ],
    ),
    (
        [
            "__init__.py",
            "celestine",
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
            "conf.py",
            "documentation",
        ],
        [
            'copyright = "YYYY, mem_dixy"',
            'release = "YYYY.MM.DD"',
            'version = "YYYY.MM.DD"',
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
]


@call
def version(**star: R) -> B:
    """"""
    ignore(star)
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
            pattern = pattern.replace("YY", DIGIT)
            pattern = pattern.replace("MM", DIGIT)
            pattern = pattern.replace("DD", DIGIT)
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


ignore(version)
