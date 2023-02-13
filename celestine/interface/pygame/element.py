""""""

from celestine.window.element import Element as element


class Element(element):
    """"""

    def draw(self, collection):
        """"""
        position = (self.x_min, self.y_min)
        collection.blit(self.item, position)

    def __init__(self, item, **star):
        self.item = item
        super().__init__(**star)
