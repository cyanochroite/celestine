""" bpy.types.Light"""
from .spawn import _real


class _light(_real):
    """Light data-block for lighting a scene."""

    area = None
    point = None
    spot = None
    sun = None


class _area(_light):
    """Area – Directional area light source."""

    type_ = "AREA"


class _point(_light):
    """Point – Omnidirectional point light source."""

    type_ = "POINT"


class _spot(_light):
    """Spot – Directional cone light source."""

    type_ = "SPOT"


class _sun(_light):
    """Sun – Constant direction parallel ray light source."""

    type_ = "SUN"


setattr(_light, "area", _area)
setattr(_light, "point", _point)
setattr(_light, "spot", _spot)
setattr(_light, "sun", _sun)
