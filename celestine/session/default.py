""""""

from celestine import load
from celestine.literal import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import S


def module(path: S, *items: S) -> S:
    """Return a default application."""
    for item in items:
        try:
            load.module(path, item)
            # Break if not found.
            return item
        except ModuleNotFoundError:
            pass
    raise ModuleNotFoundError("Failed to load any module from list.")


def application():
    """"""
    return module(
        APPLICATION,
        "demo",
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
