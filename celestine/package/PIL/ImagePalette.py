""""""

from celestine.data import wrapper, wrap
from celestine.package.PIL.Image import Image
from celestine.typed import (
    N,
    Z,
    R,
    ignore,
)


@wrapper(__name__)
class ImagePalette:
    """"""

    def __init__(self, **star: R) -> N:
        """"""
        ignore(self)
        mode: str = 'RGB'
        palette = [125, 123, 188]
        wrap(mode, palette, **star)
