""""""

import math

from celestine.typed import (
    D,
    N,
    S,
    GE,
    Z,
)
from celestine.window.collection import (
    Rectangle,
    Collection,
    Item,
)


class Container(Item, Collection):
    """"""

    item: D[S, Item]

    def partition(self, partition_x: Z, partition_y: Z) -> GE[Rectangle, N, N]:
        """"""

        size_x, size_y = self.area.size

        fragment_x = size_x // partition_x
        fragment_y = size_y // partition_y

        for index_y in range(partition_y):
            ymin = self.area.upper + fragment_y * (index_y + 0)
            ymax = self.area.upper + fragment_y * (index_y + 1)
            for index_x in range(partition_x):
                xmin = self.area.left + fragment_x * (index_x + 0)
                xmax = self.area.left + fragment_x * (index_x + 1)

                yield Rectangle(xmin, ymin, xmax, ymax)

    def call(self, name, text, action, **star):
        """"""
        self.save(
            self._button(
                name,
                text,
                call=self.window.work,
                action=action,
                argument=star,
                ring=self.ring,
                **star,
            )
        )

    def drop(self, name: S, **star):
        """"""
        return self.item_set(
            name,
            Drop(
                self.ring,
                name,
                self.window,
                self.element,
                self.area,
                **star,
            ),
        )

    def grid(self, name, width, height, **star):
        """"""
        return self.item_set(
            name,
            Grid(
                self.ring,
                name,
                self.window,
                self.element,
                self.area,
                width=width,
                height=height,
                **star,
            ),
        )

    def span(self, name, **star):
        """"""
        return self.item_set(
            name,
            Span(
                self.ring,
                name,
                self.window,
                self.element,
                self.area,
                **star,
            ),
        )

    def image(self, name, path):
        """A thumbnail image of a big picture."""
        self.save(
            self._image(
                name,
                path,
            )
        )

    def label(self, name, text):
        """"""
        self.save(
            self._label(
                name,
                text,
            )
        )

    def draw(self, ring, view, **star):
        """"""
        for _, item in self.item.items():
            item.draw(ring, view, **star)

    def poke(self, x_dot, y_dot, **star):
        """"""
        for _, item in self.item.items():
            item.poke(x_dot, y_dot, **star)

    def spot(self, area: Rectangle, **star):
        """"""
        for _, item in self.item.items():
            item.spot(area, **star)

    def view(self, name, text, action):
        """"""
        item = self._button(
            name,
            text,
            call=self.turn,
            action=action,
            argument={},
        )
        return self.save(item)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(
        self,
        ring,
        name,
        window,
        element,
        area,
        **star,
    ):
        self.ring = ring

        self.window = window

        self.data = None
        #
        self.element = element
        self._button = element["button"]
        self._image = element["image"]
        self._label = element["label"]

        self.turn = window.turn

        super().__init__(name, area, **star)


class Grid(Container):
    """"""

    def spot(self, area: Rectangle, **star) -> N:
        """"""
        self.area.set(area.axis_x, area.axis_y)

        partition_x = self.width
        partition_y = math.ceil(len(self.item) / self.width)
        (axis_x, axis_y) = self.area.get(partition_x, partition_y)

        items = iter(self)

        for _ in range(partition_y):
            (ymin, ymax) = next(axis_y)

            for _ in range(partition_x):
                (xmin, xmax) = next(axis_x)

                (_, item) = next(items)

                area = Area(Axis(xmin, xmax), Axis(ymin, ymax))
                item.spot(area)

        axis_x.close()
        axis_y.close()

    def __init__(
        self,
        ring,
        name,
        window,
        element,
        area,
        *,
        width,
        height,
        **star,
    ) -> N:
        super().__init__(
            ring,
            name,
            window,
            element,
            area,
            **star,
        )

        self.width = width

        for range_y in range(height):
            for range_x in range(width):
                name = f"{self.name}_{range_x}-{range_y}"
                self.item[name] = Item(name, area)


class Drop(Container):
    """"""

    def spot(self, area: Rectangle, **star) -> N:
        """"""
        self.area.copy(area)

        partition_x = 1
        partition_y = len(self.item)

        box = self.partition(partition_x, partition_y)
        for _, item in self.item.items():
            item.spot(next(box))
        box.close()


class Span(Container):
    """"""

    def spot(self, area: Rectangle, **star) -> N:
        """"""
        self.area.copy(area)

        partition_x = len(self.item)
        partition_y = 1

        box = self.partition(partition_x, partition_y)
        for _, item in self.item.items():
            item.spot(next(box))
        box.close()
