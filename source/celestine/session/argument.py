""""""

import typing

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import NONE
from celestine.text.unicode import QUESTION_MARK


DEFAULT = "default"


class Attribute():
    """"""

    def dictionary(
        self,
    ) -> typing.Dict[str, str]:
        """
        Do not map 'fallback' for it is not a valid ArgumentParser
        option. It functions a lot like 'default' where it is used only
        when all sources are found to be None.
        """

        return {"help": self.help}

    def __init__(
        self,
        fallback: str,
        help: str,
    ) -> None:
        """"""

        self.fallback = fallback
        self.help = help


class Choices(Attribute):
    """"""

    def dictionary(
        self,
    ):
        """"""

        return super().dictionary() | {"choices": self.choices}

    def __init__(
        self,
        choices: list[str],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.choices = choices


class Nargs(Attribute):
    """"""

    def dictionary(
        self,
    ):
        """"""

        return super().dictionary() | {"nargs": self.nargs}

    def __init__(
        self,
        nargs: str,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.nargs = nargs


#############
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


class Flag(Argument, Attribute):
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
            self.dictionary(),
        )


class Name(Argument, Attribute):
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
            self.dictionary(),
        )


class Optional(Flag):
    """"""


class Override(Flag, Choices):
    """"""

    def __init__(
        self,
        fallback: str,
        help: str,
        choices: list[str],
    ):
        super().__init__(
            fallback=fallback,
            help=help,
            choices=choices,
        )


class Positional(Name, Choices, Nargs):
    """"""

    def __init__(
        self,
        fallback: str,
        help: str,
        choices: list[str],
    ):
        super().__init__(
            fallback=fallback,
            help=help,
            choices=choices,
            nargs=QUESTION_MARK,
        )
