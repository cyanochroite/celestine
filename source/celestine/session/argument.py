""""""

from celestine.text import VERSION_NUMBER
from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import NONE
from celestine.text.unicode import QUESTION_MARK

from .attribute import Attribute
from .attribute import Action
from .attribute import Choices
from .attribute import Help
from .attribute import Nargs

from .hash import HashClass

from .text import VERSION


class Argument(HashClass, Attribute):
    """abstract class"""

    def __init__(
        self,
        use: bool,
        fallback: str,
        **kwargs,
    ) -> None:
        """"""

        super().__init__(**kwargs)
        self.fallback = fallback
        self.use = use

    def key(
        self,
        name: str,
    ) -> list[str]:
        ...


class Flag(Argument):
    """"""

    def key(
        self,
        name: str,
    ) -> list[str]:
        """"""

        return [
            NONE.join((HYPHEN_MINUS, name[0])),
            NONE.join((HYPHEN_MINUS, HYPHEN_MINUS, name)),
        ]


class Name(Argument):
    """"""

    def key(
        self,
        name: str,
    ) -> list[str]:
        """"""

        return [
            name,
        ]


class Optional(Flag, Help):
    """"""

    def __init__(
        self,
        fallback: str,
        help: str,
    ):
        super().__init__(
            use=True,
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
            use=True,
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
            use=True,
            fallback=fallback,
            help=help,
            choices=choices,
            nargs=QUESTION_MARK,
        )


class Information(Flag, Action, Help):
    """"""

    def dictionary(
        self,
    ):
        """"""

        true = {VERSION: VERSION_NUMBER}
        false = {}
        boolean = true if self.version is True else false
        return super().dictionary() | boolean

    def __init__(
        self,
        fallback: str,
        action: str,
        help: str,
        version: bool
    ):
        super().__init__(
            use=False,
            fallback=fallback,
            action=action,
            help=help,
        )
        self.version = version
