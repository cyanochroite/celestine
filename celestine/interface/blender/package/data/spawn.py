# <pep8-80 compliant>
# <pep8-80 compliant>
import bpy


class _imaginary():
    type_ = ""
    data = None

    @classmethod
    def new(cls, name):
        if cls.type_:
            return cls.data.new(name, cls.type_)
        return cls.data.new(name)

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )


class _real(_imaginary):
    @classmethod
    def make(cls, name, item=None):
        fake = item or cls.new(name)
        real = cls.object_(name, fake)
        return _real(real, fake)

    @classmethod
    def object_(cls, name, object_data):
        object_ = bpy.data.objects.new(name, object_data)
        bpy.context.scene.collection.objects.link(object_)
        return object_

    def __init__(self, real, fake):
        self.__dict__["real"] = real
        self.__dict__["fake"] = fake
        self.__dict__["data"] = ["location", "rotation_euler", "scale"]

    def __getattr__(self, name):
        if name in self.__dict__["data"]:
            return getattr(self.__dict__["real"], name)
        return getattr(self.__dict__["fake"], name)

    def __setattr__(self, name, value):
        if name in self.__dict__["data"]:
            setattr(self.real, name, value)
        else:
            setattr(self.fake, name, value)
