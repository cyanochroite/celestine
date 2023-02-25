""" bpy.types.Image"""
from .spawn import _real


class _image(_real):
    """Image data-block referencing an external or packed image."""

    @classmethod
    def new(
        cls,
        name,
        width,
        height,
        alpha,
        float_buffer,
        stereo3d,
        is_data,
        tiled,
    ):
        return super().new(
            cls.data,
            name,
            width,
            height,
            alpha,
            float_buffer,
            stereo3d,
            is_data,
            tiled,
        )

    @classmethod
    def load(cls, filepath, check_existing=False):
        return cls.data.load(filepath, check_existing=check_existing)
