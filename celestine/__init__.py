""""""

import importlib

from celestine import bank
from celestine.session import begin_session
from celestine.typed import (
    LS,
    B,
    M,
    N,
    R,
    S,
)


def _package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = ".".join(iterable)
    result = importlib.import_module(name)
    return result


def magic(name: S) -> M:
    thing = _package(f"celestine.package._{name}")
    call = getattr(thing, "Package")
    module = call(name)
    return module


def more():
    package = importlib.import_module("celestine.package")

    package.autoflake = magic("autoflake")
    package.black = magic("black")
    package.blender = magic("blender")
    package.curses = magic("curses")
    package.dearpygui = magic("dearpygui")
    package.isort = magic("isort")
    package.pillow = magic("pillow")
    package.platformdirs = magic("platformdirs")
    package.pydocstringformatter = magic("pydocstringformatter")
    package.pygame = magic("pygame")
    package.pyupgrade = magic("pyupgrade")
    package.tkinterpy = magic("tkinter")


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    # load this data
    more()
    begin_session(argument_list, exit_on_error, **star)

    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view
