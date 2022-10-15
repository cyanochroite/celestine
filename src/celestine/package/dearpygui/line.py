from . import package
from .button import Button
from .image import Image
from .label import Label


class Line():
    def __init__(self, frame, tag):
        self.frame = frame
        self.tag = tag
        self.row = package.group(horizontal=True)

    def __enter__(self):
        self.row.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.row.__exit__(exc_type, exc_value, traceback)
        return False

    def button(self, tag, label, action):
        return self.frame.item_set(
            tag,
            Button(
                self.frame.window.item_key(self.frame.tag, tag),
                label,
                self.frame.tag,
                action,
                self.frame.window.show_frame_simple,
            ),
        )

    def image(self, tag, image):
        return self.frame.item_set(
            tag,
            Image(
                self.frame.window.item_key(self.frame.tag, tag),
                image,
            ),
        )

    def label(self, tag, text):
        return self.frame.item_set(
            tag,
            Label(
                self.frame.window.item_key(self.frame.tag, tag),
                text,
                "Label",
            ),
        )
