""""""

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def draw(self, frame, **star):
        """"""
        star.update(text=F"button:{self.text}")
        super().draw(frame, **star)
