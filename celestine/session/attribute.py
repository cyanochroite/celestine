""""""

from celestine.literal import VERSION_NUMBER
from celestine.session.data import (
    Actions,
    Attributes,
)
from celestine.typed import (
    DA,
    LS,
    N,
    R,
    S,
    ignore,
)


class Attribute:
    """"""

    def dictionary(self) -> DA:
        """"""
        ignore(self)
        return {}

    def __init__(self, **star: R) -> N:
        """"""
        ignore(self)
        super().__init__(**star)


class Action(Attribute):
    """"""

    def dictionary(self) -> DA:
        """"""
        return super().dictionary() | {Attributes.ACTION: self.action}

    def __init__(self, *, action: S, **star: R) -> N:
        """"""
        self.action = action
        super().__init__(**star)


class Choices(Attribute):
    """"""

    def dictionary(self) -> DA:
        """"""
        return super().dictionary() | {Attributes.CHOICES: self.choices}

    def __init__(self, *, choices: LS, **star: R) -> N:
        """"""
        self.choices = choices
        super().__init__(**star)


class Help(Attribute):
    """"""

    def dictionary(self) -> DA:
        """"""
        return super().dictionary() | {Attributes.HELP: self.help}

    # pylint: disable-next=redefined-builtin
    def __init__(self, *, help: S, **star: R) -> N:
        """"""
        self.help = help
        super().__init__(**star)


class Nargs(Attribute):
    """"""

    def dictionary(self) -> DA:
        """"""
        return super().dictionary() | {Attributes.NARGS: self.nargs}

    def __init__(self, *, nargs: S, **star: R) -> N:
        """"""
        self.nargs = nargs
        super().__init__(**star)


class Version(Attribute):
    """"""

    def dictionary(self) -> DA:
        """"""
        ignore(self)
        return super().dictionary() | {Actions.VERSION: VERSION_NUMBER}
