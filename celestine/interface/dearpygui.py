""""""

from celestine.interface import Abstract as Abstract_
from celestine.interface import Button as Button_
from celestine.interface import Image as Image_
from celestine.interface import Label as Label_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.typed import (
    LF,
    A,
    H,
    N,
    P,
    R,
    override,
)
from celestine.window.collection import Plane


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

    @override
    def make(self, canvas: A) -> N:
        """"""
        super().make(canvas)

        dearpygui = self.hold.package.dearpygui

        dearpygui.add_button(
            callback=self.callback,
            label=self.data,
            tag=self.name,
            pos=self.area.origin.int,
        )


class Image(Abstract, Image_):
    """
    Manages image objects.

    delete_item(...)
    """

    @override
    def make(self, canvas: A) -> N:
        """
        Draw the image to screen.

        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """
        super().make(canvas)

        dearpygui = self.hold.package.dearpygui

        photo = self.load()
        width, height = self.area.size

        with dearpygui.texture_registry(show=False):
            dearpygui.add_dynamic_texture(
                default_value=photo,
                height=height,
                tag=self.name,
                width=width,
            )

        dearpygui.add_image(
            self.name,
            tag=f"{self.name}-base",
            pos=self.area.origin.int,
        )

    def load(self) -> LF:
        """"""
        dearpygui = self.hold.package.dearpygui
        itertools = self.hold.package.itertools
        pillow = self.hold.package.pillow

        photo: LF = []

        if pillow:
            image = pillow.open(self.path)
            image.resize(self.area.size)
            data = image.getdata()
            flat = itertools.flatten(data)
            photo = list(map(lambda pixel: float(pixel / 255), flat))
        else:
            image = dearpygui.load_image(self.path)
            # width = image[0]
            # height = image[1]
            # channels = image[2]
            photo = image[3]
            # Unable to figure out how to avoid crashing application.
            # So just paint a boring blue image instead.
            width, height = self.area.size
            length = width * height
            for _ in range(length):
                photo.append(0)
                photo.append(0.25)
                photo.append(0.5)
                photo.append(1)
        return photo

    @override
    def update(self, path: P, **star: R) -> N:
        """"""
        super().update(path, **star)

        dearpygui = self.hold.package.dearpygui
        photo: list[float] = self.load()

        dearpygui.set_value(self.name, photo)


class Label(Abstract, Label_):
    """"""

    @override
    def make(self, canvas: A) -> N:
        """"""
        super().make(canvas)

        dearpygui = self.hold.package.dearpygui

        dearpygui.add_text(
            f" {self.data}",  # extra space hack to fix margin error
            tag=self.name,
            pos=self.area.origin.int,
        )


class View(View_):
    """"""

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        try:
            self.hold.package.dearpygui.hide_item(self.name)
        except SystemError:
            pass

    @override
    def show(self) -> N:
        """"""
        super().show()
        try:
            self.hold.package.dearpygui.show_item(self.name)
        except SystemError:
            pass


class Window(Window_):
    """"""

    @override
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

    @override
    def make(self, canvas: A) -> N:
        """"""
        dearpygui = self.hold.package.dearpygui
        for name, item in self:
            canvas = self.hold.package.dearpygui.window(tag=name)
            item.canvas = canvas
            with item.canvas:
                dearpygui.configure_item(item.name, show=False)
                item.make(None)

    @override
    def turn(self, page):
        """"""
        super().turn(page)
        dearpygui = self.hold.package.dearpygui
        tag = self.page.name
        dearpygui.set_primary_window(tag, True)

    @override
    def __enter__(self):
        super().__enter__()

        dearpygui = self.hold.package.dearpygui

        title = self.hold.language.APPLICATION_TITLE
        dearpygui.create_context()
        width, height = self.area.size.int
        dearpygui.create_viewport(
            title=title,
            small_icon="celestine_small.ico",
            large_icon="celestine_large.ico",
            width=width,
            height=height,
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

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        dearpygui = self.hold.package.dearpygui

        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
        return False

    @override
    def __init__(self, hold: H, **star: R) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
            "view": View,
            "window": self,
        }
        super().__init__(hold, element, **star)
        self.area = Plane.make(1920, 1080)
        self.tag = "window"
