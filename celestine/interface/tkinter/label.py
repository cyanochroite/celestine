""""""

from . import package

from .element import Element


class Label(Element):
    """"""

    def draw(self, collection, **star):
        """"""
        star.update(text=self.text)
        self.item = package.Label(collection, **star)
        super().draw(collection, **star)

    def __init__(self, text, **star):
        """"""
        self.text = text
        super().__init__(**star)
