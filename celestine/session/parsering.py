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
        attributes: L[SessionParse],
        fast: B,
    ):
        """Attributes is modified in place."""

        language = self.language_module

        parser = make_parser(language, self.exit_on_error)

        arguments = make_argument_group(language, parser)

        add_argument(attributes, arguments)

        if fast:
            args = parser.parse_known_args(self.argument_list)[0]
        else:
            args = parser.parse_args(self.argument_list)

        add_attribute(
            attributes, self.configuration, args, self.application_name
        )

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""

        capitalize = name.capitalize()
        method = load.method(capitalize, SESSION, SESSION)
        # hippo = method(self.session)
        hippo = method(
            self.application_module,
            self.interface_module,
            self.language_module,
        )

        self.get_parser(
            [hippo],
            True,
        )

        value = getattr(hippo, name)
        setattr(self.session, name, value)

        self.state = hippo
        return hippo

    def spawn(self, name, *path):
        method = load.method(name, *path)
        item = method(
            self.application_module,
            self.interface_module,
            self.language_module,
        )
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
        self.session = Session()
        self.state = quick()

        self.application_name = None
        self.application_module = None

        self.interface_name = None
        self.interface_module = None

        self.language_name = None
        self.language_module = None


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

        the_named = load.module_to_name(magic.state.application)

        session1 = magic.spawn("Session", "session", "session")
        session2 = magic.spawn("Session", APPLICATION, the_named)
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

    magic.session.attribute: session2
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
