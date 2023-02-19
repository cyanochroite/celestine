""""""

from celestine.window.image import Image as image

from .element import Element


class Image(Element, image):
    """"""

    def __init__(self, text, **star):
        super().__init__(
            F"image:{text}",
            "image",
            **star,
        )
