""""""

import math

from celestine.window.container import Container as container
from celestine.window.container import Drop as drop
from celestine.window.container import Grid as grid
from celestine.window.container import Span as span

from . import package


class Container(container):
    """"""


class Drop(Container, drop):
    """"""


class Grid(Container, grid):
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


class Span(Container, span):
    """"""

    def draw(self, collection, **star):
        """"""
        frame = package.Frame(collection)
        frame.pack()
        super().draw(frame, **star)
