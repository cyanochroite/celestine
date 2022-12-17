""""""

import dataclasses
import typing

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import NONE
from celestine.text.unicode import QUESTION_MARK


DEFAULT = "default"


class ArgumentParser(type):
    """<class 'celestine.session.argument.Argument'>"""

    def __eq__(
        cls,
        other: typing.Self
    ):

        return str(cls) == str(other)

    def __hash__(
        cls,
    ) -> int:

        return hash(str(cls))

    def __str__(
        cls,
    ) -> str:

        string = super().__str__()
        (_, _, after) = string.rpartition(".")
        (before, _, _) = after.partition("'")
        return before


class Argument(metaclass=ArgumentParser):
    """"""

    default: str
    help: str

    @staticmethod
    def dictionary(x):
        candy = {k: v for (k, v) in x if k not in [DEFAULT]}

        return candy

    def __eq__(
        self,
        other: typing.Self
    ):

        return str(self) == str(other)

    def __hash__(
        self,
    ) -> int:

        return hash(str(self))

    def __str__(
        self,
    ) -> str:

        string = super().__str__()
        (_, _, after) = string.rpartition(".")
        (before, _, _) = after.partition(" ")
        return before


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




