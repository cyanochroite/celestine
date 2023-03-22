""""""

import math

from celestine.window.collection import Rectangle


class Container(Rectangle):
    """"""

    def call(self, tag, text, action, **star):
        """"""
        item = self._button(
            tag,
            text,
            call=self.window.work,
            action=action,
            argument=star,
        )
        return self.save(item)

    def drop(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            Drop(
                self.session,
                tag,
                self.window,
                self._button,
                self._image,
                self._label,
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
                self._button,
                self._image,
                self._label,
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
                self._button,
                self._image,
                self._label,
                **star,
            ),
        )

    def image(self, tag, image):
        """"""
        item = self._image(tag, image)
        return self.save(item)

    def label(self, tag, text):
        """"""
        item = self._label(tag, text)
        return self.save(item)

    def draw(self, collection, **star):
        """"""
        for _, item in self.item.items():
            item.draw(collection, **star)

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
        session,
        name,
        window,
        _button,
        _image,
        _label,
        **star,
    ):
        self.session = session
        self.tag = name
        self.window = window

        self.data = None
        #
        self._button = _button
        self._image = _image
        self._label = _label

        self.turn = window.turn
        super().__init__(**star)


class Grid(Container):
    """"""

    def button(self, tag, text, action):
        """"""
        name = self._get_tag(tag)
        super().button(name, text, action)

    def image(self, tag, image):
        """"""
        name = self._get_tag(tag)
        super().image(name, image)

    def label(self, tag, text):
        """"""
        name = self._get_tag(tag)
        super().label(name, text)

    def items(self):
        """"""
        yield from [item for (_, item) in self.item.items()]

    def _get_tag(self, name):
        """"""
        length = len(self.item)
        index_x = length % self.width
        index_y = length // self.width

        return f"{name}_{index_x}-{index_y}"

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

    def __init__(
        self,
        session,
        name,
        window,
        _button,
        _image,
        _label,
        *,
        width,
        **star,
    ):
        self.width = width
        super().__init__(
            session,
            name,
            window,
            _button,
            _image,
            _label,
            **star,
        )


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
