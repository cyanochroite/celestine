""""""


from celestine.window.element import Element as element

from . import package


class Element(element):
    """"""

    def draw(self, collection, **star):
        """"""
        self.item = self.item(collection, **star)
        self.item.pack(side=package.LEFT)

    def poke(self, x_dot, y_dot):
        """"""
        return False
