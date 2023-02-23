""""""

from celestine.window.label import Label as label

from .element import Element


class Label(label, Element):
    """"""

    def draw(self, collection, **star):
        """"""
        font = star.get("font")
        self.item = font.render(self.text, True, (255, 255, 255))
        super().draw(collection, **star)
