import bpy

from .camera import _camera as camera
from .image import _image as image
from .light import _light as light
from .material import _material as material
from .mesh import _mesh as mesh
from .object import _object as object_
from .texture import _texture as texture


def register():
    """
    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    camera.data = bpy.data.cameras
    image.data = bpy.data.images
    light.data = bpy.data.lights
    material.data = bpy.data.materials
    mesh.data = bpy.data.meshes
    object_.data = bpy.data.objects
    texture.data = bpy.data.textures


def unregister():
    """
    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
