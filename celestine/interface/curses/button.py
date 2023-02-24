""""""

from celestine.window.button import Button as button

from .element import Element


class Button(button, Element):
    """"""

    def draw(self, frame, **star):
        """"""
        star.update(text=f"button:{self.text}")
        super().draw(frame, **star)
