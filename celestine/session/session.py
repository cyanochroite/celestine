""""""

from typing import TypeAlias as TA

from celestine.parser import default

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
    A,
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
    SESSION,
    VERSION,
)

AD: TA = D[S, Argument]
AI: TA = IT[T[S, Argument]]



class SuperSession():
    """"""

    def dictionary(self, core) -> AD:
        """"""
        return {}

    def items(self, core) -> AI:
        """"""
        dictionary = self.dictionary(core)
        return dictionary.items()


class Information(SuperSession):
    """"""

    def dictionary(self, core) -> AD:
        """"""
        return {
            CONFIGURATION: InformationConfiguration(
                core.language.ARGUMENT_HELP_HELP,
            ),
            HELP: InformationHelp(
                core.language.ARGUMENT_HELP_HELP,
            ),
            VERSION: InformationVersion(
                core.language.ARGUMENT_VERSION_HELP,
            ),
        }


class Dictionary(SuperSession):
    """"""


class Application(Dictionary):
    """"""

    application: MT

    def dictionary(self, core) -> AD:
        """"""
        return super().dictionary(core) | {
            APPLICATION: Customization(
                default.application(),
                core.language.ARGUMENT_INTERFACE_HELP,
                load.argument(APPLICATION),
            ),
        }


class Interface(Dictionary):
    """"""

    interface: MT

    def dictionary(self, core) -> AD:
        """"""
        return super().dictionary(core) | {
            INTERFACE: Customization(
                default.interface(),
                core.language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
        }


class Language(Dictionary):
    """"""

    language: MT

    def dictionary(self, core) -> AD:
        """"""
        return super().dictionary(core) | {
            LANGUAGE: Customization(
                default.language(),
                core.language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
        }


class Session(Application, Interface, Language):
    """"""

    main: S

    def dictionary(self, core) -> AD:
        """"""
        return super().dictionary(core) | {
            MAIN: Positional(
                "main",
                core.language.ARGUMENT_LANGUAGE_HELP,
                function.function_page(core.application),
            ),
        }
