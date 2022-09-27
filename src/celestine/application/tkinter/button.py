from celestine.package import tkinter
from celestine.application.tkinter.widget import Widget


class Button(Widget):
    def __init__(self, frame, text, command):
        super().__init__(
            tkinter.Button(
                frame,
                text=text,
                command=command,
            )
        )
