""""""

from celestine.package.pillow.Image import Image
from celestine.typed import (
    N,
    Z,
)


class PhotoImage:
    """"""

    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def __init__(self, image: Image) -> N:
        """"""
        raise NotImplementedError(self, image)
