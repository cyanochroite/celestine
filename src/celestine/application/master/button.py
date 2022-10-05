from .widget import Widget


class Button(Widget):
    def __init__(self, frame, text, action):
        super().__init__(
            frame,
            F"button:{text}",
            "button",
        )
        self.action = action
