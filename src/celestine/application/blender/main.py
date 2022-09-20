# <pep8-80 compliant>
"""Package celestine."""
import bpy  # pylint: disable=import-error
import bmesh  # pylint: disable=import-error

from celestine.application.blender import data
from celestine.application.blender import preferences
from celestine.application.blender import UV


def register():
    """
    This is a function which only runs when enabling the add-on, this means the
    module can be loaded without activating the add-on.
    """
    data.register()
    preferences.register()


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """
    preferences.unregister()
    data.unregister()

ready = False


def new_image(image):
    mesh = bmesh.new(use_operators=False)

    mesh.verts.new((+1, +1, +0))
    mesh.verts.new((-1, +1, +0))
    mesh.verts.new((-1, -1, +0))
    mesh.verts.new((+1, -1, +0))
    mesh.verts.ensure_lookup_table()

    mesh.edges.new((mesh.verts[0], mesh.verts[1]))
    mesh.edges.new((mesh.verts[1], mesh.verts[2]))
    mesh.edges.new((mesh.verts[2], mesh.verts[3]))
    mesh.edges.new((mesh.verts[3], mesh.verts[0]))
    mesh.edges.ensure_lookup_table()

    mesh.faces.new((
        mesh.verts[0],
        mesh.verts[1],
        mesh.verts[2],
        mesh.verts[3],
    ))
    mesh.faces.ensure_lookup_table()

    uv = mesh.loops.layers.uv.verify()  # ANOCE
    (x, y) = image.size
    (x, y) = ((max(y / x, 1) - 1) / 2, (max(x / y, 1) - 1) / 2)
    mesh.faces[0].loops[0][uv].uv = (1 + x, 1 + y)
    mesh.faces[0].loops[1][uv].uv = (0 - x, 1 + y)
    mesh.faces[0].loops[2][uv].uv = (0 - x, 0 - y)
    mesh.faces[0].loops[3][uv].uv = (1 + x, 0 - y)

    meshit = bpy.data.meshes.new("name")
    mesh.to_mesh(meshit)
    mesh.free()
    return meshit


class Image():
    """Holds an image."""

    def __init__(self, file):
        _image = data.image.load(file)
        self.height = _image.size[1]
        self.image = _image
        self.width = _image.size[0]
        self.name = file


def file_dialog(tag, bind):
    """pass"""
    pass


def file_dialog_load(tag):
    """pass"""
    pass


spot = 0


def _new_object(image):
    global spot
    mush = new_image(image)
    box = data.mesh.make("image", mush)
    box.location = (spot, 0, 0)
    spot += 2.5
    return box


def image(tag, _image):
    """pass"""
    image = _image.image
    material = UV.material("pretty", image)
    object = _new_object(image)
    object.data.materials.append(material)


def image_load(file):
    """pass"""
    print("convert " + file)
    return Image(file)


def label(tag, text):
    """pass"""
    pass


def _startup_clear():
    # this probably highly unoptimized.
    # try doing this backwarks
    for camera in bpy.data.cameras:
        data.camera.remove(camera)
    for light in bpy.data.lights:
        data.light.remove(light)
    for material in bpy.data.materials:
        data.material.remove(material)
    for mesh in bpy.data.meshes:
        data.mesh.remove(mesh)
    for image in bpy.data.images:
        data.image.remove(image)
    for texture in bpy.data.textures:
        data.texture.remove(texture)

    #light = make.light.sun("light")
    light = data.light.sun.make("light")
    light.location = (0, 0, 1)
    camera = data.camera.make("camera")
    camera.location = (0, 0, 10)


def main(session):
    """def main"""
    global item
    item = {}

    global spot
    spot = 0

    register()

    _startup_clear()
    session.window.setup(session)
    session.window.view(session)

    unregister()