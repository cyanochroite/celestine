""""""

from celestine.window.collection import Box


class Element(Box):
    def __init__(self, item, **star):
        self.item = item
        super().__init__(**star)

    def action(self):
        pass

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()

    def draw(self, collection):
        """"""
        position = (self.x_min, self.y_min)
        collection.blit(self.item, position)

    def poke(self, x_dot, y_dot):
        """"""
        return self.inside(x_dot, y_dot)
