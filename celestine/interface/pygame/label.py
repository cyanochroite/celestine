""""""

from celestine.window.label import Label as label

from .element import Element


class Label(Element, label):
    """"""

    def draw(self, collection, **star):
        """"""
        font = star.get("font")
        self.item = font.render(self.text, True, (255, 255, 255))
        super().draw(collection, **star)

    def __init__(self, text, **star):
        self.text = text
        super().__init__(**star)


