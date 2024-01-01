"""Blender type is bpy.types.Collection."""

from .spawn import _imaginary


class _collection(_imaginary):
    """Collection of Object data-blocks."""

    def __getattr__(self, name):
        return getattr(self.soul, name)

    def __init__(self, name):
        super().__init__(name)
        self.soul.hide_select = True

