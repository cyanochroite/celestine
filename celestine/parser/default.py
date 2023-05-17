""""""

from celestine import load
from celestine.parser.main import get_parser
from celestine.session.session import SuperState
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    MT,
    L,
    N,
    S,
)


def module(language: MT, items: L[S], *path: S) -> MT:
    """Return a default application."""

    for item in items:
        try:
            return load.module(*path, item)
        except ModuleNotFoundError:
            pass

    raise RuntimeError("Failed to load any module from list.")
    # raise RuntimeError(language.message)


class Holder:
    """"""

    def __init__(
        self,
        application: MT,
        interface: MT,
        language: MT,
    ) -> N:
        """"""
        self.application = application
        self.interface = interface
        self.language = language


def quick():
    """Quickly parse important attributes."""

    language = {
        "error": "Failed to load any core language pack.",
    }

    # Sorted list of languages by number of native speakers in Europe.
    # English and French were manually placed at the top of the list.
    language = module(
        language,
        [
            "en",  # English English en.
            "fr",  # French français fr.
            "de",  # German Deutsch de.
            "it",  # Italian italiano it.
            "es",  # Spanish español es.
            "pl",  # Polish polski pl.
            "ro",  # Romanian română ro.
            "nl",  # Dutch Nederlands nl.
            "el",  # Greek ελληνικά el.
            "hu",  # Hungarian magyar hu.
            "sv",  # Swedish svenska sv.
            "cs",  # Czech čeština cs.
            "pt",  # Portuguese português pt.
            "bg",  # Bulgarian български bg.
            "hr",  # Croatian hrvatski hr
            "da",  # Danish dansk da.
            "fi",  # Finnish suomi fi.
            "sk",  # Slovak slovenčina sk.
            "lt",  # Lithuanian lietuvių lt.
            "sl",  # Slovenian slovenščina sl.
            "lv",  # Latvian latviešu lv.
            "et",  # Estonian eesti et.
            "mt",  # Maltese Malti mt.
            "ga",  # Irish Gaeilge ga.
        ],
        LANGUAGE,
    )

    interface = module(
        language,
        [
            "tkinter",
            "curses",
            "pygame",
            "dearpygui",
            "blender",
        ],
        INTERFACE,
    )

    application = module(
        language,
        [
            "demo",
        ],
        APPLICATION,
    )

    state = SuperState(application, interface, language)

    return state


def parse(name, value) -> MT:
    """Quickly parse important attributes."""

    session = session_loader(name.capitalize(), "session", "session")

    hippo = [
        session(application, interface, language),
    ]
    parser = get_parser(
        argv,
        exit_on_error,
        application,
        language,
        hippo,
        True,
        configuration,
    )[0]
    thing = getattr(parser, name, value)
    return thing


def start_session(argv, exit_on_error):
    """"""
    configuration = Configuration()
    configuration.load()

    state = quick()

    language = state._language
    interface = state._interface
    application = state._application

    language = quick_parse(LANGUAGE, language)
    interface = quick_parse(INTERFACE, interface)
    application = quick_parse(APPLICATION, application)

    session1 = session_loader("Session", "session", "session")

    get_name = load.module_to_name(application)
    if get_name == APPLICATION:
        get_name = INIT

    # override for demo
    get_name = "demo"

    session2 = session_loader("Session", APPLICATION, get_name)
    session3 = session_loader("Information", "session", "session")

    hippos = [
        session1(application, interface, language),
        session2(application, interface, language),
        session3(application, interface, language),
    ]
    attribute = get_parser(
        argv,
        exit_on_error,
        application,
        language,
        hippos,
        True,
        configuration,
    )

    session = attribute[0]
    session.attribute = attribute[1]

    configuration.save()

    # override for demo
    session.language = "fr"
    session.interface = "tkinter"
    session.application = "demo"

    return session


"""
importer notes.

language.py is all you need for 1 language.
language/__init__.py can be used instead.

Not recomended to use both. However, note that
language/__init__.py takes priority over language.py

Must have at least one of these.
Recomend using directory version so you can add more languages.
Error messages will assume this version.

if you have more then 1 language you must use language/__init__.py
"""


"""Configuration information will show your saved stuff."""
