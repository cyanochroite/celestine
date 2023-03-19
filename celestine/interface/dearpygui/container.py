""""""

from celestine.window.container import Container as container
from celestine.window.container import Grid as grid

from . import package
from .button import Button
from .image import Image
from .label import Label


class Container(container):
    """"""

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
