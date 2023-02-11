""""""

from . import package

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
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                offset_x=0,
                offset_y=2.5,
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
                width,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                offset_x=2.5,
                offset_y=2.5,
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
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                offset_x=10,
                offset_y=0,
                **kwargs,
            )
        )

    def draw(self, collection):
        """"""
        for (_, item) in self.item.items():
            item.draw(collection)

    def poke(self, x_dot, y_dot):
        """"""
        for (_, item) in self.item.items():
            item.poke(x_dot, y_dot)

    def button(self, tag, text, action):
        """"""
        return self.item_set(
            tag,
            Button(text, lambda: self.turn(action)),
        )

    def image(self, tag, image):
        """"""
        return self.item_set(
            tag,
            Image(image),
        )

    def label(self, tag, text):
        """"""
        return self.item_set(
            tag,
            Label(text),
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, session, name, turn, **kwargs):
        self.session = session
        self.tag = name
        self.turn = turn
        super().__init__(**kwargs)


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

    def __init__(self, session, name, turn, width, **kwargs):
        self.index_x = 0
        self.index_y = 0
        self.width = width
        super().__init__(session, name, turn, **kwargs)


class Drop(Container):
    """"""


class Span(Container):
    """"""

    def draw(self, collection):
        """"""
        self.collection = package.Frame(collection)
        self.collection.pack()
        super().draw(self.collection)
