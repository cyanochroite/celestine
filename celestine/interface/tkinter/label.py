""""""

from celestine.window.label import Label as label

from .element import Element

from . import package


class Label(Element, label):
    """"""

    def draw(self, collection, **star):
        """"""
        self.item = package.Label
        star.update(text=F"label:{self.text}")
        star.update(width=100)
        star.update(height=4)
        star.update(fg="blue")
        super().draw(collection, **star)

