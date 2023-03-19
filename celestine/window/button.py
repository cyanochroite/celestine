""""""

from .element import Element


class Button(Element):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        if super().poke(x_dot, y_dot):
            self.call(self.action, **self.argument)

    def __init__(self, tag, text, *, call, action, argument, **star):
        self.action = action
        self.argument = argument
        self.call = call
        self.text = text
        super().__init__(tag, **star)
