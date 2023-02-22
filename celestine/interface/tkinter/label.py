""""""

from celestine.window.label import Label as label

from .element import Element

from . import package


class Label(Element, label):
    """"""

    def __init__(self, text, **star):
        super().__init__(
            F"label:{text}",
            "label",
            **star,
        )

