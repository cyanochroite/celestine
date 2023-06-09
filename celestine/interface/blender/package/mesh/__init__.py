""""""
# <pep8-80 compliant>
import bmesh as bmesh_
import mathutils


def make(mesh, verts, edges, faces, layers):
    """"""
    bmesh = bmesh_.new(use_operators=False)

    for vert in verts:
        bmesh.verts.new(vert)
    bmesh.verts.ensure_lookup_table()

    for one, two in edges:
        bmesh.edges.new((bmesh.verts[one], bmesh.verts[two]))
    bmesh.edges.ensure_lookup_table()

    for face in faces:
        bmesh.faces.new(map(lambda vert: bmesh.verts[vert], face))
    bmesh.faces.ensure_lookup_table()

    layer = bmesh.loops.layers.uv.verify()
    for face, loop, one, two in layers:
        bmesh.faces[face].loops[loop][layer].uv = (one, two)

    bmesh.to_mesh(mesh)
    bmesh.free()


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


def plane(mesh, name, uv_x=0, uv_y=0):
    """"""
    box = Plane()
    box.make(mesh, (+0, +0, +1), uv_x, uv_y)
    return mesh


def text(collection, name, text):
    """"""
    from . import data
    font_curve = data.curve.font.make(collection, name, text)
    return font_curve


def _offset(numerator, denominator):
    """"""
    ratio = numerator / denominator
    unit = 1
    maximum = max(ratio, unit)
    normalization = maximum - unit
    half = 1 / 2
    halving = normalization * half
    return halving
    #  return (max(numerator / denominator, 1) - 1) / 2


def image(image):
    """"""
    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = _offset(y, x)
    x_to_y = _offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    return plane(image.name, x, y)
