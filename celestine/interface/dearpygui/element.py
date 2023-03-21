""""""


from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label

from . import package


class Abstract(abstract):
    """"""


class Button(Abstract, button):
    """"""

    def callback(self, *_):
        """callback(self, sender, app_data, user_data)"""
        self.call(self.action, **self.argument)

    def draw(self, _, **star):
        """"""
        package.add_button(
            callback=self.callback,
            label=self.text,
            tag=self.tag,
        )


class Image(Abstract, image):
    """"""

    def draw(self, _, **star):
        """
        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """
        empty = (0, 0, 0, [])
        _image = package.load_image(self.image) or empty
        width = _image[0]
        height = _image[1]
        # channels = _image[2]
        photo = _image[3]
        name = self.image

        with package.texture_registry(show=False):
            package.add_static_texture(
                default_value=photo,
                height=height,
                tag=name,
                width=width,
            )
        package.add_image(
            name,
            tag=self.tag,
        )


class Label(Abstract, label):
    """"""

    def draw(self, _, **star):
        """"""
        package.add_text(
            self.text,
            label=f"{self.tag}{label}",
            show_label=True,
            tag=self.tag,
        )
