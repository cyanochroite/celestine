""""""

from .element import Element


class Button(Element):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        if super().poke(x_dot, y_dot):
            self.action()

    def __init__(self, action, **star):
        self.action = action
        super().__init__(**star)
