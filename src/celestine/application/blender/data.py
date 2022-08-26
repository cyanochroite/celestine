# <pep8-80 compliant>
import bpy  # pylint: disable=import-error
# blend data


class all():
    data = None

    @classmethod
    def new(cls, *args):
        return cls.data.new(*args)

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )

    @classmethod
    def tag(cls, value):
        # no idea what this does
        return cls.data.tag(value)

    @classmethod
    def unregister(cls):
        cls.data = None


class camera(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.cameras


class image(all):  # incomplete
    @classmethod
    def new(cls, name, width, height, alpha=False, float_buffer=False,
            stereo3d=False, is_data=False, tiled=False):
        pass

    @classmethod
    def load(cls, filepath, check_existing=False):
        return cls.data.load(filepath, check_existing=False)

    @classmethod
    def register(cls):
        cls.data = bpy.data.images


class light(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.lights


class material(all):
    @classmethod
    def create_gpencil_data(material):
        pass

    @classmethod
    def remove_gpencil_data(material):
        pass

    @classmethod
    def register(cls):
        cls.data = bpy.data.materials


class mesh(all):
    @classmethod
    def new_from_object(object, preserve_all_data_layers=False, depsgraph=None):
        pass

    @classmethod
    def register(cls):
        cls.data = bpy.data.meshes


class object(all):
    @classmethod
    def new(cls, name, object_data):
        object = super().new(name, object_data)
        bpy.context.scene.collection.objects.link(object)
        return object

    @classmethod
    def register(cls):
        cls.data = bpy.data.objects


class texture(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.textures


def register():
    camera.register()
    image.register()
    light.register()
    material.register()
    mesh.register()
    object.register()
    texture.register()


def unregister():
    camera.unregister()
    image.unregister()
    light.unregister()
    material.unregister()
    mesh.unregister()
    object.unregister()
    texture.unregister()
