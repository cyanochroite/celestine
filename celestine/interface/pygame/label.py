""""""

from .element import Element


class Label(Element):
    """"""

    def __init__(self, font, text, **star):
        super().__init__(font.render(text, True, (255, 255, 255)), **star)


