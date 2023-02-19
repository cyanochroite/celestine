""""""

from celestine.window.collection import Rectangle

from .button import Button
from .image import Image
from .label import Label


class Container(Rectangle):
    """"""

    def draw(self, collection):
        """"""
        for (_, item) in self.item.items():
            item.draw(collection)

    def poke(self, x_dot, y_dot):
        """"""
        for (_, item) in self.item.items():
            item.poke(x_dot, y_dot)

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        for (_, item) in self.item.items():
            item.spot(x_min, y_min, x_max, y_max)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, session, name, turn, **kwargs):
        self.session = session
        self.tag = name
        self.turn = turn
        super().__init__(**kwargs)

