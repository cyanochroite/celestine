""""""

from celestine.window.collection import Rectangle


class Container(Rectangle):
    """"""

    def drop(self, tag, **kwargs):
        """"""
        raise NotImplementedError()

    def grid(self, tag, width, **kwargs):
        """"""
        raise NotImplementedError()

    def span(self, tag, **kwargs):
        """"""
        raise NotImplementedError()

    def ready(self, button, image, label):
        """"""
        self._button = button
        self._image = image
        self._label = label

    def button(self, tag, text, action):
        """"""
        item = self._button(tag, text, action=lambda: self.turn(action))
        return self.save(item)

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

    def task(self, tag, text, action):
        """"""
        call = self.window.work
        item = self._button(tag, text, action=lambda: call(action))
        return self.save(item)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, session, name, window, **star):
        self.session = session
        self.tag = name
        self.window = window
        #
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

    def __init__(self, session, name, turn, *, width, **kwargs):
        self.width = width
        super().__init__(session, name, turn, **kwargs)
