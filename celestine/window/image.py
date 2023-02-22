""""""

from .element import Element


class Image(Element):
    """"""

    def __init__(self, tag, image, **star):
        self.image = image
        super().__init__(tag, **star)
