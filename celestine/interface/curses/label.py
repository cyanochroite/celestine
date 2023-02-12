""""""

from .element import Element


class Label(Element):
    """"""

    def __init__(self, text, **star):
        super().__init__(
            F"label:{text}",
            "label",
            **star,
        )
