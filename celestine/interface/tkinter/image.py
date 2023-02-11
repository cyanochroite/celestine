""""""

from .element import Element
from . import package


class Image(Element):
    """"""

    def draw(self, collection, **star):
        """"""
        star.update(image=self.image)
        package.Label(collection, **star)
        super().draw(collection, **star)

    def __init__(self, file):
        self.image = package.PhotoImage(file=file)
        self.height = self.image.height()
        self.width = self.image.width()
        self.name = file
        super().__init__()
