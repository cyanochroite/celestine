""""""

from celestine.text.unicode import QUESTION_MARK
from celestine.text.unicode import NONE
from celestine.text.unicode import HYPHEN_MINUS
from celestine.text import VERSION_NUMBER

from .text import VERSION
from .hash import HashClass

from .attribute import Attribute

from .attribute import Action
from .attribute import Choices
from .attribute import Help
from .attribute import Nargs

from .type import AT
from .type import B
from .type import S
from .type import SL
from .type import N


class Argument(HashClass, Attribute):
    """abstract class"""

    def __init__(self, argument: B, attribute: B, fallback: S, **kwargs) -> N:
        """"""
        super().__init__(**kwargs)
        self.argument = argument
        self.attribute = attribute
        self.fallback = fallback

    def key(self, _: str) -> list[str]:
        ...


class Flag(Argument):
    """"""

    def key(self, name: S) -> SL:
        """"""
        return [
            NONE.join((HYPHEN_MINUS, name[0])),
            NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
        ]


class Name(Argument):
    """"""

    def key(self, name: S) -> SL:
        """"""
        return [name]


class Optional(Flag, Help):
    """"""

    def __init__(self, fallback: S, help: S) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=True,
            fallback=fallback,
            help=help,
        )


class Override(Flag, Help, Choices):
    """"""

    def __init__(self, fallback: S, help: S, choices: SL) -> N:
        """"""
        super().__init__(
            argument=bool(choices),
            attribute=True,
            fallback=fallback,
            help=help,
            choices=choices,
        )


class Positional(Name, Help, Choices, Nargs):
    """"""

    def __init__(self, fallback: S, help: S, choices: SL) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=True,
            fallback=fallback,
            help=help,
            choices=choices,
            nargs=QUESTION_MARK,
        )


class Information(Flag, Action, Help):
    """"""

    def dictionary(self) -> AT:
        """"""
        true = {VERSION: VERSION_NUMBER}
        boolean = true if self.version is True else {}
        return super().dictionary() | boolean

    def __init__(self, fallback: S, action: S, help: S, version: B) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=False,
            fallback=fallback,
            action=action,
            help=help,
        )
        self.version = version
