""""""

import dataclasses
import typing

from celestine.text.unicode import QUESTION_MARK
from celestine.text.unicode import NONE
from celestine.text.unicode import HYPHEN_MINUS


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


@dataclasses.dataclass
class Optional(Argument):
    """"""

    key: str = "optional"

    def valued(
        self,
        name: str,
    ) -> typing.Tuple[str, typing.Dict[str, str]]:
        """"""
        one = NONE.join((HYPHEN_MINUS, name[0]))
        two = NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name))

        asdict = dataclasses.asdict(self)
        del asdict["default"]
        del asdict["key"]
        # field magic
        return ((one, two), asdict)


@dataclasses.dataclass
class Positional(Argument):
    """"""

    choices: list[str]
    key: str = "positional"
    nargs: str = QUESTION_MARK

    def valued(
        self,
        name: str,
    ) -> typing.Tuple[str, typing.Dict[str, str]]:
        """"""

        asdict = dataclasses.asdict(self)
        del asdict["default"]
        del asdict["key"]
        # field magic
        return (tuple(name), asdict)


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

