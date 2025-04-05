"""
Initialize the program.

This module does not import modules in the usual way.
This is done so that this module does not depend on any other module.
That way other modules can use whatever imports they want freely.
This is so the packages directory can be loaded in and setup properly.
That way other modules can
"""

import importlib
import os
import pathlib
import sys


def packages() -> None:
    """
    Initialize all packages in the package directory.

    The package name will be an attribute of 'celestine.package'.
    If the package is not installed, it will be set to 'False'.
    """
    package = importlib.import_module("celestine.package")
    locations = __spec__.submodule_search_locations or []
    for location in locations:
        directory = pathlib.Path(location, "package")
        with os.scandir(directory) as folder:
            for file in folder:
                path = pathlib.Path(file.path)
                name = path.stem
                if not name[0].isalpha():
                    continue
                load = f"celestine.package.{name}"
                module = importlib.import_module(load)
                attribute = getattr(module, "Package")
                value = attribute()
                setattr(package, name, value)


def main() -> None:
    """
    Initialize the packages and then run the main program.

    Packages like pygame will print an anoying message on import.
    So we change the output stream to hide any messages
    a package may print when being imported.
    """
    sys_stdout = sys.stdout

    with open(os.devnull, "w", encoding="utf-8") as stdout:
        sys.stdout = stdout
        packages()

    sys.stdout = sys_stdout

    session = importlib.import_module("celestine.session")
    begin_main = getattr(session, "begin_main")
    begin_main()


if __name__ == "__main__":
    main()
