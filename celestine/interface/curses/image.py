""""""

from celestine.window.image import Image as image

from .element import Element


class Image(image, Element):
    """"""

    def draw(self, frame, **star):
        """"""
        star.update(text=F"image:{self.image}")
        super().draw(frame, **star)
