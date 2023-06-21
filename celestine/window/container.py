""""""

import math

from celestine.typed import (
    GE,
    D,
    N,
    S,
    Z,
)
from celestine.window.collection import (
    Collection,
    Item,
    Rectangle,
)


class Container(Item, Collection):
    """"""

    item: D[S, Item]

    def partition(self, partition_x: Z, partition_y: Z) -> GE[Rectangle, N, N]:
        """"""

        items = iter(self.item.items())
        size_x, size_y = self.area.size

        fragment_x = size_x // partition_x
        fragment_y = size_y // partition_y

        for index_y in range(partition_y):
            ymin = self.area.upper + fragment_y * (index_y + 0)
            ymax = self.area.upper + fragment_y * (index_y + 1)
            for index_x in range(partition_x):
                xmin = self.area.left + fragment_x * (index_x + 0)
                xmax = self.area.left + fragment_x * (index_x + 1)

                _, item = next(items)
                rectangle = Rectangle(xmin, ymin, xmax, ymax)
                item.spot(rectangle)

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

    def image(self, name, path, **star):
        """A thumbnail image of a big picture."""
        self.save(
            self._image(
                name,
                path,
                **star,
            )
        )

    def label(self, name, text, **star):
        """"""
        self.save(
            self._label(
                name,
                text,
                **star,
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

    def tag(self) -> S:
        """"""
        length = len(self.item)
        range_x = length % self.width
        range_y = length // self.width
        name = f"{self.name}_{range_x}-{range_y}"
        return name

    def spot(self, area: Rectangle, **star) -> N:
        """"""
        self.area.copy(area)

        partition_x = self.width
        partition_y = math.ceil(len(self.item) / self.width)

        self.partition(partition_x, partition_y)

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
        self.height = height

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

        self.partition(partition_x, partition_y)


class Span(Container):
    """"""

    def spot(self, area: Rectangle, **star) -> N:
        """"""
        self.area.copy(area)

        partition_x = len(self.item)
        partition_y = 1

        self.partition(partition_x, partition_y)
