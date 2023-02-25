""""""

from typing import TypeAlias as TA

from celestine.text import VERSION_NUMBER
from celestine.typed import (
    A,
    D,
    L,
    N,
    S,
)

from .text import (
    ACTION,
    CHOICES,
    HELP,
    NARGS,
    VERSION,
)

AT: TA = D[S, A]


class Attribute:
    """"""

    def dictionary(self) -> AT:
        """"""
        return {}


class Action(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {ACTION: self.action}

    def __init__(self, action: S, **kwargs) -> N:
        """"""
        super().__init__(**kwargs)
        self.action = action


class Choices(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {CHOICES: self.choices}

    def __init__(self, choices: L[S], **kwargs) -> N:
        """"""
        super().__init__(**kwargs)
        self.choices = choices


class Help(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {HELP: self.help}

    def __init__(self, help: S, **kwargs) -> N:  # pylint: disable=W0622
        """"""
        super().__init__(**kwargs)
        self.help = help


class Nargs(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {NARGS: self.nargs}

    def __init__(self, nargs: S, **kwargs) -> N:
        """"""
        super().__init__(**kwargs)
        self.nargs = nargs


class Version(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {VERSION: VERSION_NUMBER}

    def __init__(self, **kwargs) -> N:
        """"""
        super().__init__(**kwargs)
