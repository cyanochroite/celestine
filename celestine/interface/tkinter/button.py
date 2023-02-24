""""""

from celestine.window.button import Button as button

from .element import Element

from . import package


class Button(button, Element):
    """"""

    def draw(self, collection, **star):
        """"""
        self.item = package.Button
        star.update(text=f"button:{self.text}")
        star.update(command=self.action)
        super().draw(collection, **star)
