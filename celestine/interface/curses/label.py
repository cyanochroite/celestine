""""""

from celestine.window.label import Label as label

from .element import Element


class Label(Element, label):
    """"""

    def draw(self, frame, **star):
        """"""
        star.update(text=F"label:{self.text}")
        super().draw(frame, **star)
