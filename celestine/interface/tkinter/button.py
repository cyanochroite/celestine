""""""

from . import package

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def draw(self, collection, **star):
        """"""
        self.item = package.Button
        star.update(text=F"button:{self.text}")
        star.update(command=self.action)
        super().draw(collection, **star)

    def __init__(self, text, **star):
        self.text = text
        super().__init__(**star)

