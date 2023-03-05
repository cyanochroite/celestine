""""""
# <pep8-80 compliant>
import math

import bpy

DEGREE_TO_RADIAN = math.pi / 180


class _imaginary:
    """Objects that only exist in spirit."""

    type_ = ""
    data = None

    @classmethod
    def new(cls, name):
        """"""
        if cls.type_:
            return cls.data.new(name, cls.type_)
        return cls.data.new(name)

    @classmethod
    def remove(cls, item):
        """"""
        cls.data.remove(
            item, do_unlink=True, do_id_user=True, do_ui_user=True
        )


class _real(_imaginary):
    """Objects that exist in the real world."""

    @classmethod
    def bind(cls, collection, name, soul):
        """Give an existing soul a body."""
        body = bpy.data.objects.new(name, soul)
        collection.objects.link(body)
        return cls(body, soul)

    @classmethod
    def make(cls, collection, name):
        """Create a new soul and give it a body."""
        soul = cls.new(name)
        return cls.bind(collection, name, soul)

    def __init__(self, body, soul):
        self.__dict__["body"] = body
        self.__dict__["soul"] = soul

    def __getattr__(self, name):
        match name:
            case "location":
                getattr(self.body, name)
            case "parent":
                getattr(self.body, name)
            case "rotation_euler":
                getattr(self.body, name)
            case "scale":
                getattr(self.body, name)
            case _:
                getattr(self.soul, name)

    def __setattr__(self, name, value):
        match name:
            case "location":
                setattr(self.body, name, value)
            case "rotation":
                (x_dot, y_dot, z_dot) = value
                x_dot *= DEGREE_TO_RADIAN
                y_dot *= DEGREE_TO_RADIAN
                z_dot *= DEGREE_TO_RADIAN
                value = (x_dot, y_dot, z_dot)
                setattr(self.body, "rotation_euler", value)
            case "parent":
                setattr(self.body, name, value.body)
            case "rotation_euler":
                setattr(self.body, name, value)
            case "scale":
                setattr(self.body, name, value)
            case _:
                setattr(self.soul, name, value)


class _text(_real):
    @classmethod
    def new(cls, name, text):
        soul = super().new(name)
        soul.body = text
        return soul

    @classmethod
    def make(cls, collection, name, text):
        """Create a new soul and give it a body."""
        soul = cls.new(name, text)
        return cls.bind(collection, name, soul)
