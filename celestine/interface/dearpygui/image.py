""""""

from celestine.window.image import Image as image

from .element import Element

from . import package


class Image(image, Element):
    """"""

    def draw(self, collection, **star):
        """"""
        _image = package.load_image(self.image) or (0, 0, 0, [])
        width = _image[0]
        height = _image[1]
        # channels = _image[2]
        photo = _image[3]
        name = self.image

        with package.texture_registry(show=False):
            package.add_static_texture(
                width=width, height=height, default_value=photo, tag=name
            )
        package.add_image(name, tag=self.tag)
        super().draw(collection, **star)
