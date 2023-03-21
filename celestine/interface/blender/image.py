""""""

from celestine.window.image import Image as image

from .element import Element
from .package import (
    UV,
    data,
)
from .package import mesh as _mesh
from .package.data import mesh as make_mesh


class Image(image, Element):
    """"""

    def draw(self, collection):
        _image = data.image.load(self.image)
        material = UV.material("pretty", _image)
        plane = _mesh.image(_image)
        mesh = make_mesh.bind(collection, self.image, plane)
        mesh.body.data.materials.append(material)
        self.item = mesh
        super().draw(collection)
