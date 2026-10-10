""""""

import importlib
import re

from celestine import (
    bank,
    load,
    walk,
)
from celestine.literal import (
    APPLICATION,
    CELESTINE,
    COLON,
    INTERFACE,
    LANGUAGE,
    join,
)
from celestine.session import default
from celestine.session.magic import Magic
from celestine.typed import (
    A,
    M,
    N,
    S,
    ignore,
)


def set_lang():
    """"""
    # monkeypatch in the language
    language = load.package(CELESTINE, LANGUAGE)
    for key, value in vars(bank.language).items():
        setattr(language, key, value)


def begin_session(module: M, name: S) -> A:
    """
    First load Language so human can read errors.

    Then load Interface so human see errors the way they want.
    """

    bank.configuration = load.instance(
        "session",
        "configuration",
        "Configuration",
    )

    # The order here matters.
    bank.language = load.module(LANGUAGE, default.language())
    set_lang()
    bank.interface = load.module(INTERFACE, default.interface())
    bank.application = module
    setattr(bank.application, "name", name)

    magic = Magic()

    with magic:
        magic.parse(LANGUAGE)
        set_lang()
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        method = load.method("Configuration", "session", "session")
        magic.get_parser([method], True)
        path = method.configuration
        bank.configuration.load(path)

        magic.parse(LANGUAGE)
        set_lang()
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        session = importlib.import_module("celestine.session.session")
        importlib.reload(session)

        session1 = load.method("Session", "session", "session")
        name = bank.application.__spec__.name.split(".")[-1]
        session2 = load.method("Session", APPLICATION, name)
        session3 = load.method("Information", "session", "session")

        magic.get_parser([session1, session2, session3], False)

    # Save values to session object.
    bank.application = module
    bank.attribute = session2
    bank.directory = session1.directory
    bank.interface = load.module(INTERFACE, session1.interface)
    bank.window = bank.interface.Window()

    set_lang()

    return bank.window


def run(goto: S, base: S) -> N:
    """
    Initializes and runs the main 'window' object.

    Imports the package found from loading 'base'.
    Goes through all modules and gathers all the decorators.
    When finished, the window object will be setup and good to go.
    """
    module1 = importlib.import_module(base)
    window = begin_session(module1, base)

    pattern = re.compile(r"<function (\w+)\.<locals>\.decorator")
    walked = walk.package(base)

    for module in walked:
        dictionary = vars(module)
        items = dictionary.items()

        for variable, decorator in items:
            yarn = repr(decorator)
            match = pattern.match(yarn)

            if not match:
                continue

            name = module.__spec__.name
            key = join(name, COLON, variable)
            decorator(window, key)

    if goto:
        window.main = goto
    window.run()


ignore(
    run,
)
