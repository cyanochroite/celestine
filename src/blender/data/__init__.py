# <pep8-80 compliant>
# <pep8-80 compliant>
import bpy

from blender.data.light import _light as light
from blender.data.texture import _texture as texture


class all_stuff():
    @classmethod
    def new(cls, *args):
        return cls.data.new(*args)

    @classmethod
    def object_(cls, name, object_data):
        object = bpy.data.objects.new(name, object_data)
        bpy.context.scene.collection.objects.link(object)
        return object

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )

    @classmethod
    def make(cls, name):
        return cls.object_(name, cls.new(name))


class most(all_stuff):
    """Light data-block for lighting a scene."""
    type_ = None

    @classmethod
    def new(cls, name):
        return super().new(name, cls.type_)


class object(all_stuff):
    pass

class camera(all_stuff):
    """Camera data-block for storing camera settings."""
    #data = bpy.data.cameras


class material(all_stuff):
    """
    Material data-block to define the appearance of geometric objects for
    rendering.
    """
    #data = bpy.data.materials


class mesh(all_stuff):
    """Mesh data-block defining geometric surfaces."""
    #data = bpy.data.meshes

    @classmethod
    def make(cls, name, mesh=None):
        if not mesh:
            mesh = cls.new(name)
        return cls.object_(name, mesh)


class image(all_stuff):
    """Image data-block referencing an external or packed image."""
    #data = bpy.data.images

    @classmethod
    def new(cls, name, width, height, alpha, float_buffer, stereo3d, is_data,
            tiled):
        return super().new(
            cls.data,
            name,
            width,
            height,
            alpha,
            float_buffer,
            stereo3d,
            is_data,
            tiled,
        )

    @classmethod
    def load(cls, filepath, check_existing=False):
        return cls.data.load(filepath, check_existing=False)


def register():
    """
    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    object.data = bpy.data.objects
    camera.data = bpy.data.cameras
    material.data = bpy.data.materials
    mesh.data = bpy.data.meshes
    image.data = bpy.data.images
    light.data = bpy.data.lights
    texture.data = bpy.data.textures


def unregister():
    """
    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
