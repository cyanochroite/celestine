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


class SuperState:
    """"""

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""

        capitalize = name.capitalize()
        method = load.method(capitalize, SESSION, SESSION)
        hippo = method(self)

        self.get_parser(
            self.application,
            self.language,
            [hippo],
            True,
        )

        return hippo

    def __init__(
        self, application: MT, interface: MT, language: MT
    ) -> N:
        """"""
        self.application = application
        self.interface = interface
        self.language = language


class SuperSession(SuperState):
    """"""

    def dictionary(self) -> AD:
        """"""
        return {}

    def items(self) -> AI:
        """"""
        dictionary = self.dictionary()
        return dictionary.items()

    def __init__(self, other):
        super().__init__(
            other.application,
            other.interface,
            other.language,
        )


class Information(SuperSession):
    """"""

    def dictionary(self) -> AD:
        """"""
        return {
            CONFIGURATION: InformationConfiguration(
                self.language.ARGUMENT_HELP_HELP,
            ),
            HELP: InformationHelp(
                self.language.ARGUMENT_HELP_HELP,
            ),
            VERSION: InformationVersion(
                self.language.ARGUMENT_VERSION_HELP,
            ),
        }


class Dictionary(SuperSession):
    """"""

    def __setattr__(self, key: S, value: S) -> N:
        """"""
        try:
            module = load.module_fallback(key, value)
            self.__dict__[key] = module
        except TypeError:
            self.__dict__[key] = value


class Application(Dictionary):
    """"""

    application: MT

    def dictionary(self) -> AD:
        """"""
        return super().dictionary() | {
            APPLICATION: Customization(
                self.language.ARGUMENT_INTERFACE_HELP,
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
                self.language.ARGUMENT_INTERFACE_HELP,
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
                self.language.ARGUMENT_LANGUAGE_HELP,
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
                self.language.ARGUMENT_LANGUAGE_HELP,
                function.function_page(self.application),
            ),
        }

    def __setattr__(self, name: S, value: S) -> N:
        """"""
        match name:
            case "main":
                self.__dict__[name] = value
            case "attribute":
                self.__dict__[name] = value
            case _:
                super().__setattr__(name, value)
