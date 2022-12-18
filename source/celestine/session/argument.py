""""""

import typing

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import NONE
from celestine.text.unicode import QUESTION_MARK

from celestine.session.attribute import Attribute
from celestine.session.attribute import Choices
from celestine.session.attribute import Help
from celestine.session.attribute import Nargs

from celestine.session.hash import HashClass


class Argument(HashClass, Attribute):
    """"""


class Flag(Argument):
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


class Name(Argument):
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


class Optional(Flag, Help):
    """"""

    def __init__(
        self,
        fallback: str,
        help: str,
    ):
        super().__init__(
            fallback=fallback,
            help=help,
        )


class Override(Flag, Help, Choices):
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


class Positional(Name, Help, Choices, Nargs):
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
