""""""


from celestine import load
from celestine.parser import default
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
from .text import SESSION


class Core:
    """"""

    application: MT
    interface: MT
    language: MT

    def __init__(self, application: S, interface: S, language: S) -> N:
        """"""

        self.application = application
        self.interface = interface
        self.language = language

    def __setattr__(self, name, value):
        module = load.module(name, value)
        module.name = value
        super().__setattr__(name, module)


class Session:
    application: MT
    attribute: L[S]
    code: MT
    interface: MT
    language: MT
    main: S
    view: MT


from celestine.parser import (
    add_argument,
    add_attribute,
)
from celestine.parser.argument import make_argument_group
from celestine.parser.parser import make_parser


class Magic:
    def get_parser(
        self,
        attributes: L[SessionParse],
        fast: B,
        core,
    ):
        """Attributes is modified in place."""

        language = self.core.language

        parser = make_parser(language, self.exit_on_error)

        arguments = make_argument_group(language, parser)

        add_argument(attributes, arguments, core)

        if fast:
            args = parser.parse_known_args(self.argument_list)[0]
        else:
            args = parser.parse_args(self.argument_list)

        add_attribute(
            attributes,
            self.configuration,
            args,
            self.core.application.name,
            core,
        )

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""
        method = load.method(name.capitalize(), SESSION, SESSION)
        self.get_parser(
            [method],
            True,
            self.core,
        )
        setattr(self.core, name, getattr(method, name))

    def __enter__(self):
        self.configuration.load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.configuration.save()
        return False

    def __init__(self, argument_list: L[S], exit_on_error: B) -> N:
        self.argument_list = argument_list
        self.configuration = Configuration()
        self.exit_on_error = exit_on_error

        self.core = Core(
            default.application(),
            default.interface(),
            default.language(),
        )


def start_session(
    argument_list: L[S], exit_on_error: B
) -> SessionParse:
    """"""

    magic = Magic(argument_list, exit_on_error)

    with magic:
        magic.parse(LANGUAGE)
        magic.parse(INTERFACE)
        magic.parse(APPLICATION)

        session1 = load.method("Session", "session", "session")
        session2 = load.method(
            "Session", APPLICATION, magic.core.application.name
        )
        session3 = load.method("Information", "session", "session")

        magic.get_parser(
            [session1, session2, session3],
            False,
            magic.core,
        )

    application = magic.core.application.name
    session = Session()

    session.application = load.module(APPLICATION, session1.application)

    session.attribute = session2

    code = load.module(APPLICATION, application, "code")
    session.code = load.functions(code)

    session.interface = load.module(INTERFACE, session1.interface)

    session.language = load.module(LANGUAGE, session1.language)

    session.main = session1.main

    view = load.module(APPLICATION, application, "view")
    session.view = load.functions(view)

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
