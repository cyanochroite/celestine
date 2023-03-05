""""""

from celestine.window.container import Container as container
from celestine.window.container import Grid as grid

from . import package
from .button import Button
from .image import Image
from .label import Label


def callback(sender, app_data, user_data):
    """"""


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
                lambda sender, app_data, user_data: self.turn(
                    *user_data
                ),
            ),
        )

    def task(self, tag, text, action):
        """"""
        call = self.window.work
        return self.item_set(
            tag,
            Button(
                tag,
                text,
                package.tag_root(self.tag),
                action,
                lambda sender, app_data, user_data: call(action),
            ),
        )

    def drop(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            Drop(
                self.session,
                tag,
                self.window,
                **star,
            ),
        )

    def grid(self, tag, width, **star):
        """"""
        return self.item_set(
            tag,
            Grid(
                self.session,
                tag,
                self.window,
                width=width,
                **star,
            ),
        )

    def span(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            Span(
                self.session,
                tag,
                self.window,
                **star,
            ),
        )

    def __init__(self, session, name, window, **star):
        self.frame = None
        super().__init__(session, name, window, **star)
        super().ready(Button, Image, Label)


class Grid(grid, Container):
    """"""


class Drop(Container):
    """"""


class Span(Container):
    """"""
