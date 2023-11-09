""""""

from celestine.typed import (
    LS,
    B,
    N,
    R,
    S,
)
from celestine.unicode import (
    HYPHEN_MINUS,
    NONE,
    QUESTION_MARK,
)

from .attribute import (
    Action,
    Attribute,
    Choices,
    Help,
    Nargs,
    Version,
)
from .data import (
    HELP,
    STORE_TRUE,
    VERSION,
)
from .hash import HashClass


class Argument(HashClass, Attribute):
    """Abstract class."""

    def __init__(
        self, argument: B, attribute: B, fallback: S, **star: R
    ) -> N:
        """"""
        super().__init__(**star)
        self.argument = argument
        self.attribute = attribute
        self.fallback = fallback

    def key(self, _: S) -> LS:
        """"""
        return []


class Flag(Argument):
    """"""

    def key(self, name: S) -> LS:
        """"""
        return [
            NONE.join((HYPHEN_MINUS, name[0])),
            NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
        ]


class Name(Argument):
    """"""

    def key(self, name: S) -> LS:
        """"""
        return [name]


class Application(Flag, Help):
    """"""

    # pylint: disable-next=redefined-builtin
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

    # pylint: disable-next=redefined-builtin
    def __init__(self, fallback: S, help: S, choices: LS) -> N:
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

    # pylint: disable-next=redefined-builtin
    def __init__(self, fallback: S, help: S, choices: LS) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=True,
            fallback=fallback,
            help=help,
            choices=choices,
            nargs=QUESTION_MARK,
        )


class Optional(Flag, Help):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, fallback: S, help: S) -> N:
        """"""
        super().__init__(
            argument=True,
            attribute=True,
            fallback=fallback,
            help=help,
        )


class Information(Flag, Action, Help):
    """"""

    # pylint: disable-next=redefined-builtin
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

    # pylint: disable-next=redefined-builtin
    def __init__(self, help) -> N:
        """"""
        super().__init__(
            action=STORE_TRUE,
            help=help,
        )


class InformationHelp(Information):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, help: S) -> N:
        """"""
        super().__init__(
            action=HELP,
            help=help,
        )


class InformationVersion(Information, Version):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, help: S) -> N:
        """"""
        super().__init__(
            action=VERSION,
            help=help,
        )
