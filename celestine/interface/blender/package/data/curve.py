""" bpy.types.Curve"""
from .spawn import _text


class _curve(_text):
    """Curve data-block storing curves, splines and NURBS."""

    font = None


class _font(_curve):
    """Vector font for Text objects."""

    type_ = "FONT"


setattr(_curve, "font", _font)
