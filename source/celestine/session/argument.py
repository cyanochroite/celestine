""""""

import dataclasses


@dataclasses.dataclass
class Argument():
    """"""

    default: str
    description: str


@dataclasses.dataclass
class Optional(Argument):
    """"""


@dataclasses.dataclass
class Override(Argument):
    """"""

    choice: list[str]


@dataclasses.dataclass
class Positional(Argument):
    """"""

    choice: list[str]
