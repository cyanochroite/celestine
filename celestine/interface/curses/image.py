from .element import Element


class Image(Element):
    def __init__(self, text, **star):
        super().__init__(
            F"image:{text}",
            "image",
            **star,
        )
