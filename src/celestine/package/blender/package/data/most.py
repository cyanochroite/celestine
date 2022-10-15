# <pep8-80 compliant>
# <pep8-80 compliant>
import bpy

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
