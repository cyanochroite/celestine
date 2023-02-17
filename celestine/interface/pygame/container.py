""""""

import math

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


class Grid(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.axis_x.set(x_min, x_max)
        self.axis_y.set(y_min, y_max)

        length = len(self.item)
        width = self.width
        height = math.ceil(length / width)

        items = [item for (_, item) in self.item.items()]

        axis_y = self.axis_y.get(height)
        for index_y in range(height):
            (ymin, ymax) = next(axis_y)

            axis_x = self.axis_x.get(width)
            for index_x in range(self.width):
                (xmin, xmax) = next(axis_x)

                index = index_y * self.width + index_x
                item = items[index]
                item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()
        """"""

    def get_tag(self, name):
        """"""
        length = len(self.item)
        index_x = length % self.width
        index_y = length // self.width

        return F"{name}_{index_x}-{index_y}"

    def __init__(self, session, name, turn, font, width, **kwargs):
        self.width = width
        super().__init__(session, name, turn, font, **kwargs)


class Drop(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.axis_x.set(x_min, x_max)
        self.axis_y.set(y_min, y_max)

        partition = len(self.item)

        axis_x = self.axis_x.get(1)
        axis_y = self.axis_y.get(partition)

        for (_, item) in self.item.items():
            (xmin, xmax) = next(axis_x)
            (ymin, ymax) = next(axis_y)

            item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()


class Span(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.axis_x.set(x_min, x_max)
        self.axis_y.set(y_min, y_max)

        partition = len(self.item)

        axis_x = self.axis_x.get(partition)
        axis_y = self.axis_y.get(1)

        for (_, item) in self.item.items():
            (xmin, xmax) = next(axis_x)
            (ymin, ymax) = next(axis_y)

            item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()

