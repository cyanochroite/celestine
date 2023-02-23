""""""

import math

from celestine.window.container import Container as container
from celestine.window.container import Grid as grid

from . import package

from .button import Button
from .image import Image
from .label import Label


class Container(container):
    """"""

    def button(self, tag, label, action):
        return self.item_set(
            tag,
            Button(
                tag,
                label,
                package.tag_root(self.tag),
                action,
                lambda sender, app_data, user_data: self.turn(*user_data),
            ),
        )

    def image(self, tag, image):
        return self.item_set(
            tag,
            Image(
                tag,
                image,
            ),
        )

    def label(self, tag, text):
        return self.item_set(
            tag,
            Label(
                tag,
                text,
                "Label",
            ),
        )

    def drop(self, tag, **kwargs):
        """"""
        return self.item_set(
            tag,
            Drop(
                self.session,
                tag,
                self.turn,
                **kwargs,
            )
        )

    def grid(self, tag, width, **kwargs):
        """"""
        return self.item_set(
            tag,
            Grid(
                self.session,
                tag,
                self.turn,
                width=width,
                **kwargs,
            )
        )

    def span(self, tag, **kwargs):
        """"""
        return self.item_set(
            tag,
            Span(
                self.session,
                tag,
                self.turn,
                **kwargs,
            )
        )

    def __init__(self, session, name, turn, **kwargs):
        self.frame = None
        super().__init__(session, name, turn, **kwargs)
        super().ready(Button, Image, Label)


class Grid(grid, Container):
    """"""

    def draw(self, collection, **star):
        """"""
        partition_x = self.width
        partition_y = math.ceil(len(self.item) / self.width)

        items = self.items()

        for _ in range(partition_y):
            frame = package.Frame(collection)
            for _ in range(partition_x):
                item = next(items)
                item.draw(frame, **star)
            frame.pack()


class Drop(Container):
    """"""


class Span(Container):
    """"""

    def draw(self, collection, **star):
        """"""
        frame = package.Frame(collection)
        frame.pack()
        super().draw(frame, **star)
