""""""

import celestine
from celestine.session.session import SuperSession
from celestine.typed import (
    N,
    ignore,
)


class Session(SuperSession):
    """"""


def main() -> N:
    """"""
    celestine.init(__package__)
    celestine.main("demo.draw:zero", __package__)


ignore(Session, main)
