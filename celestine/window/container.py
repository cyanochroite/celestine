""""""

import math

from celestine.window.collection import Rectangle


class Container(Rectangle):
    """"""

    def call(self, tag, text, action, **star):
        """"""
        self.save(
            self._button(
                tag,
                text,
                call=self.window.work,
                action=action,
                argument=star,
                this=self.this,
                **star,
            )
        )

    def drop(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            Drop(
                self.this,
                tag,
                self.window,
                self.element,
                **star,
            ),
        )

    def grid(self, tag, width, height, **star):
        """"""
        return self.item_set(
            tag,
            Grid(
                self.this,
                tag,
                self.window,
                self.element,
                width=width,
                height=height,
                **star,
            ),
        )

    def span(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            Span(
                self.this,
                tag,
                self.window,
                self.element,
                **star,
            ),
        )

    def image(self, tag, image):
        """"""
        self.save(
            self._image(
                tag,
                image,
            )
        )

    def label(self, tag, text):
        """"""
        self.save(
            self._label(
                tag,
                text,
            )
        )

    def draw(self, view, **star):
        """"""
        for _, item in self.item.items():
            item.draw(view, **star)

    def poke(self, x_dot, y_dot, **star):
        """"""
        for _, item in self.item.items():
            item.poke(x_dot, y_dot, **star)

    def spot(self, x_min, y_min, x_max, y_max, **star):
        """"""
        for _, item in self.item.items():
            item.spot(x_min, y_min, x_max, y_max, **star)

    def view(self, tag, text, action):
        """"""
        item = self._button(
            tag, text, call=self.turn, action=action, argument={}
        )
        return self.save(item)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(
        self,
        this,
        name,
        window,
        element,
        **star,
    ):
        self.this = this

        self.tag = name
        self.window = window

        self.data = None
        #
        self.element = element
        self._button = element["button"]
        self._image = element["image"]
        self._label = element["label"]

        self.turn = window.turn
        super().__init__(**star)


class Grid(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = self.width
        partition_y = math.ceil(len(self.item) / self.width)
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        items = self.__iter__()

        for _ in range(partition_y):
            (ymin, ymax) = next(axis_y)

            for _ in range(partition_x):
                (xmin, xmax) = next(axis_x)

                (_, item) = next(items)
                item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()

    def __init__(
        self,
        this,
        name,
        window,
        element,
        *,
        width,
        height,
        **star,
    ):
        super().__init__(
            this,
            name,
            window,
            element,
            **star,
        )

        self.width = width

        for range_y in range(height):
            for range_x in range(width):
                tag = f"{self.tag}_{range_x}-{range_y}"
                self.item[tag] = None


class Drop(Container):
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


class Span(Container):
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
