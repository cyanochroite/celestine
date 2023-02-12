""""""

from .element import Element


class Button(Element):
    """"""

    def __init__(self, font, text, action, **star):
        super().__init__(
            font.render(F"Button{text}", True, (255, 255, 255)),
            **star,
        )
        self.action = action
