""" bpy.types.Collection"""
import bpy

from .spawn import _imaginary


class _collection(_imaginary):
    """Collection of Object data-blocks."""

    @classmethod
    def scene(cls):
        """"""
        return cls(bpy.context.scene.collection)

    @classmethod
    def make(cls, name):
        """"""
        soul = cls.new(name)
        bpy.context.scene.collection.children.link(soul)
        return cls(soul)

    def __init__(self, soul):
        self.objects = soul.objects
        self.soul = soul
        self.soul.hide_select = True

    def hide(self):
        """"""
        self.soul.hide_render = True
        self.soul.hide_viewport = True

    def show(self):
        """"""
        self.soul.hide_render = False
        self.soul.hide_viewport = False
