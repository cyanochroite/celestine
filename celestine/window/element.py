""""""

from celestine.window.collection import Box


class Element(Box):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        return self.inside(x_dot, y_dot)

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def __init__(self, tag, **star):
        self.item = None
        self.tag = tag
        super().__init__(**star)
