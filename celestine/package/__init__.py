""""""

import importlib
import importlib.abc
import importlib.machinery
import os
import pathlib
import sys

from celestine.text import CELESTINE
from celestine.typed import (
    LS,
    OS,
    B,
    M,
    N,
    P,
    R,
    S,
)
from celestine.unicode import FULL_STOP


def _package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


def _project_path() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


class Abstract:
    """"""

    name: S
    package: M | N

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.main()

    def module(self) -> LS:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def run(self) -> N:
        """"""

        if not self.package:
            return

        argv = sys.argv

        path = str(_project_path())
        sys.argv = [path, path]
        try:
            module = _package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self) -> B:
        return self.package is not None

    def __getattr2__(self, name: S) -> S:
        return getattr(self.package, name)

    def __init__(self, name: S, pypi: OS = None, **star: R) -> N:
        self.name = name
        self.pypi = pypi or name

        # pygame prints an anoying message on import
        # so this here to hide any messages a package may print
        # when being imported
        sys_stdout = sys.stdout

        with open(
            os.devnull,
            "w",
            encoding="utf-8",
            # stream.Mode.WRITE_TEXT.value,
            # encoding=stream.Encoding.UTF_8.value,
        ) as stdout:
            sys.stdout = stdout  # as TextIO
            try:
                self.package = _package(self.pypi)
            except ValueError:
                #  Name was none.
                self.package = None
            except ModuleNotFoundError:
                self.package = None
                # found = f"Package '{self.name}' not found."
                # install = f"Install with 'pip install {self.pypi}'."
                # message = f"{found} {install}"
                # logging.warning(message)

        sys.stdout = sys_stdout
