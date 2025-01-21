""""""

from celestine.data import (
    wrap,
    wrapper,
)
from celestine.typed import (
    N,
    R,
    ignore,
)


@wrapper(__name__)
class ImagePalette:
    """"""

    def __init__(self, **star: R) -> N:
        """"""
        ignore(self)
        mode: str = "RGB"
        palette = [125, 123, 188]
        wrap(mode, palette, **star)
