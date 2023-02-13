""""""

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def __init__(self, font, text, **star):
        item = font.render(F"Button{text}", True, (255, 255, 255))
        super().__init__(item, **star)
