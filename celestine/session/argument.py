""""""

from abc import abstractmethod

from celestine.literal import (
    HYPHEN_MINUS,
    NONE,
    QUESTION_MARK,
)
from celestine.session.attribute import (
    Action,
    Attribute,
    Choices,
    Help,
    Nargs,
    Version,
)
from celestine.session.data import Actions
from celestine.session.hash import HashClass
from celestine.typed import (
    LS,
    B,
    N,
    R,
    S,
    ignore,
)


class Argument(HashClass, Attribute):
    """Abstract class."""

    def __init__(
        self,
        arguments: B,
        attribute: B,
        fallback: S,
        **star: R,
    ) -> N:
        """"""
        super().__init__(**star)
        self.arguments = arguments
        self.attribute = attribute
        self.fallback = fallback

    @abstractmethod
    def key(self, name: S) -> LS:
        """"""
        raise NotImplementedError(self, name)


class Flag(Argument):
    """"""

    def key(self, name: S) -> LS:
        """"""
        ignore(self)
        return [
            NONE.join((HYPHEN_MINUS, name[0])),
            NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
        ]


class Name(Argument):
    """"""

    def key(self, name: S) -> LS:
        """"""
        ignore(self)
        return [name]


class Application(Flag, Help):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, fallback: S, help: S) -> N:
        """"""
        ignore(self)
        super().__init__(
            arguments=True,
            attribute=True,
            fallback=fallback,
            help=help,
        )


class Customization(Flag, Help, Choices):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, fallback: S, help: S, choices: LS) -> N:
        """"""
        ignore(self)
        super().__init__(
            arguments=bool(choices),
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
        ignore(self)
        super().__init__(
            arguments=True,
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
        ignore(self)
        super().__init__(
            arguments=True,
            attribute=True,
            fallback=fallback,
            help=help,
        )


class Information(Flag, Action, Help):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, action: S, help: S) -> N:
        """"""
        ignore(self)
        super().__init__(
            arguments=True,
            attribute=False,
            fallback=NONE,
            action=action,
            help=help,
        )


class InformationConfiguration(Information):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, help: S) -> N:
        """"""
        ignore(self)
        super().__init__(
            action=Actions.STORE_TRUE,
            help=help,
        )


class InformationHelp(Information):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, help: S) -> N:
        """"""
        ignore(self)
        super().__init__(
            action=Actions.HELP,
            help=help,
        )


class InformationVersion(Information, Version):
    """"""

    # pylint: disable-next=redefined-builtin
    def __init__(self, help: S) -> N:
        """"""
        ignore(self)
        super().__init__(
            action=Actions.VERSION,
            help=help,
        )
