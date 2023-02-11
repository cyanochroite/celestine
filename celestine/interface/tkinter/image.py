from . import package
from .widget import Widget


class Image(Widget):
    def __init__(self, frame, file):
        image = package.PhotoImage(file=file)
        self.height = image.height()
        self.image = image
        self.width = image.width()
        self.name = file
        super().__init__(
            package.Label(
                frame,
                image=image,
            )
        )
