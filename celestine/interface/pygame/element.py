""""""

from celestine.window.element import Element as element


class Element(element):
    """"""

    def draw(self, collection):
        """"""
        position = (self.x_min, self.y_min)
        collection.blit(self.item, position)

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def __init__(self, item, **star):
        self.item = item
        super().__init__(**star)
