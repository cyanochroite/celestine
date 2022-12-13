""""""

import dataclasses
import typing

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import NONE
from celestine.text.unicode import QUESTION_MARK


KEY = "key"
DEFAULT = "default"


@dataclasses.dataclass
class Argument():
    """"""

    default: str
    help: str

    @staticmethod
    def dictionary(x):
        candy = {k: v for (k, v) in x if k not in [KEY, DEFAULT]}

        return candy


@dataclasses.dataclass
class Optional(Argument):
    """"""

    def value(
        self,
        name: str,
    ) -> typing.Tuple[typing.Tuple[str, str], typing.Dict[str, str]]:
        """"""

        return (
            (
                NONE.join((HYPHEN_MINUS, name[0])),
                NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
            ),
            dataclasses.asdict(
                self,
                dict_factory=self.dictionary,
            ),
        )


@dataclasses.dataclass
class Positional(Argument):
    """"""

    def value(
        self,
        name: str,
    ) -> typing.Tuple[typing.Tuple[str], typing.Dict[str, str]]:
        """"""

        return (
            (
                name,
            ),
            dataclasses.asdict(
                self,
                dict_factory=self.dictionary,
            ),
        )


@dataclasses.dataclass
class Optionaly(Optional):
    """"""

    key: str = dataclasses.field(default="optional", init=False)


@dataclasses.dataclass
class Overridey(Optional):
    """"""

    choices: list[str]
    key: str = dataclasses.field(default="override", init=False)


@dataclasses.dataclass
class Positionaly(Positional):
    """"""

    choices: list[str]
    key: str = dataclasses.field(default="positional", init=False)
    nargs: str = dataclasses.field(default=QUESTION_MARK, init=False)
