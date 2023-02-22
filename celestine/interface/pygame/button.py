""""""

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def draw(self, collection, **star):
        """"""
        font = star.get("font")
        text = F"Button{self.text}"
        self.item = font.render(text, True, (255, 255, 255))
        super().draw(collection, **star)

