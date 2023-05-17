""""""


from celestine import load
from celestine.parser.main import get_parser
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    MT,
    B,
    L,
    S,
)

from .configuration import Configuration
from .session import Session as SessionParse

INIT = "__init__"


from celestine.parser.default import quick

SESSION = "session"


class Session:
    application: MT
    attribute: L[S]
    interface: MT
    language: MT
    code: MT
    view: MT


def start_session(
    argument_list: L[S], exit_on_error: B
) -> SessionParse:
    """"""

    def parse(holder, name, default) -> MT:
        """Quickly parse important attributes."""

        class_name = name.capitalize()
        session = load.method(class_name, SESSION, SESSION)

        hippo = session(holder)

        get_parser(
            argument_list,
            exit_on_error,
            holder.application,
            holder.language,
            [hippo],
            True,
            configuration,
        )

        return hippo

    configuration = Configuration()
    configuration.load()

    state = quick()
    state = parse(state, LANGUAGE, state.language)
    state = parse(state, INTERFACE, state.interface)
    state = parse(state, APPLICATION, state.application)

    session1 = load.method("Session", "session", "session")(state)
    session2 = getattr(state.application, "Session")(state)
    session3 = load.method("Information", "session", "session")(state)

    get_parser(
        argument_list,
        exit_on_error,
        state.application,
        state.language,
        [session1, session2, session3],
        True,
        configuration,
    )

    configuration.save()

    new_session = Session()

    the_name = load.module_to_name(session1.application)

    code = load.functions(load.module(APPLICATION, the_name, "code"))
    view = load.functions(load.module(APPLICATION, the_name, "view"))

    new_session.application = session1.application
    new_session.attribute: session2
    new_session.interface = session1.interface
    new_session.language = session1.language
    new_session.code = code
    new_session.view = view
    new_session.main = "main"
    return new_session


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
