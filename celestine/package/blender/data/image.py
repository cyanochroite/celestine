"""Blender type is bpy.types.Image."""
from .spawn import _real


class _image(_real):
    """Image data-block referencing an external or packed image."""

    # @classmethod
    # def make(
    #    cls,
    #    name,
    #    width,
    #    height,
    #    alpha=False,
    #    float_buffer=False,
    #    stereo3d=False,
    #    is_data=False,
    #    tiled=False,
    # ):
    # raise NotImplementedError("When do we use this?")
    # image = bpy.types.BlendDataImages(bpy_struct)
    # return image.new(
    #    cls.data,
    #    name,
    #    width,
    #    height,
    #    alpha=alpha,
    #    float_buffer=float_buffer,
    #    stereo3d=stereo3d,
    #    is_data=is_data,
    #    tiled=tiled,
    # )

    @classmethod
    def load(cls, path):
        """"""
        filepath = str(path)
        check_existing = True
        return cls.data.load(filepath, check_existing=check_existing)
