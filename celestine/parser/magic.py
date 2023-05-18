""""""

from celestine import load
from celestine.parser.default import quick
from celestine.parser.main import (
    add_argument,
    add_attribute,
)
from celestine.parser.parser import make_parser
from celestine.session.configuration import Configuration
from celestine.session.session import Session as SessionParse
from celestine.typed import (
    MT,
    B,
    L,
    N,
    S,
)

from .argument import make_argument_group

INIT = "__init__"


SESSION = "session"


class Session:
    """"""

    application: MT
    attribute: L[S]
    interface: MT
    language: MT
    code: MT
    view: MT


class Magic:
    """"""

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

    def parse(self, name) -> N:
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

        setattr(self, f"{name}_name", value)
        setattr(self, f"{name}_module", load.module(name, value))
        setattr(self.session, name, value)

    def spawn(self, name, *path):
        """"""
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

        self.application_name = ""
        self.application_module = load.module()

        self.interface_name = ""
        self.interface_module = load.module()

        self.language_name = ""
        self.language_module = load.module()
