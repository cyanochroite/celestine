""""""

from celestine.text import VERSION_NUMBER

from celestine.typed import D
from celestine.typed import L
from celestine.typed import S
from celestine.typed import TA

from .text import ACTION
from .text import CHOICES
from .text import HELP
from .text import NARGS
from .text import VERSION


AT: TA = D[S, S | L[S]]


class Attribute():
    """"""

    def dictionary(self) -> AT:
        """"""
        return {}


class Action(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {ACTION: self.action}

    def __init__(self, action: S, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.action = action


class Choices(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {CHOICES: self.choices}

    def __init__(self, choices: L[S], **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.choices = choices


class Help(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {HELP: self.help}

    def __init__(self, help: S, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.help = help


class Nargs(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {NARGS: self.nargs}

    def __init__(self, nargs: S, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.nargs = nargs


class Version(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {VERSION: VERSION_NUMBER}

    def __init__(self, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
