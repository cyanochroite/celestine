import bpy

from celestine.window.page import Page as master

from . import package
from .package import data
from .line import Line


class Page(master):
    def line(self, tag):
        return self.item_set(
            tag,
            Line(
                self,
                tag,
                self.spawn(),
            ),
        )

    def __init__(self, window, rectangle, **kwargs):
        super().__init__(
            window.session,
            cord_x_min=rectangle.cord_x_min,
            cord_y_min=rectangle.cord_y_min,
            cord_x_max=rectangle.cord_x_max,
            cord_y_max=rectangle.cord_y_max,
            offset_y=-2.5,
            ** kwargs,
        )
        self.turn = window.turn
