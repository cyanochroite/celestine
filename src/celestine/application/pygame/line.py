from . import package
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
        item = Button(
            self.row,
            label,
            action,
        )
        item.grid(self.frame.cord_x, self.frame.cords_y())

        package.draw.line(self.row, (255, 255, 255),
                          (200, 20), (200, 580), 5)

        return item

    def image(self, tag, label):
        item = Image(
            self.row,
            label,
        )
        item.grid(self.frame.cord_x, self.frame.cords_y())

        package.draw.line(self.row, (255, 255, 255),
                          (400, 20), (400, 580), 5)

        return item

    def label(self, tag, label):
        item = Label(
            self.row,
            label,
        )
        item.grid(self.frame.cord_x, self.frame.cords_y())
        package.draw.line(self.row, (255, 255, 255),
                          (20, 200), (580, 200), 5)

        return item
