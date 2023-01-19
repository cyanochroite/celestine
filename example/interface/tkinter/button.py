from . import package
from .widget import Widget


class Button(Widget):
    def __init__(self, frame, text, command):
        super().__init__(
            package.Button(
                frame,
                text=text,
                command=command,
            )
        )
