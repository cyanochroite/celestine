""""""


from celestine.window.collection import Object

from . import package


class Element(Object):
    """"""

    def draw(self, collection, **star):
        """"""
        self.item = self.item(collection, **star)
        self.item.pack(side=package.LEFT)

    def poke(self, x_dot, y_dot):
        """"""
        return False

