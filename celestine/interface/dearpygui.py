""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    dearpygui,
)
from celestine.typed import (
    LF,
    LS,
    VS,
    N,
    P,
    R,
    S,
    ignore,
    override,
)
from celestine.window.collection import Area


class Abstract(Abstract_):
    """"""

    @override
    def hide(self) -> N:
        """"""
        ignore(self)
        super().hide()
        dearpygui.hide_item(self.name)

    @override
    def show(self) -> N:
        """"""
        ignore(self)
        super().show()
        dearpygui.show_item(self.name)


class Element(Element_, Abstract):
    """
    Manages image objects.

    delete_item(...)
    """

    def callback(self, *_) -> N:
        """
        The object callback.

        callback(self, sender, app_data, user_data)
        """
        ignore(_)
        self.click(self.area.world.centroid)
        bank.dequeue()

    @override
    def build(self, parent: S, **star: R) -> N:
        """
        Draw the image to screen.

        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """
        ignore(star)
        super().build(parent)

        if self.action or self.goto:
            dearpygui.add_button(
                callback=self.callback,
                label=self.text,
                tag=self.name,
                parent=parent,
                pos=self.area.world.origin.value,
            )
            return

        if self.text:
            dearpygui.add_text(
                f" {self.text}",  # extra space hack to fix margin error
                tag=self.name,
                parent=parent,
                pos=self.area.world.origin.value,
            )
            return

        # image
        photo = self.load()
        width, height = self.area.local.size

        with dearpygui.texture_registry(show=False):
            dearpygui.add_dynamic_texture(
                default_value=photo,
                height=height,
                parent=parent,
                tag=self.name,
                width=width,
            )

        dearpygui.add_image(
            self.name,
            tag=f"{self.name}-base",
            parent=parent,
            pos=self.area.local.origin,
        )

    def load(self) -> LF:
        """"""

        itertools = None

        photo: LF = []

        if PIL and itertools:
            image = PIL.Image.open(
                fp=self.path,
                mode=LATIN_SMALL_LETTER_R,
                formats=bank.window.formats(),
            )
            image.resize(self.area.local.size)
            data = image.getdata()
            flat = itertools.flatten(data)
            photo = list(map(lambda pixel: float(pixel / 255), flat))
        else:
            image = dearpygui.load_image(self.path)
            photo = image[3]
            # Unable to figure out how to avoid crashing application.
            # So just paint a boring blue image instead.
            width, height = self.area.local.size
            length = width * height
            for _ in range(length):
                ignore(_)
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
    def build(self, parent: VS, **star: R) -> N:
        """"""
        ignore(star)
        self.canvas = dearpygui.add_group(parent=parent, tag=self.name)
        super().build(self.name)


class Window(Window_):
    """"""

    @override
    @classmethod
    def extension(cls) -> LS:
        """"""
        ignore(cls)
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
    def build(self, **star: R) -> N:
        """"""
        ignore(star)
        self.canvas = dearpygui.add_window(tag=self.name)
        dearpygui.set_primary_window(self.name, True)
        super().build()

    @override
    def run(self) -> N:
        ignore(self)
        super().run()
        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.fast(1280, 1080)
        self.tag = "window"

        self.canvas = None

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


ignore(Window)
