""""""
import dataclasses
import types
import typing

from celestine.text.directory import LANGUAGE
from celestine.text.directory import INTERFACE
from celestine.text.directory import APPLICATION

from celestine.session import load

EN = "en"
VIEWER = "viewer"
MAIN = "main"

CHOICES = "choices"


@dataclasses.dataclass
class Attribute():
    """"""


@dataclasses.dataclass
class Optional(Attribute):
    """"""

    default: str
    description: str


@dataclasses.dataclass
class Override(Attribute):
    """"""

    default: str
    description: str
    choice: list[str]


@dataclasses.dataclass
class Positional(Attribute):
    """"""

    default: str
    description: str
    choice: list[str]


class Hippo():
    """"""
    application: str
    interface: str
    language: str
    main: str

    @staticmethod
    def dictionary(
        language: types.ModuleType,
    ) -> typing.Dict[str, Attribute]:
        """"""

        return {
            INTERFACE: Override(
                load.argument_default(INTERFACE),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
            LANGUAGE: Override(
                EN,
                language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
            APPLICATION: Positional(
                load.argument_default(APPLICATION),
                "Choose an applicanion. They have more option.",
                load.argument(APPLICATION),
            ),
            MAIN: Positional(
                MAIN,
                "Choose an applicanion. They have more option.",
                [MAIN],
            ),
        }
