""""""

import collections.abc

from celestine import (
    bank,
    language,
    load,
)
from celestine.literal import (
    APPLICATION,
    CONFIGURATION,
    DIRECTORY,
    INTERFACE,
    LANGUAGE,
    NONE,
)
from celestine.session import default
from celestine.session.argument import (
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Optional,
    Positional,
)
from celestine.session.data import (
    Actions,
    Values,
)
from celestine.typed import (
    DA,
    A,
    S,
    T,
    ignore,
)


class SuperSession:
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return {}

    @classmethod
    def items(cls) -> collections.abc.Iterable[T[S, A]]:
        """"""
        dictionary = cls.dictionary()
        return dictionary.items()


class Information(SuperSession):
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            "save": InformationConfiguration(
                language.ARGUMENT_HELP_HELP,
            ),
            Actions.HELP: InformationHelp(
                language.ARGUMENT_HELP_HELP,
            ),
            Actions.VERSION: InformationVersion(
                language.ARGUMENT_VERSION_HELP,
            ),
        }


class Dictionary(SuperSession):
    """"""


class Application(Dictionary):
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            APPLICATION: Customization(
                default.application(),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(APPLICATION),
            ),
        }


class Configuration(Dictionary):
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            CONFIGURATION: Optional(
                default.application(),
                language.ARGUMENT_INTERFACE_HELP,
            ),
        }


class Directory(Dictionary):
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            DIRECTORY: Optional(
                default.application(),
                language.ARGUMENT_INTERFACE_HELP,
            ),
        }


class Interface(Dictionary):
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            INTERFACE: Customization(
                default.interface(),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
        }


class Language(Dictionary):
    """"""

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            LANGUAGE: Customization(
                default.language(),
                language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
        }


class Session(
    Application,
    Configuration,
    Directory,
    Interface,
    Language,
):
    """"""

    main: S

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            Values.MAIN: Positional(
                NONE,
                language.ARGUMENT_LANGUAGE_HELP,
                load.function_page(bank.application),
            ),
        }
