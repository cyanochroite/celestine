""""""

import importlib
import importlib.resources

from celestine import bank
from celestine.session import begin_session
from celestine.typed import (
    LS,
    A,
    B,
    M,
    N,
    R,
    S,
)

CELESTINE = "celestine"
VERSION_NUMBER = "2023.10.7"
INTERFACE = "interface"
BLENDER = "blender"
REGISTER = "register"
UNREGISTER = "unregister"

CELESTINE = "celestine"
VERSION_NUMBER = "2023.10.7"
INTERFACE = "interface"
BLENDER = "blender"
REGISTER = "register"
UNREGISTER = "unregister"

bl_info = {
    "name": "celestine",
    "description": "A python framework for desktop applications.",
    "author": "mem_dixy",
    "version": (2023, 10, 7),
    "blender": (4, 0, 0),
    "location": "View3D > Properties > Object Properties > celestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "category": "3D View",
}


def module(*path: S) -> M:
    """Load an internal module from anywhere in the application."""
    return package(CELESTINE, *path)


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = ".".join(iterable)
    result = importlib.import_module(name)
    return result


def attribute(*path: S) -> A:
    """Functions like the 'from package import item' syntax."""
    iterable = [*path]
    name = iterable.pop(-1)
    item = module(*iterable)
    result = getattr(item, name)
    return result


def redirect(*path: S) -> N:
    """
    Loads a function from the specified path, and then runs it.

    :param path: The last item is the function name.
    """
    function = attribute(*path)
    function()


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    begin_session(argument_list, exit_on_error, **star)
    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view


def register() -> N:
    """
    Blender register function.

    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    load.redirect(INTERFACE, BLENDER, REGISTER)


def unregister() -> N:
    """
    Blender unregister function.

    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    load.redirect(INTERFACE, BLENDER, UNREGISTER)
