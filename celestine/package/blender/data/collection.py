"""Blender type is bpy.types.Collection."""
import bpy

from .spawn import _imaginary


class _collection(_imaginary):
    """Collection of Object data-blocks."""

    @property
    def children(self):
        return bpy.context.collection[self.name].children

    @property
    def objects(self):
        return self.soul.objects


    def __init__(self, name):
        super().__init__(name)
        bpy.context.scene.collection.children.link(self.soul)

        self.soul.hide_select = True

