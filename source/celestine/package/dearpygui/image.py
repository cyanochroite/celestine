from . import package
from .widget import Widget


class Image(Widget):
    def __init__(self, tag, file):
        image = package.load_image(file) or (0, 0, 0, [])
        self.width = image[0]
        self.height = image[1]
        self.channels = image[2]
        self.image = image[3]
        self.name = file

        with package.texture_registry(show=False):
            package.add_static_texture(
                width=self.width,
                height=self.height,
                default_value=self.image,
                tag=self.name
            )

        package.add_image(self.name, tag=tag)
