""""""


import importlib
import pathlib

from celestine import (
    bank,
    load,
)
from celestine.typed import (
    LS,
    B,
    C,
    D,
    M,
    N,
    R,
    S,
)

from .magic import Magic

CELESTINE = "celestine"
VERSION_NUMBER = "2023.10.7"
INTERFACE = "interface"
BLENDER = "blender"
REGISTER = "register"
UNREGISTER = "unregister"
LANGUAGE = "language"
INTERFACE = "interface"
APPLICATION = "application"


CELESTINE = "celestine"
PACKAGE = "package"
this = load.module(PACKAGE)


def _package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = ".".join(iterable)
    result = importlib.import_module(name)
    return result


def magic(name: S) -> M:
    thing = _package("celestine", "package", name)
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


def begin_session(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """

    First load Language so human can read errors.
    Then load Interface so human see errors the way they want.
    """

    # load this data
    more()

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
    bank.view = view | main
    bank.window = bank.interface.Window(**star)

    # monkeypatch in the language
    language = load.package(CELESTINE, LANGUAGE)
    for key, value in vars(bank.language).items():
        setattr(language, key, value)
