""""""


import sys
import os
import pathlib
import os
import sys


from celestine import (
    bank,
    load,
    stream,
)
from celestine.data.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    LS,
    B,
    C,
    D,
    N,
    R,
    S,
    LS,
    OS,
    B,
    D,
    M,
    N,
    R,
    S,
)

from .magic import Magic


CELESTINE = "celestine"
PACKAGE = "package"
this = load.module(PACKAGE)


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

        path = str(load.project_path())
        sys.argv = [path, path]
        try:
            module = load.package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self) -> B:
        return self.package is not None

    def __getattr__(self, name: S) -> S:
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
            stream.Mode.WRITE_TEXT.value,
            encoding=stream.Encoding.UTF_8.value,
        ) as stdout:
            sys.stdout = stdout  # as TextIO
            try:
                self.package = load.package(self.pypi)
            except ModuleNotFoundError:
                self.package = None
                # found = f"Package '{self.name}' not found."
                # install = f"Install with 'pip install {self.pypi}'."
                # message = f"{found} {install}"
                # logging.warning(message)

        sys.stdout = sys_stdout


class Package:
    """"""

    dictionary: D[S, M]

    def __getattr__(self, name: S) -> M:
        """"""
        try:
            return self.dictionary[name]
        except KeyError as error:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message) from error

    def __init__(self, **star: R) -> N:
        self.dictionary = {}
        argument = load.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(name)
            self.dictionary[name] = package


def begin_session(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """

    First load Language so human can read errors.
    Then load Interface so human see errors the way they want.
    """

    magic = Magic(argument_list, exit_on_error)

    with magic:
        magic.parse(LANGUAGE)
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        method = load.method("Configuration", "session", "session")
        magic.get_parser([method], True)
        path = method.configuration
        magic.configuration.load(path)

        magic.parse(LANGUAGE)
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        session1 = load.method("Session", "session", "session")
        session2 = load.method(
            "Session", APPLICATION, magic.core.application.name
        )
        session3 = load.method("Information", "session", "session")

        magic.get_parser([session1, session2, session3], False)

    # Save values to session object.
    application = magic.core.application.name

    # items = load.python(APPLICATION, application)
    # car = list(items)

    code: D[S, C] = {}
    main: D[S, C] = {}
    view: D[S, C] = {}

    modules = load.modules(APPLICATION, application)
    for module in modules:
        code |= load.decorators(module, "code")
        main |= load.decorators(module, "main")
        view |= load.decorators(module, "scene")

    if not main:
        raise LookupError("No '@main' decorator found.")

    if len(main) > 1:
        raise UserWarning("Expecting only one '@main' decorator.")

    bank.application = load.module(APPLICATION, session1.application)
    bank.attribute = session2
    bank.code = code
    bank.configuration = pathlib.Path()  # unset
    bank.directory = session1.directory
    bank.interface = load.module(INTERFACE, session1.interface)
    bank.language = load.module(LANGUAGE, session1.language)
    bank.main = next(iter(main))

    module = load.module("package")
    for name in load.argument(PACKAGE):
        attribute = load.attribute(PACKAGE, name, "Package")
        package = attribute(name)
        setattr(module, name, package)

    bank.view = view | main
    bank.window = bank.interface.Window(**star)
