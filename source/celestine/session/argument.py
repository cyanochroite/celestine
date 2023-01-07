""""""

from celestine.unicode import QUESTION_MARK
from celestine.unicode import NONE
from celestine.unicode import HYPHEN_MINUS

from celestine.typed import B
from celestine.typed import L
from celestine.typed import S
from celestine.typed import N

from .text import VERSION

from .text import STORE_TRUE
from .text import HELP


from .hash import HashClass

from .attribute import Attribute

from .attribute import Action
from .attribute import Choices
from .attribute import Help
from .attribute import Nargs
from .attribute import Version


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

    def key(self, name: S) -> L[S]:
        """"""
        return [
            NONE.join((HYPHEN_MINUS, name[0])),
            NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
        ]


class Name(Argument):
    """"""

    def key(self, name: S) -> L[S]:
        """"""
        return [name]


class Application(Flag, Help):
    """"""

    def __init__(self, fallback: S, help: S) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=True,
            fallback=fallback,
            help=help,
        )


class Customization(Flag, Help, Choices):
    """"""

    def __init__(self, help: S, choices: L[S]) -> N:
        """"""
        super().__init__(
            argument=bool(choices),
            attribute=True,
            fallback=NONE,
            help=help,
            choices=choices,
        )


class Positional(Name, Help, Choices, Nargs):
    """"""

    def __init__(self, fallback: S, help: S, choices: L[S]) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=True,
            fallback=fallback,
            help=help,
            choices=choices,
            nargs=QUESTION_MARK,
        )


class Information (Flag, Action, Help):
    """"""

    def __init__(self, action: S, help: S) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=False,
            fallback=NONE,
            action=action,
            help=help,
        )


class InformationConfiguration(Information):
    """"""

    def __init__(self, help) -> N:
        """"""
        super().__init__(
            action=STORE_TRUE,
            help=help,
        )


class InformationHelp(Information):
    """"""

    def __init__(self, help: S) -> N:
        """"""
        super().__init__(
            action=HELP,
            help=help,
        )


class InformationVersion(Information, Version):
    """"""

    def __init__(self, help: S) -> N:
        """"""
        super().__init__(
            action=VERSION,
            help=help,
        )

