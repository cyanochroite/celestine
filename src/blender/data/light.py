# <pep8-80 compliant>
""" bpy.types.Light"""
import bpy  # pylint: disable=import-error

from blender.data.most import most


class _light(most):
    """Light data-block for lighting a scene."""
#    try:
#        data = bpy.data.lights
#    except AttributeError:
#        pass


class _area(_light):
    """Area – Directional area light source."""
    type_ = 'AREA'


class _point(_light):
    """Point – Omnidirectional point light source."""
    type_ = 'POINT'


class _spot(_light):
    """Spot – Directional cone light source."""
    type_ = 'SPOT'


class _sun(_light):
    """Sun – Constant direction parallel ray light source."""
    type_ = 'SUN'


_light.area = _area
_light.point = _point
_light.spot = _spot
_light.sun = _sun
