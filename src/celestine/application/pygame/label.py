from .widget import Widget


class Label(Widget):
    def __init__(self, window, font, text, rectangle):
        super().__init__(
            window,
            font.render(text, True, (255, 255, 255)),
            rectangle,
        )
