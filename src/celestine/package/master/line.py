from .button import Button
from .image import Image
from .label import Label


class Line():
    def __init__(self, frame, tag):
        self.frame = frame
        self.tag = tag
        self.row = frame.frame

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def select(self, cord_x, cord_y):
        return False

    def unselect(self, cord_x, cord_y):
        return False

    def button(self, tag, label, action):
        pass

    def image(self, tag, label):
        pass

    def label(self, tag, label):
        pass
