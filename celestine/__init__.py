"""
Initialize the program.

This module does not import modules in the usual way.
This is done so that this module does not depend on any other module.
That way other modules can use whatever imports they want freely.
This is so the packages directory can be loaded in and setup properly.
"""

import importlib
import os
import pkgutil
import sys

from celestine.typed import (
    N,
    S,
)


def init(root: S) -> N:
    """"""
    sys_stdout = sys.stdout
    with open(os.devnull, "w", encoding="utf-8") as stdout:
        sys.stdout = stdout

        locations = ["package", "language", "interface"]
        for location in locations:
            name = f"{root}.{location}"
            try:
                module = importlib.import_module(name)
            except ModuleNotFoundError:
                return

            spec = module.__spec__
            if not spec:
                return

            path = spec.submodule_search_locations
            modules = pkgutil.iter_modules(path)

            for info in modules:
                _name = f"{name}.{info.name}:Self"
                try:
                    value = pkgutil.resolve_name(_name)
                    setattr(module, info.name, value())
                except AttributeError:
                    pass

    sys.stdout = sys_stdout


init(__package__)


def main(*names: S) -> N:
    """
    Initialize the packages and then run the main program.

    Packages like pygame will print an anoying message on import.
    So we change the output stream to hide any messages
    a package may print when being imported.
    """
    for name in names:
        init(name)

    session = importlib.import_module("celestine.session")
    run = getattr(session, "run")
    run(names[0])


# names order important
# load first module
# go through the spec locations next
# try to find each package thing
