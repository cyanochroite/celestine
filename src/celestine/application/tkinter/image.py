from . import tkinter
from .widget import Widget


class Image(Widget):
    def __init__(self, frame, file):
        image = tkinter.PhotoImage(file=file)
        self.height = image.height()
        self.image = image
        self.width = image.width()
        self.name = file
        super().__init__(
            tkinter.Label(
                frame,
                image=image,
            )
        )
