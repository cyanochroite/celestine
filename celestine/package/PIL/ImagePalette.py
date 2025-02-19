""""""

from celestine.data import wrap
from celestine.typed import (
    N,
    R,
    ignore,
)


class ImagePalette:
    """"""

    def __init__(self, **star: R) -> N:
        """"""
        ignore(self)
        mode: str = "RGB"
        palette = [125, 123, 188]
        wrap(mode, palette, **star)
