""""""


from celestine import load
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    MT,
    B,
    L,
    N,
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


from celestine.parser.main import (
    add_argument,
    add_attribute,
    make_argument_group,
    make_parser,
)


class Magic:
    def get_parser(
        self,
        application: MT,
        language: MT,
        attributes: L[SessionParse],
        fast: B,
    ):
        """Attributes is modified in place."""
        parser = make_parser(language, self.exit_on_error)

        arguments = make_argument_group(language, parser)

        add_argument(attributes, arguments)

        if fast:
            args = parser.parse_known_args(self.argument_list)[0]
        else:
            args = parser.parse_args(self.argument_list)

        add_attribute(attributes, self.configuration, args)

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""

        capitalize = name.capitalize()
        method = load.method(capitalize, SESSION, SESSION)
        hippo = method(self.state)

        self.get_parser(
            self.state.application,
            self.state.language,
            [hippo],
            True,
        )

        self.state = hippo

    def spawn(self, clone, name, *path):
        method = load.method(name, *path)
        item = method(clone)
        return item

    def __enter__(self):
        self.configuration.load()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.configuration.save()

    def __init__(self, argument_list: L[S], exit_on_error: B) -> N:
        self.argument_list = argument_list
        self.configuration = Configuration()
        self.exit_on_error = exit_on_error
        self.state = quick()


def start_session(
    argument_list: L[S], exit_on_error: B
) -> SessionParse:
    """"""

    magic = Magic(argument_list, exit_on_error)

    with magic:
        magic.parse(LANGUAGE)
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        the_named = load.module_to_name(magic.state.application)

        session1 = magic.spawn(
            magic.state, "Session", "session", "session"
        )
        session2 = magic.spawn(
            magic.state, "Session", APPLICATION, the_named
        )
        session3 = magic.spawn(
            magic.state, "Information", "session", "session"
        )

        magic.get_parser(
            magic.state.application,
            magic.state.language,
            [session1, session2, session3],
            True,
        )

    # convert to usable

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
