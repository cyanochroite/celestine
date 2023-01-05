""""""

from .text import NARGS
from .text import HELP
from .text import CHOICES
from .text import ACTION

from .type import AT


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

    def __init__(self, action: str, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.action = action


class Choices(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {CHOICES: self.choices}

    def __init__(self, choices: list[str], **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.choices = choices


class Help(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {HELP: self.help}

    def __init__(self, help: str, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.help = help


class Nargs(Attribute):
    """"""

    def dictionary(self) -> AT:
        """"""
        return super().dictionary() | {NARGS: self.nargs}

    def __init__(self, nargs: str, **kwargs) -> None:
        """"""
        super().__init__(**kwargs)
        self.nargs = nargs
