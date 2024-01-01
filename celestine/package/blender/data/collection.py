"""Blender type is bpy.types.Collection."""
import bpy

from .spawn import _imaginary


class _collection(_imaginary):
    """Collection of Object data-blocks."""

    def __init__(self, name):
        soul = self.new(name)
        bpy.context.scene.collection.children.link(soul)

        self.objects = soul.objects
        self.soul = soul
        self.soul.hide_select = True
