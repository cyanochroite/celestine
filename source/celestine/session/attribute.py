""""""

import typing

from .text import CHOICES
from .text import HELP
from .text import NARGS


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

        return {}

    def __init__(
        self,
        fallback: str,
    ) -> None:
        """"""

        self.fallback = fallback


class Choices(Attribute):
    """"""

    def dictionary(
        self,
    ):
        """"""

        return super().dictionary() | {CHOICES: self.choices}

    def __init__(
        self,
        choices: list[str],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.choices = choices


class Help(Attribute):
    """"""

    def dictionary(
        self,
    ):
        """"""

        return super().dictionary() | {HELP: self.help}

    def __init__(
        self,
        help: str,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.help = help


class Nargs(Attribute):
    """"""

    def dictionary(
        self,
    ):
        """"""

        return super().dictionary() | {NARGS: self.nargs}

    def __init__(
        self,
        nargs: str,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.nargs = nargs
