""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import (
    Object,
    Plane,
    Point,
)
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    dearpygui,
)
from celestine.typed import (
    LF,
    LS,
    A,
    D,
    N,
    P,
    R,
    S,
    cast,
    ignore,
    override,
)


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

    def callback(self, *_: A) -> N:
        """
        The object callback.

        callback(self, sender, app_data, user_data)
        """
        ignore(_)
        self.click(self.area.centroid)
        bank.dequeue()

    def unbuild(self, parent: A, star: D[S, A]) -> N:
        """"""
        ignore(parent, star)
        dearpygui.delete_item(self.name)

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """
        Draw the image to screen.

        image = (0, 0, 0, [])
        width = image[0]
        height = image[1]
        channels = image[2]
        photo = image[3]
        """
        super().build(parent, star)

        texture_data: LF = []
        for _ in range(self.area.z_len * 0):  # TODO skip
            texture_data.append(0)
            texture_data.append(0.25)
            texture_data.append(0.5)
            texture_data.append(1)

        dearpygui.add_dynamic_texture(
            self.area.x_len,
            self.area.y_len,
            texture_data,
            parent="__demo_texture_container",
            tag=f"_{self.name}",
        )

        star.update(label=f" {self.text}")
        star.update(tag=self.name)
        star.update(parent=parent.name)
        star.update(pos=self.area.centroid)

        # if not self.text:
        #    star.update(texture_tag=f"_{self.name}")

        if self.action or self.goto:
            star.update(callback=self.callback)
            if self.text:
                self.item = dearpygui.add_button(**star)
            else:
                self.item = dearpygui.add_image_button(**star)
        elif self.text or self.path:
            if self.text:
                self.item = dearpygui.add_text(self.text, **star)
            if self.path:
                self.item = dearpygui.add_image(**star)
        else:
            self.item = dearpygui.add_group(
                parent=parent.name, tag=self.name
            )

    def reimage(self, path: P, **star: R) -> N:
        """"""
        if not path:
            # TODO: IMPORTANT! Change all others for check here.
            return

        if not bool(PIL):
            return

        texture_data: LF = []

        image = PIL.Image.open(
            fp=path,
            mode=LATIN_SMALL_LETTER_R,
            formats=bank.window.formats(),
        )
        image = image.convert(mode="RGBA")
        image_size = self.image_size(image.size)
        image = image.resize(image_size.size.data)

        target = Plane.create(*self.area.size)
        image = self.imagin(image, image_size, target.size, "RGBA")

        for pixel in image.getdata():
            pixie = cast(LF, pixel)
            for colour in pixie:
                # TODO: This returns a TZ4
                texture_data.append(colour / 255)

        dearpygui.set_value(f"_{self.name}", texture_data)
        super().reimage(path, **star)


class Window(Window_, Abstract):
    """"""

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)
        dearpygui.add_window(tag=self.name)
        dearpygui.set_primary_window(self.name, True)

        dearpygui.add_texture_registry(
            label="Demo Texture Container",
            tag="__demo_texture_container",
        )

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
    @classmethod
    def make(cls, *data: A, **star: R) -> Object:
        """"""
        ignore(cls)
        result = Element(*data, **star)
        return result

    @override
    def run(self) -> N:
        dearpygui.create_context()
        dearpygui.create_viewport(
            title=bank.language.APPLICATION_TITLE,
            small_icon="celestine_small.ico",
            large_icon="celestine_large.ico",
            width=self.area.x_len,
            height=self.area.y_len,
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
            disable_close=False,
        )
        super().run()
        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()

    @override
    def __init__(self) -> N:
        super().__init__()
        self.area = Plane.make(1280, 1080)
        self.tag = "window"
        self.parent = None


ignore(
    Window,
)
