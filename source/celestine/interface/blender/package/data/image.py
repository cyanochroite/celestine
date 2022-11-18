""" bpy.types.Image"""
from celestine.package.blender.package.data.spawn import _imaginary


class _image(_imaginary):
    """Image data-block referencing an external or packed image."""

    @classmethod
    def new(cls, name, width, height, alpha, float_buffer, stereo3d, is_data,
            tiled):
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
