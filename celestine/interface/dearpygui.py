""""""

from celestine import load
from celestine.package import dearpygui
from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label
from celestine.window.window import Window as window


class Abstract(abstract):
    """"""


class Button(Abstract, button):
    """"""

    def callback(self, *_):
        """
        The object callback.

        callback(self, sender, app_data, user_data)
        """
        self.call(self.action, **self.argument)

    def draw(self, _, *, make, **star):
        """"""
        if not make:
            return

        dearpygui.add_button(
            callback=self.callback,
            label=self.data,
            tag=self.tag,
            pos=(self.x_min, self.y_min),
        )


class Image(Abstract, image):
    """
    Manages image objects.

    delete_item(...)
    """

    def add(self):
        """"""

        empty = (0, 0, 0, [])
        path = self.image or load.path.asset("null.png")

        _image = dearpygui.load_image(path) or empty
        width = _image[0]
        height = _image[1]
        # channels = _image[2]
        photo = _image[3]
        name = path

        with dearpygui.dataure_registry(show=False):
            try:
                dearpygui.add_dynamic_texture(
                    default_value=photo,
                    height=height,
                    tag=name,
                    width=width,
                )
            except SystemError:
                """Image already exists."""

        return name

    def draw(self, _, *, make, **star):
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

        name = self.add()

        dearpygui.add_image(
            name,
            tag=self.tag,
            pos=(self.x_min, self.y_min),
        )

    def update(self, *, image, **star):
        """"""
        if not super().update(image=image, **star):
            return False

        dearpygui.set_value(self.tag, self.image)
        return True


class Label(Abstract, label):
    """"""

    def draw(self, _, *, make, **star):
        """"""
        if not make:
            return

        dearpygui.add_text(
            f" {self.data}",  # extra space hack to fix margin error
            tag=self.tag,
            pos=(self.x_min, self.y_min),
        )


class Window(window):
    """"""

    def view(self, name, document):
        value = self.container.drop(name)
        value.data = dearpygui.window(tag=value.tag)
        self._view.set(name, value)
        with value.data:
            dearpygui.configure_item(value.tag, show=False)
            document(value)
            value.spot(0, 0, 1920, 1080)
            value.draw(None, make=True)

    def draw(self, **star):
        """"""

    def turn(self, page, **star):
        if self.page:
            dearpygui.hide_item(self.page.tag)

        super().turn(page, **star)

        tag = self.page.tag
        dearpygui.show_item(tag)
        dearpygui.set_primary_window(tag, True)

    def __enter__(self):
        super().__enter__()
        title = self.session.language.APPLICATION_TITLE
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
        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
        self.container = None
        return False

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.tag = "window"


def image_format():
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


def window(session, **star):
    """"""
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
    }
    size = (1280, 1080)
    return Window(session, element, size, **star)
