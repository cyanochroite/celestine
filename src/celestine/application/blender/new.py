# <pep8-80 compliant>
from . import data


def camera(name):
    return data.camera.new(name)


def image(name):
    print("!!FIX!!")
    # FIX
    return data.image.new(name, data.image)


class light(data.light):
    @classmethod
    def area(cls, name):
        return cls.new(name, 'AREA')

    @classmethod
    def point(cls, name):
        return cls.new(name, 'POINT')

    @classmethod
    def spot(cls, name):
        return cls.new(name, 'SPOT')

    @classmethod
    def sun(cls, name):
        return cls.new(name, 'SUN')


def material(name):
    return data.material.new(name)


def mesh(name):
    return data.mesh.new(name)


def object(name, object_data):
    return data.object.new(name, object_data)


class texture(data.texture):
    @classmethod
    def none(cls, name):
        return cls.new(name, 'NONE')

    @classmethod
    def blend(cls, name):
        return cls.new(name, 'BLEND')

    @classmethod
    def clouds(cls, name):
        return cls.new(name, 'CLOUDS')

    @classmethod
    def distorted_noise(cls, name):
        return cls.new(name, 'DISTORTED_NOISE')

    @classmethod
    def image(cls, name):
        return cls.new(name, 'IMAGE')

    @classmethod
    def magic(cls, name):
        return cls.new(name, 'MAGIC')

    @classmethod
    def marble(cls, name):
        return cls.new(name, 'MARBLE')

    @classmethod
    def musgrave(cls, name):
        return cls.new(name, 'MUSGRAVE')

    @classmethod
    def noise(cls, name):
        return cls.new(name, 'NOISE')

    @classmethod
    def stucci(cls, name):
        return cls.new(name, 'STUCCI')

    @classmethod
    def voronoi(cls, name):
        return cls.new(name, 'VORONOI')

    @classmethod
    def wood(cls, name):
        return cls.new(name, 'WOOD')
