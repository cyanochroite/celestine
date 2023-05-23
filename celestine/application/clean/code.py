"""Run a bunch of auto formaters."""

import io
from celestine import load
from celestine.file import (
    open_file,
    save_file,
)
from celestine.load import directory
from celestine.package import run

from celestine.file import normalize


def clean(**star):
    """"""
    print("clean start")
    run("pyupgrade")
    run("pydocstringformatter")
    run("autoflake")
    run("isort")
    run("black")
    print("clean finish")


def licence(**star):
    """"""

    split = "\n\n"

    location = load.pathway("licence")
    files = directory.file(location, [], [])
    for file in files:
        string = io.StringIO()

        text = open_file(file)
        lines = text.split(split)
        for line in lines:
            character = normalize.character(line)
            newline = normalize.whitespace(character)
            whitespace = normalize.whitespace(newline)
            punctuation = normalize.punctuation(whitespace)
            newer = normalize.wrap_text(punctuation)
            for stuff in newer:
                string.write(stuff)

            string.write(split)

        save_file(string.getvalue(), file)
        #save_file(split.join(data), file)







