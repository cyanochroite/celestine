""""""

from celestine import load
from celestine.session.session import SuperState
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    MT,
    L,
    S,
)


def module(language: MT, items: L[S], *path: S) -> S:
    """Return a default application."""

    for item in items:
        try:
            load.module(*path, item)
            # Break if not found.
            return item
        except ModuleNotFoundError:
            pass

    raise RuntimeError(language.message)  # TODO fix this.


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
