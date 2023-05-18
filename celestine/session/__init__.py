""""""




from celestine import load
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.parser import default
from celestine.typed import (
    MT,
    B,
    L,
    N,
    S,
)

from .configuration import Configuration
from .session import Session as SessionParse

from .text import INIT
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


class Session:
    application: MT
    attribute: L[S]
    interface: MT
    language: MT
    code: MT
    view: MT


from celestine.parser import (
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
            self.core.application_name,
            core,
        )

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""

        capitalize = name.capitalize()
        method = load.method(capitalize, SESSION, SESSION)
        # hippo = method(self.session)
        hippo = method()

        self.get_parser(
            [hippo],
            True,
            self.core,
        )

        value = getattr(hippo, name)

        setattr(self.core, f"{name}_name", value)
        setattr(self.core, name, load.module(name, value))

    def spawn(self, name, *path):
        method = load.method(name, *path)
        item = method()
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

        self.core = Core(
            load.module(APPLICATION, default.application()),
            load.module(INTERFACE, default.interface()),
            load.module(LANGUAGE, default.language()),
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

        session1 = magic.spawn("Session", "session", "session")
        session2 = magic.spawn(
            "Session", APPLICATION, magic.core.application_name
        )
        session3 = magic.spawn("Information", "session", "session")

        magic.get_parser(
            [session1, session2, session3],
            False,
            magic.core,
        )

    # convert to usable

    the_name = magic.core.application_name

    code = load.functions(load.module(APPLICATION, the_name, "code"))
    view = load.functions(load.module(APPLICATION, the_name, "view"))


    #

    session = Session()

    session.application = load.module(
        APPLICATION, session1.application
    )

    session.attribute = session2
    session.interface = load.module(INTERFACE, session1.interface)
    session.language = load.module(LANGUAGE, session1.language)

    session.code = code
    session.view = view
    session.main = session1.main

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
