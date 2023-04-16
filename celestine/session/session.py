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
from celestine.unicode import LOW_LINE

from .argument import Argument
from .text import (
    CONFIGURATION,
    HELP,
    MAIN,
    VERSION,
)

AD: TA = D[S, Argument]
AI: TA = IT[T[S, Argument]]


class SuperState:
    """"""

    def __init__(
        self, application: MT, interface: MT, language: MT
    ) -> N:
        """"""
        self._application = application
        self._interface = interface
        self._language = language


class SuperSession(SuperState):
    """"""

    def dictionary(self) -> AD:
        """"""
        return {}

    def items(self) -> AI:
        """"""
        dictionary = self.dictionary()
        return dictionary.items()


class Information(SuperSession):
    """"""

    def dictionary(self) -> AD:
        """"""
        return {
            CONFIGURATION: InformationConfiguration(
                self._language.ARGUMENT_HELP_HELP,
            ),
            HELP: InformationHelp(
                self._language.ARGUMENT_HELP_HELP,
            ),
            VERSION: InformationVersion(
                self._language.ARGUMENT_VERSION_HELP,
            ),
        }


class Dictionary(SuperSession):
    """"""

    def __setattr__(self, key: S, value: S) -> N:
        """"""
        if key.startswith(LOW_LINE):
            self.__dict__[key] = value
        else:
            module = load.module_fallback(key, value)
            self.__dict__[key] = module


class Application(Dictionary):
    """"""

    application: MT

    def dictionary(self) -> AD:
        """"""
        return super().dictionary() | {
            APPLICATION: Customization(
                self._language.ARGUMENT_INTERFACE_HELP,
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
                self._language.ARGUMENT_INTERFACE_HELP,
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
                self._language.ARGUMENT_LANGUAGE_HELP,
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
                self._language.ARGUMENT_LANGUAGE_HELP,
                function.function_page(self._application),
            ),
        }

    def __setattr__(self, name: S, value: S) -> N:
        """"""
        match name:
            case "call":
                self.__dict__[name] = value
            case "view":
                self.__dict__[name] = value
            case "main":
                self.__dict__[name] = value
            case "attribute":
                self.__dict__[name] = value
            case _:
                super().__setattr__(name, value)
