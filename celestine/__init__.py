""""""

import importlib
from celestine import bank, load
from celestine.typed import (
    LS,
    B,
    N,
    S,
    M,
    R,
)


def loader(name: S) -> M:
    """"""
    thing = load.package("celestine", "package", name)
    call = getattr(thing, "Package")
    module = call(name)
    return module


def more():
    """"""
    package = importlib.import_module("celestine.package")

    package.autoflake = loader("autoflake")
    package.black = loader("black")
    package.blender = loader("blender")
    package.curses = loader("curses")
    package.dearpygui = loader("dearpygui")
    package.isort = loader("isort")
    package.pillow = loader("pillow")
    package.platformdirs = loader("platformdirs")
    package.pydocstringformatter = loader("pydocstringformatter")
    package.pygame = loader("pygame")
    package.pyupgrade = loader("pyupgrade")
    package.tkinter = loader("tkinter")


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    more()

    session = load.package("celestine", "session")
    begin_session = getattr(session, "begin_session")
    begin_session(argument_list, exit_on_error, **star)

    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view
