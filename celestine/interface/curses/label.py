from .element import Element


class Label(Element):
    def __init__(self, frame, text):
        super().__init__(
            frame,
            F"label:{text}",
            "label",
        )
