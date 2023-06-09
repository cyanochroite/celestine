""""""
from math import radians

from celestine.typed import N

from .element import Abstract
from .package import data
from .package import mesh as _mesh
from .package.data import mesh as make_mesh
from .package.data.collection import _collection

COLLECTION = _collection


class Mouse(Abstract):
    """"""

    def __init__(self) -> N:
        self.text = "mouse"
        super().__init__("mouse")

    def draw(self, view: COLLECTION) -> N:
        """"""
        plane = _mesh.plane(self.text)
        self.item = make_mesh.bind(view, self.text, plane)

        self.render()

        mesh = data.mesh.make(view, self.text)
        mesh.location = (0, 0, -1)
        mesh.rotation_euler = (0, 0, radians(45))
        mesh.scale = (0.5, 0.5, 0.5)
        self.item = mesh


class Diamond(Planar):
    """"""

    def make(self, mesh):
        """"""
        normal = mathutils.Vector((+0, +0, +1))

        verts = [
            self.vertex_new((+1, +0), normal),
            self.vertex_new((-0, +1), normal),
            self.vertex_new((-1, -0), normal),
            self.vertex_new((+0, -1), normal),
        ]

        layers = [
            (0, 0, 1, 1),
            (0, 1, 0, 1),
            (0, 2, 0, 0),
            (0, 3, 1, 0),
        ]

        mesh = data.mesh.make(collection, "mouse")
        quadrilateral(mesh, verts, layers)
