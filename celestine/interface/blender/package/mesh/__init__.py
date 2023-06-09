""""""
# <pep8-80 compliant>
import bmesh as bmesh_

from celestine.interface.blender.package import data


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


def text(collection, name, words):
    """"""
    font_curve = data.curve.font.make(collection, name, words)
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
