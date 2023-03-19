""""""

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
            argument=star
        )
        return self.save(item)

    def drop(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            self._drop(
                self.session,
                tag,
                self.window,
                self.data,
                self._button,
                self._image,
                self._label,
                self._drop,
                self._grid,
                self._span,
                **star,
            ),
        )

    def grid(self, tag, width, **star):
        """"""
        return self.item_set(
            tag,
            self._grid(
                self.session,
                tag,
                self.window,
                self.data,
                self._button,
                self._image,
                self._label,
                self._drop,
                self._grid,
                self._span,
                width=width,
                **star,
            ),
        )

    def span(self, tag, **star):
        """"""
        return self.item_set(
            tag,
            self._span(
                self.session,
                tag,
                self.window,
                self.data,
                self._button,
                self._image,
                self._label,
                self._drop,
                self._grid,
                self._span,
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
            tag,
            text,
            call=self.turn,
            action=action,
            argument={}
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
            data,
            _button,
            _image,
            _label,
            _drop,
            _grid,
            _span,
            **star,
    ):
        self.session = session
        self.tag = name
        self.window = window

        self.data = data
        #
        self._button = _button
        self._image = _image
        self._label = _label

        self._drop = _drop
        self._grid = _grid
        self._span = _span

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

    def __init__(
        self,
        session,
        name,
        window,
        data,
        _button,
        _image,
        _label,
        _drop,
        _grid,
        _span,
        *,
        width,
        **star,
    ):
        self.width = width
        super().__init__(
            session,
            name,
            window,
            data,
            _button,
            _image,
            _label,
            _drop,
            _grid,
            _span,
            **star,
        )


class Drop(Container):
    """"""


class Span(Container):
    """"""
