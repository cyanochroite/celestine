""""""

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def draw(self, collection, **star):
        """"""
        font = star.get("font")
        self.item = font.render(F"Button{self.text}", True, (255, 255, 255))
        super().draw(collection, **star)

    def __init__(self, text, **star):
        self.text = text
        super().__init__(**star)

