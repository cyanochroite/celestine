""""""

from celestine.package.PIL.Image import Image
from celestine.typed import (
    F,
    N,
    R,
)


class Brightness:
    """
    Adjust image brightness.

    This class can be used to control the brightness of an image.
    An enhancement factor of 0.0 gives a black image.
    A factor of 1.0 gives the original image.
    """

    def enhance(self, factor: F) -> Image:
        """Returns an enhanced image."""
        raise NotImplementedError(self, factor)

    def __init__(self, image: Image, **star: R) -> N:
        """"""
        raise NotImplementedError(self, image)


class Color:
    """
    Adjust image color balance.

    This class can be used to adjust the colour balance of an image,
    in a manner similar to the controls on a colour TV set.
    An enhancement factor of 0.0 gives a black and white image.
    A factor of 1.0 gives the original image.
    """

    def enhance(self, factor: F) -> Image:
        """Returns an enhanced image."""
        raise NotImplementedError(self, factor)

    def __init__(self, image: Image, **star: R) -> N:
        """"""
        raise NotImplementedError(self, image)


class Contrast:
    """
    Adjust image contrast.

    This class can be used to control the contrast of an image,
    similar to the contrast control on a TV set.
    An enhancement factor of 0.0 gives a solid gray image.
    A factor of 1.0 gives the original image.
    """

    def enhance(self, factor: F) -> Image:
        """Returns an enhanced image."""
        raise NotImplementedError(self, factor)

    def __init__(self, image: Image, **star: R) -> N:
        """"""
        raise NotImplementedError(self, image)


class Sharpness:
    """
    Adjust image sharpness.

    This class can be used to adjust the sharpness of an image.
    An enhancement factor of 0.0 gives a blurred image,
    a factor of 1.0 gives the original image,
    and a factor of 2.0 gives a sharpened image.
    """

    def enhance(self, factor: F) -> Image:
        """Returns an enhanced image."""
        raise NotImplementedError(self, factor)

    def __init__(self, image: Image, **star: R) -> N:
        """"""
        raise NotImplementedError(self, image)
