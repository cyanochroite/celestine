""""""

from celestine.window.image import Image as image

from . import package
from .element import Element


class Image(image, Element):
    """"""

    def draw(self, collection, **star):
        """"""
        self.hold = package.PhotoImage(file=self.image)
        self.item = package.Label
        star.update(image=self.hold)
        super().draw(collection, **star)
