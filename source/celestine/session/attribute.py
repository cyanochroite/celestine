""""""

import dataclasses


@dataclasses.dataclass
class Optional():
    """"""

    default: str
    description: str


@dataclasses.dataclass
class Override():
    """"""

    default: str
    description: str
    choice: list[str]


@dataclasses.dataclass
class Positional():
    """"""

    default: str
    description: str
    choice: list[str]
