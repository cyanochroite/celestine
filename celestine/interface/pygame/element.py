""""""

from celestine.window.element import Element as element


class Element(element):
    """"""

    def draw(self, collection, **star):
        """"""
        position = (self.x_min, self.y_min)
        collection.blit(self.item, position)
