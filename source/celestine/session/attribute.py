""""""

import dataclasses


@dataclasses.dataclass
class Attribute():
    """"""


@dataclasses.dataclass
class Optional(Attribute):
    """"""

    default: str
    description: str


@dataclasses.dataclass
class Override(Attribute):
    """"""

    default: str
    description: str
    choice: list[str]


@dataclasses.dataclass
class Positional(Attribute):
    """"""

    default: str
    description: str
    choice: list[str]
