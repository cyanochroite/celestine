"""bpy.types.Texture"""
from .spawn import _imaginary


class _texture(_imaginary):
    """Light data-block for lighting a scene."""


class _none(_texture):
    """None."""
    type_ = "NONE"


class _blend(_texture):
    """Blend – Procedural - create a ramp texture."""
    type_ = "BLEND"


class _clouds(_texture):
    """
    Clouds – Procedural - create a cloud-like fractal noise texture.
    """
    type_ = "CLOUDS"


class _distorted(_texture):
    """
    Distorted Noise – Procedural - noise texture distorted by two noise
    algorithms.
    """
    type_ = "DISTORTED_NOISE"


class _image(_texture):
    """
    Image or Movie – Allow for images or movies to be used as textures.
    """
    type_ = "IMAGE"


class _magic(_texture):
    """
    Magic – Procedural - color texture based on trigonometric functions.
    """
    type_ = "MAGIC"


class _marble(_texture):
    """
    Marble – Procedural - marble-like noise texture with wave generated
    bands.
    """
    type_ = "MARBLE"


class _musgrave(_texture):
    """Musgrave – Procedural - highly flexible fractal noise texture."""
    type_ = "MUSGRAVE"


class _noise(_texture):
    """
    Noise – Procedural - random noise, gives a different result every
    time, for every frame, for every pixel.
    """
    type_ = "NOISE"


class _stucci(_texture):
    """Stucci – Procedural - create a fractal noise texture."""
    type_ = "STUCCI"


class _voronoi(_texture):
    """
    Voronoi – Procedural - create cell-like patterns based on Worley
    noise.
    """
    type_ = "VORONOI"


class _wood(_texture):
    """
    Wood – Procedural - wave generated bands or rings, with optional
    noise.
    """
    type_ = "WOOD"


setattr(_texture, "none", _none)
setattr(_texture, "blend", _blend)
setattr(_texture, "clouds", _clouds)
setattr(_texture, "distorted_noise", _distorted)
setattr(_texture, "image", _image)
setattr(_texture, "magic", _magic)
setattr(_texture, "marble", _marble)
setattr(_texture, "musgrave", _musgrave)
setattr(_texture, "noise", _noise)
setattr(_texture, "stucci", _stucci)
setattr(_texture, "voronoi", _voronoi)
setattr(_texture, "wood", _wood)
