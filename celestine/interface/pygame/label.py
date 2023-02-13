""""""

from celestine.window.label import Label as label

from .element import Element


class Label(Element, label):
    """"""

    def __init__(self, font, text, **star):
        super().__init__(font.render(text, True, (255, 255, 255)), **star)


