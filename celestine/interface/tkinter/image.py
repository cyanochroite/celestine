""""""


from celestine.window.image import Image as image

from .element import Element

from . import package


class Image(Element, image):
    """"""

    def draw(self, collection, **star):
        """"""
        self.item = package.Label
        star.update(image=self.image)
        super().draw(collection, **star)

    def __init__(self, file):
        self.image = package.PhotoImage(file=file)
        self.height = self.image.height()
        self.width = self.image.width()
        self.name = file
        super().__init__()
