from math import radians

from .element import Element
from .package import data
from .package import mesh as _mesh
from .package.data import mesh as make_mesh


class Mouse(Element):
    def __init__(self):
        self.text = "mouse"
        super().__init__()

    def draw(self, collection):
        plane = _mesh.plane(self.text)
        self.mesh = make_mesh.bind(collection, self.text, plane)
        super().draw(collection)
        self.mesh.location = (0, 0, -1)
        self.mesh.rotation_euler = (0, 0, radians(45))
        self.mesh.scale = (0.5, 0.5, 0.5)
