""""""


from celestine import load
from celestine.parser.magic import Magic
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    B,
    L,
    S,
)

from .session import Session as SessionParse

INIT = "__init__"
SESSION = "session"


def start_session(
    argument_list: L[S], exit_on_error: B
) -> SessionParse:
    """"""
    magic = Magic(argument_list, exit_on_error)
    with magic:
        magic.application_name = magic.state._application
        magic.application_module = load.module(
            APPLICATION, magic.application_name
        )

        magic.interface_name = magic.state._interface
        magic.interface_module = load.module(
            INTERFACE, magic.interface_name
        )

        magic.language_name = magic.state._language
        magic.language_module = load.module(
            LANGUAGE, magic.language_name
        )
        # load.module(LANGUAGE, language)

        magic.parse(LANGUAGE)
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        session1 = magic.spawn("Session", "session", "session")
        session2 = magic.spawn(
            "Session", APPLICATION, magic.application_name
        )
        session3 = magic.spawn("Information", "session", "session")

        magic.get_parser(
            [session1, session2, session3],
            False,
        )

    # convert to usable

    the_name = load.module_to_name(session1.application)

    code = load.functions(load.module(APPLICATION, the_name, "code"))
    view = load.functions(load.module(APPLICATION, the_name, "view"))

    magic.session.application = load.module(
        APPLICATION, session1.application
    )

    magic.session.attribute = session2
    magic.session.interface = load.module(INTERFACE, session1.interface)
    magic.session.language = load.module(LANGUAGE, session1.language)

    magic.session.code = code
    magic.session.view = view
    magic.session.main = session1.main

    return magic.session


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
