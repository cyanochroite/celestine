""""""

import dataclasses
import typing

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import NONE
from celestine.text.unicode import QUESTION_MARK


DEFAULT = "default"


class Argument():
    """"""

    default: str
    help: str

    @staticmethod
    def dictionary(x):
        candy = {k: v for (k, v) in x if k not in [DEFAULT]}

        return candy

    def __str__(self):
        candy = super().__str__()
        cat = candy.split(" ")
        fish = cat[0]
        dog = fish.split("<", )
        doorbell = dog[1]
        canopen = doorbell.split(".", )
        frog = canopen[-1]
        return frog

#        return super().__str__().split("(")[0]

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)


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
            self.asdict(),
        )


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
            self.asdict(),
        )


class Optionaly(Optional):
    """"""

    def asdict(self):
        return {
            "help": self.help,
        }

    def __init__(
        self,
        default: str,
        help: str,
    ) -> None:
        """"""

        self.default = default
        self.help = help


class Override(Optional):
    """"""

    choices: list[str]

    def asdict(self):
        return {
            "help": self.help,
            "choices": self.choices,
        }

    def __init__(
        self,
        default: str = "",
        help: str = "",
        choices: list[str] = [],
    ) -> None:
        """"""

        self.default = default
        self.help = help
        self.choices = choices


class Positionaly(Positional):
    """"""

    choices: list[str]
    nargs: str = QUESTION_MARK

    def asdict(self):
        return {
            "help": self.help,
            "choices": self.choices,
            "nargs": self.nargs,
        }

    def __init__(
        self,
        default: str,
        help: str,
        choices: list[str],
        nargs: str = QUESTION_MARK,
    ) -> None:
        """"""

        self.default = default
        self.help = help
        self.choices = choices
        self.nargs = nargs




