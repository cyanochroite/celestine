from . import package
from .button import Button
from .image import Image
from .label import Label

from .rectangle import Row
from .rectangle import Collection


class Line(Row, Collection):
    def __init__(self, page, tag, rectangle):
        super().__init__(
            cord_x_min=rectangle.cord_x_min,
            cord_y_min=rectangle.cord_y_min,
            cord_x_max=rectangle.cord_x_max,
            cord_y_max=rectangle.cord_y_max,
        )
        self.tag = tag
        self.turn = page.turn
        self.window = page.window
        self.font = page.font

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def action(self):
        pass

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()
            for child in self.children():
                child.select(cord_x, cord_y)

    def button(self, tag, text, action):
        return self.item_set(
            tag,
            Button(
                self.window,
                self.font,
                text,
                lambda: self.turn(action),
                self.spawn(),
            ),
        )

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
        return self.item_set(
            tag,
            Label(
                self.window,
                self.font,
                text,
                self.spawn(),
            ),
        )
