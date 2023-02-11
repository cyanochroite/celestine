""""""

from . import package

from .element import Element


class Button(Element):
    """"""

    def __init__(self, text, action):
        """"""
        self.action = action
        self.text = text
        super().__init__()

    def draw(self, collection, **star):
        """"""
        star.update(command=self.action, text=self.text)
        self.item = package.Button(collection, **star)
        super().draw(collection, **star)
