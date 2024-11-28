""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ3,
    VP,
    VZ,
    B,
    N,
    S,
)


class Font:
    """"""

    def render(self, text: S, antialias: B, color: TZ3) -> Surface:
        """"""
        raise NotImplementedError(self, text, antialias, color)

    def __init__(self, file_path: VP = None, size: VZ = None) -> N:
        """"""
        raise NotImplementedError(self, file_path, size)


def init() -> N:
    """"""
    raise NotImplementedError()
