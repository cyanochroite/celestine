""""""

import math

from celestine.window.container import Container as container
from celestine.window.container import Drop as drop
from celestine.window.container import Grid as grid
from celestine.window.container import Span as span


class Container(container):
    """"""


class Drop(Container, drop):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = 1
        partition_y = len(self.item)
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        for _, item in self.item.items():
            (xmin, xmax) = next(axis_x)
            (ymin, ymax) = next(axis_y)

            item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()


class Grid(Container, grid):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = self.width
        partition_y = math.ceil(len(self.item) / self.width)
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        items = self.items()

        for _ in range(partition_y):
            (ymin, ymax) = next(axis_y)

            for _ in range(partition_x):
                (xmin, xmax) = next(axis_x)

                item = next(items)
                item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()

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
        return f"{name}_{self.index_x}-{self.index_y}"


class Span(Container, span):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = len(self.item)
        partition_y = 1
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        for _, item in self.item.items():
            (xmin, xmax) = next(axis_x)
            (ymin, ymax) = next(axis_y)

            item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()
