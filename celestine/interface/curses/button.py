from .element import Element


class Button(Element):
    def __init__(self, frame, text, action):
        super().__init__(
            frame,
            F"button:{text}",
            "button",
        )
        self.action = action
