""""""

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
)
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
    AD,
    AI,
    M,
    S,
)
from celestine.unicode import NONE

from . import default


class SuperSession:
    """"""

    @classmethod
    def dictionary(cls) -> AD:
        """"""
        return {}

    @classmethod
    def items(cls) -> AI:
        """"""
        dictionary = cls.dictionary()
        return dictionary.items()


class Information(SuperSession):
    """"""

    @classmethod
    def dictionary(cls) -> AD:
        """"""
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

    application: M

    @classmethod
    def dictionary(cls) -> AD:
        """"""
        return super().dictionary() | {
            APPLICATION: Customization(
                default.application(),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(APPLICATION),
            ),
        }


class Configuration(Dictionary):
    """"""

    configuration: M

    @classmethod
    def dictionary(cls) -> AD:
        """"""
        return super().dictionary() | {
            CONFIGURATION: Optional(
                default.application(),
                language.ARGUMENT_INTERFACE_HELP,
            ),
        }


class Directory(Dictionary):
    """"""

    directory: M

    @classmethod
    def dictionary(cls) -> AD:
        """"""
        return super().dictionary() | {
            DIRECTORY: Optional(
                default.application(),
                language.ARGUMENT_INTERFACE_HELP,
            ),
        }


class Interface(Dictionary):
    """"""

    interface: M

    @classmethod
    def dictionary(cls) -> AD:
        """"""
        return super().dictionary() | {
            INTERFACE: Customization(
                default.interface(),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
        }


class Language(Dictionary):
    """"""

    language: M

    @classmethod
    def dictionary(cls) -> AD:
        """"""
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
    def dictionary(cls) -> AD:
        """"""
        return super().dictionary() | {
            Values.MAIN: Positional(
                NONE,
                language.ARGUMENT_LANGUAGE_HELP,
                load.function_page(bank.application),
            ),
        }
