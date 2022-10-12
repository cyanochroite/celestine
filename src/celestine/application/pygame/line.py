from . import package
from .button import Button
from .image import Image
from .label import Label


class Line():
    def __init__(self, page, tag):
        self.tag = tag
        self.page = page
        self.window = page.window
        self.font = page.font

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def select(self, cord_x, cord_y):
        return False

    def unselect(self, cord_x, cord_y):
        return False

    def button(self, tag, text, action):
        item = Button(
            self.window,
            self.font,
            text,
            action,
            self.page.cord_x,
            self.page.cords_y()
        )
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

    def label(self, tag, text):
        item = Label(
            self.window,
            self.font,
            text,
            self.page.cord_x,
            self.page.cords_y()
        )
        return item
