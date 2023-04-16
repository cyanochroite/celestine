""""""

from celestine import load
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

    def draw(self, _, *, make, **star):
        """"""
        if not make:
            return

        package.add_button(
            callback=self.callback,
            label=self.text,
            tag=self.tag,
            pos=(self.x_min, self.y_min),
        )


class Image(Abstract, image):
    """ "delete_item(...)"."""

    def add(self):
        """"""

        empty = (0, 0, 0, [])
        path = self.image or load.asset("null.png")

        _image = package.load_image(path) or empty
        width = _image[0]
        height = _image[1]
        # channels = _image[2]
        photo = _image[3]
        name = path

        with package.texture_registry(show=False):
            try:
                package.add_dynamic_texture(
                    default_value=photo,
                    height=height,
                    tag=name,
                    width=width,
                )
            except SystemError:
                """image already exists"""

        return name

    def draw(self, _, *, make, **star):
        """
        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """

        if not make:
            return

        name = self.add()

        package.add_image(
            name,
            tag=self.tag,
            pos=(self.x_min, self.y_min),
        )

    def update(self, *, image, **star):
        """"""
        if not super().update(image=image, **star):
            return False

        package.set_value(self.tag, self.image)
        return True


class Label(Abstract, label):
    """"""

    def draw(self, _, *, make, **star):
        """"""
        if not make:
            return

        package.add_text(
            f" {self.text}",  # extra space hack to fix margin error
            tag=self.tag,
            pos=(self.x_min, self.y_min),
        )
