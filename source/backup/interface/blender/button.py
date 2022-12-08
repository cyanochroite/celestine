from .widget import Widget


class Button(Widget):
    def __init__(self, text, action, rectangle):
        super().__init__(
            text,
            rectangle,
        )
        self.action = action
