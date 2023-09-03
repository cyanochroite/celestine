"""Run a bunch of auto formaters."""

import io
import re

from celestine import load
from celestine.file import (
    normalize,
    text_load,
    text_save,
    text_write,
    text_read,
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


array2 = {
    "../pyproject.toml": ["version = \"YYYY.MM.DD\""],

    "../CITATION.cff": [
        "version: YYYY.MM.DD",
        "date-released: 'YYYY-MM-DD'",
    ],

    "../documentation/conf.py": [
        "copyright = \"YYYY, mem_dixy\""
        "release = \"YYYY.MM.DD\"",
        "version = \"YYYY.MM.DD\"",
    ],
    "/data/__init__.py": ["VERSION_NUMBER = \"YYYY.MM.DD\""],

}

array1 = [
    (["pyproject.toml"], ["version = \"YYYY.MM.DD\""]),

    (["CITATION.cff"], [
        "version: YYYY.MM.DD",
        "date-released: 'YYYY-MM-DD'",
    ]),

    (["documentation", "conf.py"], [
        "copyright = \"YYYY, mem_dixy\""
        "release = \"YYYY.MM.DD\"",
        "version = \"YYYY.MM.DD\"",
    ]),

    (["/data/__init__.py"], ["VERSION_NUMBER = \"YYYY.MM.DD\""]),

]

array3 = [
    (
        ["pyproject.toml"],
        ["version = \"YYYY.MM.DD\""],
    ),
    (
        ["CITATION.cff"], [
            "version: YYYY.MM.DD",
            "date-released: 'YYYY-MM-DD'",
        ],
    ),
    (
        ["documentation", "conf.py"],
        [
            "copyright = \"YYYY, mem_dixy\""
            "release = \"YYYY.MM.DD\"",
            "version = \"YYYY.MM.DD\"",
        ],
    ),
    (
        ["/data/__init__.py"],
        ["VERSION_NUMBER = \"YYYY.MM.DD\""],
    ),
]

array = [
    (
        [
            "pyproject.toml",
        ],
        [
            "version = \"YYYY.MM.DD\"",
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
            "copyright = \"YYYY, mem_dixy\"",
            "release = \"YYYY.MM.DD\"",
            "version = \"YYYY.MM.DD\"",
        ],
    ),
    (
        [
            "celestine",
            "data",
            "__init__.py",
        ],
        [
            "VERSION_NUMBER = \"YYYY.MM.DD\"",
        ],
    ),
]


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

    location = load.pathway.pathway("licence")
    print(location)

    file = load.pathway.pathway("../pyproject.toml")
    text = text_read(file)
    # text = re.sub(r"(version)", "1234-56-78", text)
    text = sub(text)
    print(text)
    text_write(file, text)

