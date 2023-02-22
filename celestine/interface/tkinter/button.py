""""""

from . import package

from celestine.window.button import Button as button

from .element import Element


class Button(Element, button):
    """"""

    def __init__(self, frame, text, command):
        super().__init__(
            package.Button(
                frame,
                text=text,
                command=command,
            )
        )
