""""""

from celestine.window.collection import Box


class Element(Box):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        return self.inside(x_dot, y_dot)

