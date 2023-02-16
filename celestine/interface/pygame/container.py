""""""

from celestine.window.collection import Rectangle

from .button import Button
from .image import Image
from .label import Label


class Container(Rectangle):
    """"""

    def drop(self, tag, **kwargs):
        """Elements go down. Like a <div> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Drop(
                self.session,
                tag,
                self.turn,
                self.font,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                offset_x=0,
                offset_y=50,
                **kwargs,
            )
        )

    def grid(self, tag, width, **kwargs):
        """Elements go in a grid. Like the <table> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Grid(
                self.session,
                tag,
                self.turn,
                self.font,
                width,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                offset_x=250,
                offset_y=250,
                **kwargs,
            )
        )

    def span(self, tag, **kwargs):
        """Elements go sideways. Like a <span> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Span(
                self.session,
                tag,
                self.turn,
                self.font,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                offset_x=500,
                offset_y=0,
                **kwargs,
            )
        )

    def draw(self, collection):
        """"""
        for (_, item) in self.item.items():
            item.draw(collection)

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        super().spot(x_min, y_min, x_max, y_max)
        for (_, item) in self.item.items():
            item.spot(x_min, y_min, x_max, y_max)

    def poke(self, x_dot, y_dot):
        """"""
        for (_, item) in self.item.items():
            item.poke(x_dot, y_dot)

    def button(self, tag, text, action):
        """"""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Button(
                self.font,
                text,
                action=lambda: self.turn(action),
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
            ),
        )

    def image(self, tag, image):
        """"""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Image(
                image,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
            ),
        )

    def label(self, tag, text):
        """"""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Label(
                self.font,
                text,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
            ),
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, session, name, turn, font, **kwargs):
        self.session = session
        self.tag = name
        self.turn = turn
        self.font = font
        super().__init__(**kwargs)

    def area(self, size):
        length = len(self.item)
        partition = length or 1
        segment = size / partition
        return segment


class Grid(Container):
    """"""

    def get_next(self):
        """"""
        x_min = self.move_x_min + self.offset_x * (self.index_x + 0)
        y_min = self.move_y_min + self.offset_y * (self.index_y + 0)
        x_max = self.move_x_min + self.offset_x * (self.index_x + 1)
        y_max = self.move_y_min + self.offset_y * (self.index_y + 1)

        self.index_x += 1
        if self.index_x >= self.width:
            self.index_x = 0
            self.index_y += 1

        return (x_min, y_min, x_max, y_max)

    def get_x_min(self):
        """"""

    def get_tag(self, name):
        """"""
        return F"{name}_{self.index_x}-{self.index_y}"

    def __init__(self, session, name, turn, font, width, **kwargs):
        self.index_x = 0
        self.index_y = 0
        self.width = width
        super().__init__(session, name, turn, font, **kwargs)


class Drop(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        size = self.area(y_max)
        self.axis_x.set(x_min, x_max, x_max)
        self.axis_y.set(y_min, y_max, size)
        for (_, item) in self.item.items():
            item.spot(x_min, y_min, x_max, size)


class Span(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        size = self.area(x_max)
        self.axis_x.set(x_min, x_max, size)
        self.axis_y.set(y_min, y_max, y_max)
        for (_, item) in self.item.items():
            item.spot(x_min, y_min, size, y_max)