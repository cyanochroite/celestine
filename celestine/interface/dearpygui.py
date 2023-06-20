""""""

from celestine import load
from celestine.typed import (
    N,
    R,
)
from celestine.window.collection import (
    Area,
    Axis,
)
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_
from celestine.window.window import Window as Window_


class Abstract(Abstract_):
    """"""


class Button(Abstract, Button_):
    """"""

    def callback(self, *_):
        """
        The object callback.

        callback(self, sender, app_data, user_data)
        """
        self.call(self.action, **self.argument)

    def draw(self, ring, _, *, make, **star):
        """"""
        if not make:
            return

        dearpygui = ring.package.dearpygui

        dearpygui.add_button(
            callback=self.callback,
            label=self.data,
            tag=self.name,
            pos=(self.area.axis_x.minimum, self.area.axis_y.minimum),
        )


class Image(Abstract, Image_):
    """
    Manages image objects.

    delete_item(...)
    """

    def draw(self, ring, _, *, make, **star):
        """
        Draw the image to screen.

        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """

        if not make:
            return

        dearpygui = ring.package.dearpygui

        image = dearpygui.load_image(str(self.path))
        width = image[0]
        height = image[1]
        # channels = image[2]
        photo = image[3]

        with dearpygui.texture_registry(show=False):
            try:
                dearpygui.add_dynamic_texture(
                    default_value=photo,
                    height=height,
                    tag=f"{self.name}-image",
                    width=width,
                )
            except SystemError:
                """Image already exists."""

        dearpygui.add_image(
            f"{self.name}-image",
            tag=self.name,
            pos=(self.area.axis_x.minimum, self.area.axis_y.minimum),
        )

    def update(self, ring: R, image, **star):
        """"""
        super().update(ring, image, **star)

        dearpygui = ring.package.dearpygui

        dearpygui.set_value(self.name, self.image)


class Label(Abstract, Label_):
    """"""

    def draw(self, ring, _, *, make, **star):
        """"""
        if not make:
            return

        dearpygui = ring.package.dearpygui

        dearpygui.add_text(
            f" {self.data}",  # extra space hack to fix margin error
            tag=self.name,
            pos=(self.area.axis_x.minimum, self.area.axis_y.minimum),
        )


class Window(Window_):
    """"""

    def extension(self):
        """"""
        return [
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".gif",
            ".hdr",
            ".pic",
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
        ]

    def view(self, name, document):
        dearpygui = self.ring.package.dearpygui

        value = self.container.drop(name)
        value.data = dearpygui.window(tag=value.name)
        self._view.set(name, value)
        with value.data:
            dearpygui.configure_item(value.name, show=False)
            document(self.ring, value)
            area = Area(Axis(0, 1920), Axis(0, 1080))
            value.spot(area)
            value.draw(self.ring, None, make=True)

    def draw(self, **star):
        """"""

    def turn(self, page, **star):
        dearpygui = self.ring.package.dearpygui

        if self.page:
            dearpygui.hide_item(self.page.name)

        super().turn(page, **star)

        tag = self.page.name
        dearpygui.show_item(tag)
        dearpygui.set_primary_window(tag, True)

    def __enter__(self):
        super().__enter__()

        dearpygui = self.ring.package.dearpygui

        title = self.ring.language.APPLICATION_TITLE
        dearpygui.create_context()
        dearpygui.create_viewport(
            title=title,
            small_icon="celestine_small.ico",
            large_icon="celestine_large.ico",
            width=1920,
            height=1080,
            x_pos=256,
            y_pos=256,
            min_width=640,
            max_width=3840,
            min_height=480,
            max_height=2160,
            resizable=True,
            vsync=True,
            always_on_top=False,
            decorated=True,
            clear_color=(0, 0, 0),
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        dearpygui = self.ring.package.dearpygui

        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
        self.container = None
        return False

    def __init__(self, ring: R, **star) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
        }
        area = Area(Axis(0, 1280), Axis(0, 1080))
        super().__init__(ring, element, area, **star)
        self.tag = "window"
