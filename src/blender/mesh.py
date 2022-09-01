# <pep8-80 compliant>
import bmesh
import mathutils

from blender import data


class Mesh():
    """Create a mesh in Blender."""

    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def vertex_add(self, vector):
        """Add 'vertex' to the mesh."""
        coordinate = (vector.x, vector.y, vector.z)
        self.verts.new(coordinate)

    def vertex_finalize(self):
        """Call this after adding all 'vertex' to mesh."""
        self.verts.ensure_lookup_table()

    def edge_add(self, vertex_a, vertex_b,):
        """Add 'edge' to the mesh."""
        vert_a = self.verts[vertex_a]
        vert_b = self.verts[vertex_b]
        vertices = (vert_a, vert_b)
        self.edges.new(vertices)

    def edge_finalize(self):
        """Call this after adding all 'edge' to mesh."""
        self.edges.ensure_lookup_table()

    def face_add(self, vertex_a, vertex_b, vertex_c, vertex_d):
        """Add 'face' to the mesh."""
        vert_a = self.verts[vertex_a]
        vert_b = self.verts[vertex_b]
        vert_c = self.verts[vertex_c]
        vert_d = self.verts[vertex_d]
        vertices = (vert_a, vert_b, vert_c, vert_d)
        self.faces.new(vertices)

    def face_finalize(self):
        """Call this after adding all 'face' to mesh."""
        self.faces.ensure_lookup_table()

    def uv_add(self, face, loop, point):
        """Add 'uv' to the mesh."""
        index_uv = self.bmesh.loops.layers.uv.verify()
        self.faces[face].loops[loop][index_uv].uv = (point.x, point.y)

    def uv_finalize(self):
        """Call this after adding all 'uv' to mesh."""

    def finalize(self, name):
        """Call this after adding all the stuff to mesh."""
        mesh = data.mesh.new(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        return mesh


class Quadrilateral(Mesh):
    def vertex(self, zero, one, two, three):
        self.vertex_add(zero)
        self.vertex_add(one)
        self.vertex_add(two)
        self.vertex_add(three)
        self.vertex_finalize()

    def edge(self):
        self.edge_add(0, 1)
        self.edge_add(1, 2)
        self.edge_add(2, 3)
        self.edge_add(3, 0)
        self.edge_finalize()

    def face(self):
        self.face_add(0, 1, 2, 3)
        self.face_finalize()

    def uv(self, zero, one, two, three):
        self.uv_add(0, 0, zero)
        self.uv_add(0, 1, one)
        self.uv_add(0, 2, two)
        self.uv_add(0, 3, three)
        self.uv_finalize()


class Planar(Quadrilateral):
    def __init__(self):
        super().__init__()
        self.normal = mathutils.Vector((+0, +0, +1))

    def vertex_new(self, vector, normal):
        vector = mathutils.Vector(vector)
        vector.resize_3d()
        rotation = self.normal.rotation_difference(normal)
        vector.rotate(rotation)
        return vector


class Plane(Planar):
    def vertex(self, normal=(+1, +1, +1)):
        normal = mathutils.Vector(normal)

        vector_a = self.vertex_new((+1, +1), normal)
        vector_b = self.vertex_new((-1, +1), normal)
        vector_c = self.vertex_new((-1, -1), normal)
        vector_d = self.vertex_new((+1, -1), normal)

        super().vertex(vector_a, vector_b, vector_c, vector_d)

    def edge(self):
        self.edge_add(0, 1)
        self.edge_add(1, 2)
        self.edge_add(2, 3)
        self.edge_add(3, 0)
        self.edge_finalize()

    def face(self):
        self.face_add(0, 1, 2, 3)
        self.face_finalize()

    def uv(self, uv_x=0, uv_y=0):
        self.uv_add(0, 0, mathutils.Vector((1 + uv_x, 1 + uv_y)))
        self.uv_add(0, 1, mathutils.Vector((0 - uv_x, 1 + uv_y)))
        self.uv_add(0, 2, mathutils.Vector((0 - uv_x, 0 - uv_y)))
        self.uv_add(0, 3, mathutils.Vector((1 + uv_x, 0 - uv_y)))
        self.uv_finalize()


def plane(uv_x=0, uv_y=0):
    box = Plane()
    box.vertex()
    box.edge()
    box.face()
    box.uv(uv_x, uv_y)
    name = "Plane"
    return box.finalize(name)


def _offset(numerator, denominator):
    ratio = numerator / denominator
    unit = 1
    maximum = max(ratio, unit)
    normalization = maximum - unit
    half = 1 / 2
    halving = normalization * half
    return halving
    #  return (max(numerator / denominator, 1) - 1) / 2


def image(image):
    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = _offset(y, x)
    x_to_y = _offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    return plane(x, y)
