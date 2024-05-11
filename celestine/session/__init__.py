""""""

import importlib

from celestine import (
    bank,
    load,
)
from celestine.literal import (
    APPLICATION,
    CELESTINE,
    INTERFACE,
    LANGUAGE,
    PACKAGE,
)
from celestine.typed import (
    LS,
    B,
    C,
    D,
    N,
    R,
    S,
)

from . import default
from .magic import Magic

this = load.module(PACKAGE)


def set_lang():
    """"""
    # monkeypatch in the language
    language = load.package(CELESTINE, LANGUAGE)
    for key, value in vars(bank.language).items():
        setattr(language, key, value)


def begin_session(argument_list: LS, exit_on_error: B, **star: R) -> N:
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
    hold = default.application()
    bank.application = load.module(APPLICATION, default.application())
    bank.application.name = hold

    magic = Magic(argument_list, exit_on_error)

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
        session2 = load.method(
            "Session", APPLICATION, bank.application.name
        )
        session3 = load.method("Information", "session", "session")

        magic.get_parser([session1, session2, session3], False)

    # Save values to session object.
    application = bank.application.name

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
    # bank.configuration = pathlib.Path()  # unset
    bank.directory = session1.directory
    bank.interface = load.module(INTERFACE, session1.interface)
    # bank.language = load.module(LANGUAGE, session1.language)
    bank.main = next(iter(main))
    bank.view = view | main
    bank.window = bank.interface.Window(**star)

    set_lang()

    return bank.window
