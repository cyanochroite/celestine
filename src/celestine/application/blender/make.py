# <pep8-80 compliant>
from . import new


def camera(name):
    return new.object(name, new.camera(name))


class image():  # incomplete
    @classmethod
    def register(cls):
        cls.data = bpy.data.images

    @staticmethod
    def new(name, width, height):
        return bpy.data.images.new(name, width, height)

    @staticmethod
    def load(name, width, height):
        return bpy.data.images.load(filepath, check_existing)
#    return bpy.data.images.load(filepath, check_existing=check_existing)


class light():
    @staticmethod
    def area(name):
        return new.object(name, new.light.area(name))

    @staticmethod
    def point(name):
        return new.object(name, new.light.point(name))

    @staticmethod
    def spot(name):
        return new.object(name, new.light.spot(name))

    @staticmethod
    def sun(name):
        return new.object(name, new.light.sun(name))


def mesh(name, mesh=None):
    if not mesh:
        mesh = new.mesh(name)
    return new.object(name, mesh)
