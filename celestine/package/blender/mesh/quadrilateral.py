""""""
import mathutils

from celestine.package.blender import data

from . import make


def quadrilateral(mesh, verts, layers):
    """"""
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    ]

    faces = [
        (0, 1, 2, 3),
    ]

    make(mesh, verts, edges, faces, layers)


class Planar:
    """"""

    def __init__(self):
        super().__init__()
        self.normal = mathutils.Vector((+0, +0, +1))

    def vertex_new(self, vector, normal):
        """"""
        vector = mathutils.Vector(vector)
        vector.resize_3d()
        rotation = self.normal.rotation_difference(normal)
        vector.rotate(rotation)
        return vector


class Plane(Planar):
    """"""

    def make(self, mesh, normal=(+0, +0, +1), uv_x=0, uv_y=0):
        """"""
        normal = mathutils.Vector(normal)

        verts = [
            self.vertex_new((+1, +1), normal),
            self.vertex_new((-1, +1), normal),
            self.vertex_new((-1, -1), normal),
            self.vertex_new((+1, -1), normal),
        ]

        layers = [
            (0, 0, 1 + uv_x, 1 + uv_y),
            (0, 1, 0 - uv_x, 1 + uv_y),
            (0, 2, 0 - uv_x, 0 - uv_y),
            (0, 3, 1 + uv_x, 0 - uv_y),
        ]

        quadrilateral(mesh, verts, layers)


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

        quadrilateral(mesh, verts, layers)


def plane(collection, name, uv_x=0, uv_y=0):
    """"""
    box = Plane()
    mesh = data.mesh.make(collection, name)
    box.make(mesh.soul, (+0, +0, +1), uv_x, uv_y)
    return mesh
