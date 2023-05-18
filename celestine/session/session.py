""""""

from typing import TypeAlias as TA

from celestine import load
from celestine.load import function
from celestine.session.argument import (
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Positional,
)
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    IT,
    MT,
    D,
    N,
    S,
    T,
)

from .argument import Argument
from .text import (
    CONFIGURATION,
    HELP,
    MAIN,
    VERSION,
)

AD: TA = D[S, Argument]
AI: TA = IT[T[S, Argument]]
SESSION = "session"


def module(path: S, *items: S) -> S:
    """Return a default application."""

    for item in items:
        try:
            load.module(path, item)
            # Break if not found.
            return item
        except ModuleNotFoundError:
            pass

    raise RuntimeError("Failed to load any module from list.")
    # raise RuntimeError(language.message)


def language():
    """"""
    # Sorted list of languages by number of native speakers in Europe.
    # English and French were manually placed at the top of the list.
    return module(
        LANGUAGE,
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
    )


def interface():
    """"""
    return module(
        INTERFACE,
        "tkinter",
        "curses",
        "pygame",
        "dearpygui",
        "blender",
    )


def application():
    """"""
    return module(
        APPLICATION,
        "demo",
    )


class SuperState:
    """"""

    _application: MT
    _interface: MT
    _language: MT

    def __init__(
        self, _application: MT, _interface: MT, _language: MT
    ) -> N:
        """"""

        self._application = _application
        self._interface = _interface
        self._language = _language


class SuperSession(SuperState):
    """"""

    def dictionary(self) -> AD:
        """"""
        return {}

    def items(self) -> AI:
        """"""
        dictionary = self.dictionary()
        return dictionary.items()


class Information(SuperSession):
    """"""

    def dictionary(self) -> AD:
        """"""
        return {
            CONFIGURATION: InformationConfiguration(
                self._language.ARGUMENT_HELP_HELP,
            ),
            HELP: InformationHelp(
                self._language.ARGUMENT_HELP_HELP,
            ),
            VERSION: InformationVersion(
                self._language.ARGUMENT_VERSION_HELP,
            ),
        }


class Dictionary(SuperSession):
    """"""


class Application(Dictionary):
    """"""

    application: MT

    def dictionary(self) -> AD:
        """"""
        return super().dictionary() | {
            APPLICATION: Customization(
                application(),
                self._language.ARGUMENT_INTERFACE_HELP,
                load.argument(APPLICATION),
            ),
        }


class Interface(Dictionary):
    """"""

    interface: MT

    def dictionary(self) -> AD:
        """"""
        return super().dictionary() | {
            INTERFACE: Customization(
                interface(),
                self._language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
        }


class Language(Dictionary):
    """"""

    language: MT

    def dictionary(self) -> AD:
        """"""
        return super().dictionary() | {
            LANGUAGE: Customization(
                language(),
                self._language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
        }


class Session(Application, Interface, Language):
    """"""

    main: S

    def dictionary(self) -> AD:
        """"""
        return super().dictionary() | {
            MAIN: Positional(
                "main",
                self._language.ARGUMENT_LANGUAGE_HELP,
                function.function_page(self._application),
            ),
        }
