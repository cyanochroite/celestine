""""""

from celestine.data import wrapper
from celestine.package.PIL.Image import Image
from celestine.typed import (
    N,
    Z,
)


@wrapper(__name__)
class PhotoImage:
    """"""

    @wrapper(__name__)
    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def __init__(self, image: Image) -> N:
        """"""
        raise NotImplementedError(self, image)
