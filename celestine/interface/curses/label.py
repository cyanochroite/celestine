""""""

from celestine.window.label import Label as label

from .element import Element


class Label(label, Element):
    """"""

    def draw(self, frame, **star):
        """"""
        star.update(text=f"label:{self.text}")
        super().draw(frame, **star)
