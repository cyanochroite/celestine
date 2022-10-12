from .widget import Widget


class Label(Widget):
    def __init__(self, window, font, text, cord_x, cord_y):
        super().__init__(
            window,
            font.render(text, True, (255, 255, 255)),
            (cord_x, cord_y)
        )
