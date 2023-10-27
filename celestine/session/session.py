""""""


from celestine import load
from celestine.data.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.load import function
from celestine.session.argument import (
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Positional,
)
from celestine.typed import (
    AD,
    AI,
    M,
    S,
)

from . import default
from .data import (
    CONFIGURATION,
    HELP,
    MAIN,
    VERSION,
)


class SuperSession:
    """"""

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return {}

    @classmethod
    def items(cls, core) -> AI:
        """"""
        dictionary = cls.dictionary(core)
        return dictionary.items()


class Information(SuperSession):
    """"""

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
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

    application: M

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
            APPLICATION: Customization(
                default.application(),
                core.language.ARGUMENT_INTERFACE_HELP,
                load.pathway.argument(APPLICATION),
            ),
        }


class Interface(Dictionary):
    """"""

    interface: M

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
            INTERFACE: Customization(
                default.interface(),
                core.language.ARGUMENT_INTERFACE_HELP,
                load.pathway.argument(INTERFACE),
            ),
        }


class Language(Dictionary):
    """"""

    language: M

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
            LANGUAGE: Customization(
                default.language(),
                core.language.ARGUMENT_LANGUAGE_HELP,
                load.pathway.argument(LANGUAGE),
            ),
        }


class Session(Application, Interface, Language):
    """"""

    main: S

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return super().dictionary(core) | {
            MAIN: Positional(
                "main",
                core.language.ARGUMENT_LANGUAGE_HELP,
                function.function_page(core.application),
            ),
        }
