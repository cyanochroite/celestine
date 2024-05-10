""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package import (
    dearpygui,
    pillow,
)
from celestine.typed import (
    LF,
    A,
    B,
    N,
    P,
    R,
    override,
)
from celestine.window.collection import Area


class Abstract(Abstract_):
    """"""


class Element(Element_, Abstract):
    """
    Manages image objects.

    delete_item(...)
    """

    def callback(self, *_):
        """
        The object callback.

        callback(self, sender, app_data, user_data)
        """
        self.click(self.area.world.centroid)
        bank.dequeue()

    @override
    def make(self, canvas: A) -> B:
        """
        Draw the image to screen.

        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """
        super().make(canvas)

        if self.action or self.goto:
            dearpygui.add_button(
                callback=self.callback,
                label=self.text,
                tag=self.name,
                pos=self.area.world.origin.value,
            )
            return True

        if self.text:
            dearpygui.add_text(
                f" {self.text}",  # extra space hack to fix margin error
                tag=self.name,
                pos=self.area.world.origin.value,
            )
            return True

        # image
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

        return True

    def load(self) -> LF:
        """"""

        itertools = itertools

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

        photo: list[float] = self.load()

        dearpygui.set_value(self.name, photo)


class View(View_, Abstract):
    """"""

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        try:
            dearpygui.hide_item(self.name)
        except SystemError:
            pass

    @override
    def show(self) -> N:
        """"""
        super().show()
        try:
            dearpygui.show_item(self.name)
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
    def make(self, **star: R) -> N:
        """"""
        self.canvas = None

        for name, item in self:
            canvas = dearpygui.window(tag=name)
            item.canvas = canvas
            with item.canvas:
                dearpygui.configure_item(item.name, show=False)
                item.make(None)

    @override
    def turn(self, page):
        """"""
        super().turn(page)

        tag = self.page.name
        dearpygui.set_primary_window(tag, True)

    @override
    def __enter__(self):
        super().__enter__()

        title = bank.language.APPLICATION_TITLE
        dearpygui.create_context()
        width, height = self.area.world.size
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

        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
        return False

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.make(1280, 1080)
        self.tag = "window"
