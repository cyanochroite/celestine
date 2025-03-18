"""Python Imaging Library (Fork)."""

from celestine.package import Abstract
from celestine.package.bpy import (
    context,
    props,
    types,
    utils,
)
from celestine.typed import ignore

ignore(context, props, types, utils)


class Package(Abstract):
    """"""
