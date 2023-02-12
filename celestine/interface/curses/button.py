""""""


from .element import Element


class Button(Element):
    """"""

    def __init__(self, text, action, **star):
        super().__init__(
            F"button:{text}",
            "button",
            **star,
        )
        self.action = action
