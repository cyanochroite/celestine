""""""

from celestine.window.element import Element as element


class Element(element):
    """"""

    def center_float(self):
        """"""
        x_dot = (self.x_min + self.x_max) / 2
        y_dot = (self.y_min + self.y_max) / 2
        return (x_dot, y_dot)

    def draw(self, collection):
        """"""
        (x_dot, y_dot) = self.center_float()
        # child sets mesh and then calls this
        self.mesh.location = (x_dot, y_dot, 0)
        self.mesh.rotation = (180, 0, 0)
