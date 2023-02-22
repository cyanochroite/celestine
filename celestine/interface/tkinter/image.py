""""""


from celestine.window.image import Image as image

from .element import Element

from . import package


class Image(Element, image):
    """"""

    def draw(self, collection, **star):
        """"""
        self.hold = package.PhotoImage(file=self.image)
        self.item = package.Label
        star.update(image=self.hold)
        super().draw(collection, **star)

