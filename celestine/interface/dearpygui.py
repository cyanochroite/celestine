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
    ANY,
    LF,
    LS,
    D,
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
    def unbuild(self, parent: ANY, star: D[S, ANY]) -> N:
        """"""
        dpg.delete_item(self.name)

    @override
    def build(self, parent: ANY, star: D[S, ANY]) -> N:
        """
        Draw the image to screen.

        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """
        super().build(parent, star)

        width, height = self.area.local.size.value
        width = 200
        height = 200
        length = width * height

        texture_data = []
        for i in range(length):
            texture_data.append(0)
            texture_data.append(0.25)
            texture_data.append(0.5)
            texture_data.append(1)

        dearpygui.add_dynamic_texture(
            width,
            height,
            texture_data,
            parent="__demo_texture_container",
            tag=f"_{self.name}",
        )

        star.update(label=f" {self.text}")
        star.update(tag=self.name)
        star.update(parent=parent)
        star.update(pos=self.area.world.origin.value)

        if not self.text:
            star.update(texture_tag=f"_{self.name}")

        if self.action or self.goto:
            star.update(callback=self.callback)
            if self.text:
                self.item = dearpygui.add_button(**star)
            else:
                self.item = dearpygui.add_image_button(**star)
        else:
            if self.text:
                self.item = dearpygui.add_text(self.text, **star)
            else:
                self.item = dearpygui.add_image(**star)

    @override
    def reimage(self, path: P, **star: R) -> N:
        """"""
        if not path:
            # TODO: IMPORTANT! Change all others for check here.
            return

        texture_data = []
        if bool(PIL):
            pil_image = PIL.Image.open(
                fp=path,
                mode=LATIN_SMALL_LETTER_R,
                formats=bank.window.formats(),
            )
            pil_image = pil_image.convert("RGBA")
            image_size = self.image_size(pil_image.size)
            # pil_image = pil_image.resize(image_size.size.value)
            pil_image = pil_image.resize((200, 200))
            for pixel in pil_image.getdata():
                for colour in pixel:
                    texture_data.append(colour / 255)
        else:
            return

        dearpygui.set_value(f"_{self.name}", texture_data)
        super().reimage(path, **star)

    @override
    def retext(self, text: S, **star: R) -> N:
        """"""
        super().retext(text, **star)

    @override
    def update(self, path: P, **star: R) -> N:
        """"""
        super().update(path, **star)

        photo: list[float] = self.load()

        dearpygui.set_value(self.name, photo)


class View(View_, Abstract):
    """"""

    @override
    def build(self, parent: ANY, star: D[S, ANY]) -> N:
        """"""
        super().build(parent, star)
        self.item = dearpygui.add_group(parent=parent, tag=self.name)


class Window(Window_, Abstract):
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
    def build(self, parent: ANY, star: D[S, ANY]) -> N:
        """"""
        super().build(parent, star)
        self.item = dearpygui.add_window(tag=self.name)
        dearpygui.set_primary_window(self.name, True)

        dearpygui.add_texture_registry(
            label="Demo Texture Container", tag="__demo_texture_container"
        )

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

        self.parent = None

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
