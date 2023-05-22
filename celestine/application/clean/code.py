"""Run a bunch of auto formaters."""

from celestine import load
from celestine.file import (
    open_file,
    save_file,
)
from celestine.load import directory
from celestine.package import run


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

    todo = [
        "BG",
        "CS",
        "DA",
        "DE",
        "EL",
        "EN",
        "ES",
        "ET",
        "FI",
        "FR",
        "HR",
        "HU",
        "IT",
        "LT",
        "LV",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SK",
        "SL",
        "SV",
    ]

    location = load.pathway("licence")
    files = directory.file(location, [], [])
    for file in files:
        data = []
        lines = open_file(file)
        for line in lines:
            line = line.strip()
            line = line.replace("  ", " ")
            data.append(line)

        save_file("\n".join(data), file)
