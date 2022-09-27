from celestine.package import tkinter
from celestine.application.tkinter.button import Button
from celestine.application.tkinter.image import Image
from celestine.application.tkinter.label import Label


class Line():
    def __init__(self, frame, tag):
        self.frame = frame
        self.tag = tag
        self.row = tkinter.Frame(frame.frame)

    def __enter__(self):
        self.row.pack()
        return self

    def __exit__(self, *_):
        return False

    def button(self, tag, label, action):
        return self.frame.item_set(
            tag,
            Button(
                self.row,
                label,
                lambda: self.frame.window[action],
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
