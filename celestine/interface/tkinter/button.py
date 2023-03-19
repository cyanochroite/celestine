""""""

from celestine.window.button import Button as button

from . import package
from .element import Element


class Button(button, Element):
    """"""

    def callback(self):
        """"""
        self.call(self.action, **self.argument)

    def draw(self, collection, **star):
        """"""
        self.item = package.Button
        star.update(text=f"button:{self.text}")
        star.update(command=self.callback)
        super().draw(collection, **star)
