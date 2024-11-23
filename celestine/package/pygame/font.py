""""""

import typing

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ3,
    B,
    N,
    P,
    S,
    Z,
)


class Font(typing.Protocol):
    """"""

    def __init__(self, file_path: P, size: Z) -> N:
        """"""
        raise NotImplementedError(self, file_path, size)

    def render(
        self,
        text: S,
        antialias: B,
        color: TZ3,
        background: Surface,
    ) -> Surface:
        """"""
        raise NotImplementedError(
            self,
            text,
            antialias,
            color,
            background,
        )


def init() -> N:
    """"""
    raise NotImplementedError()
