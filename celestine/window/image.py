""""""

from .element import Element


class Image(Element):
    """"""

    def __init__(self, image, **star):
        self.image = image
        super().__init__(**star)
