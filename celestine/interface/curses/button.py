""""""

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def __init__(self, text, **star):
        super().__init__(
            F"button:{text}",
            "button",
            **star,
        )
