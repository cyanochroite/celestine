""""""

from celestine.window.image import Image as image

from .element import Element


class Image(image, Element):
    """"""

    def draw(self, collection):
        image = data.image.load(self.name)
        material = UV.material("pretty", image)
        plane = _mesh.image(image)
        mesh = make_mesh.bind(collection, self.name, plane)
        mesh.body.data.materials.append(material)
        self.mesh = mesh
        super().draw(collection)

    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)
