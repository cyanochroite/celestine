"""Run a bunch of auto formaters."""

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
