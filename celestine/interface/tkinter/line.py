from . import package
from .button import Button
from .image import Image
from .label import Label


class Line():
    def button(self, tag, label, action):
        return self.frame.item_set(
            tag,
            Button(
                self.row,
                label,
                lambda: self.turn(action),
            ),
        )

    def image(self, tag, file):
        return self.frame.item_set(
            tag,
            Image(
                self.row,
                file,
            ),
        )

    def label(self, tag, text):
        return self.frame.item_set(
            tag,
            Label(
                self.row,
                text=text,
                width=100,
                height=4,
                fg="blue",
            ),
        )

    def __init__(self, frame, tag):
        self.turn = frame.turn
        self.frame = frame
        self.tag = tag
        self.row = package.Frame(frame.frame)

    def __enter__(self):
        self.row.pack()
        return self

    def __exit__(self, *_):
        return False
