""""""

from celestine.window.element import Element as element


class Element(element):
    """"""

    def draw(self, collection):
        """"""
        (x_dot, y_dot) = self.center_float()
        # child sets mesh and then calls this
        self.mesh.location = (x_dot, y_dot, 0)
        self.mesh.rotation = (180, 0, 0)
