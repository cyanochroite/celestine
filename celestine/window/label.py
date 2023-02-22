""""""

from .element import Element


class Label(Element):
    """"""

    def __init__(self, tag, text, **star):
        self.text = text
        super().__init__(tag, **star)
