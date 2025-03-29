""""""

import bmesh as bpy_bmesh


def make(mesh, verts, edges, faces, layers):
    """"""
    bmesh = bpy_bmesh.new(use_operators=False)

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
