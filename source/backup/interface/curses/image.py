from .widget import Widget


class Image(Widget):
    def __init__(self, frame, text):
        super().__init__(
            frame,
            F"image:{text}",
            "image",
        )
