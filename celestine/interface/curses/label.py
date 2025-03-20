from .widget import Widget


class Label(Widget):
    def __init__(self, frame, text):
        super().__init__(
            frame,
            F"label:{text}",
            "label",
        )
