""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ3,
    VP,
    VZ,
    B,
    N,
    R,
    S,
)


class Font:
    """"""

    def render(
        self,
        text: S,
        antialias: B,
        color: TZ3,
        **star: R,
    ) -> Surface:
        """"""
        raise NotImplementedError(self, text, antialias, color)

    def __init__(
        self, file_path: VP = None, size: VZ = None, **star: R
    ) -> N:
        """"""
        raise NotImplementedError(self, file_path, size)


def init(**star: R) -> N:
    """"""
    raise NotImplementedError()
