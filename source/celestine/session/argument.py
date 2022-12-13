""""""

import dataclasses
import typing

from celestine.text.unicode import QUESTION_MARK
from celestine.text.unicode import NONE
from celestine.text.unicode import HYPHEN_MINUS


Name: typing.TypeAlias = typing.Tuple[str]
Flag: typing.TypeAlias = typing.Tuple[str, str]


@dataclasses.dataclass
class Argument():
    """"""

    default: str
    help: str

    def value(
        self,
    ) -> typing.Dict[str, str]:
        """"""

        asdict = dataclasses.asdict(self)
        del asdict["default"]
        return asdict

    def fish(
        self,
        value: Name | Flag,
    ) -> typing.Tuple[Name | Flag, typing.Dict[str, str]]:
        """"""
        asdict = dataclasses.asdict(self)
        del asdict["default"]
        del asdict["key"]
        # field magic
        return (value, asdict)


@dataclasses.dataclass
class Optional(Argument):
    """"""

    key: str = "optional"

    def valued(
        self,
        name: str,
    ) -> typing.Tuple[Name | Flag, typing.Dict[str, str]]:
        """"""
        one = NONE.join((HYPHEN_MINUS, name[0]))
        two = NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name))

        return self.fish((one, two))


@dataclasses.dataclass
class Positional(Argument):
    """"""

    choices: list[str]
    key: str = "positional"
    nargs: str = QUESTION_MARK

    def valued(
        self,
        name: str,
    ) -> typing.Tuple[Name | Flag, typing.Dict[str, str]]:
        """"""

        return self.fish((name, ))


@dataclasses.dataclass
class Optionaly(Optional):
    """"""

    key: str = "optional"


@dataclasses.dataclass
class Overridey(Positional):
    """"""

    key: str = "override"


@dataclasses.dataclass
class Positionaly(Positional):
    """"""

    choices: list[str]
    key: str = "positional"
    nargs: str = QUESTION_MARK

