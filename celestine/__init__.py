""""""

import os
import sys

from celestine import load
from celestine.typed import (
    LS,
    B,
    N,
    R,
)

bl_info = {
    "name": "Célestine",
    "description": "A python framework for desktop applications.",
    "author": "Marian Molyneux",
    "version": (2024, 6, 9),
    "blender": (4, 1, 0),
    "location": "View3D > Properties > Object Properties > Célestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/issues",
    "category": "3D View",
}


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """
    Initialize the packages and then run the main program.

    Packages like pygame will print an anoying message on import.
    So we change the output stream to hide any messages
    a package may print when being imported.
    """
    package = load.module("package")

    sys_stdout = sys.stdout
    with open(os.devnull, "w", encoding="utf-8") as stdout:
        sys.stdout = stdout
        argument = load.argument("package")
        for name in argument:
            value = load.instance("package", name, "Package")
            setattr(package, name, value)
    sys.stdout = sys_stdout

    begin_main = load.function("session", "begin_main")
    begin_main(argument_list, exit_on_error, **star)


def register() -> N:
    """
    Blender register function.

    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    load.module("bank")
    load.instance("interface", "blender", "register")


def unregister() -> N:
    """
    Blender unregister function.

    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    load.module("bank")
    load.instance("interface", "blender", "unregister")
