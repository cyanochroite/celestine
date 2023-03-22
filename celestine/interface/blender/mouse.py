""""""
from math import radians

from .element import Abstract
from .package import mesh as _mesh
from .package.data import mesh as make_mesh


class Mouse(Abstract):
    """"""

    def __init__(self):
        self.text = "mouse"
        super().__init__("mouse")

    def draw(self, collection):
        """"""
        plane = _mesh.plane(self.text)
        self.item = make_mesh.bind(collection, self.text, plane)
        super().draw(collection)
        self.item.location = (0, 0, -1)
        self.item.rotation_euler = (0, 0, radians(45))
        self.item.scale = (0.5, 0.5, 0.5)
