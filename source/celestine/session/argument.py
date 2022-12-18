""""""

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

    def dictionary(
        self
    ):
        """"""

        return {"default": self.default}

    def asdict(
        self,
    ) -> typing.Dict[str, str]:
        """"""

        return {
            "help": self.help,
        }

    def value(
        self,
        name: str,
    ) -> typing.Tuple[str, typing.Dict[str, str]]:
        """type hinting broken on this function"""

        return (name, self.asdict())

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


class Flag(Argument):
    """"""

    def value(
        self,
        name,
    ):
        """type hinting broken on this function"""

        return super().value(
            (
                NONE.join((HYPHEN_MINUS, name[0])),
                NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
            )
        )


class Name(Argument):
    """"""

    def value(
        self,
        name,
    ):
        """type hinting broken on this function"""

        return super().value(
            (
                name,
            )
        )


class Optional(Flag):
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


class Override(Flag):
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


class Positional(Name):
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




