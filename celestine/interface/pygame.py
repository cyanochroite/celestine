""""""

from celestine import load
from celestine.typed import (
    L,
    N,
    R,
    S,
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

    def render(self, collection, item, **star):
        """"""
        position = (self.area.axis_x.minimum, self.area.axis_y.minimum)
        collection.blit(item, position)


class Button(Abstract, Button_):
    """"""

    def draw(self, ring: R, view, *, font, **star):
        """"""
        text = f"Button{self.data}"

        item = font.render(text, True, (255, 255, 255))
        self.render(view, item, **star)


class Label(Abstract, Label_):
    """"""

    def draw(self, ring: R, view, *, font, **star):
        """"""
        item = font.render(self.data, True, (255, 255, 255))
        self.render(view, item, **star)


class Image(Abstract, Image_):
    """"""

    def draw(self, ring: R, view, *, mode="hi", **star):
        """"""
        pillow = ring.package.pillow
        pygame = ring.package.pygame

        # do we call parent or some other function to get this right?
        # maybe call super, which does nothing but set name
        size = self.area.size

        if mode == "one":
            pass

        if pillow:
            image = pillow.image_load(self.path)
            size = self.resize(image.size)
            image.resize(size)
            image = pygame.image.fromstring(
                image.image.tobytes(),
                image.image.size,
                image.image.mode,
            )
        else:
            image = pygame.image.load(self.path)
            image = image.convert_alpha()
            size = self.resize((image.get_width(), image.get_height()))
            image = pygame.transform.scale(image, size)

        self.render(view, image, **star)


class Window(Window_):
    """"""

    def data(self, container):
        """"""
        container.data = self.book

    def draw(self, **star):
        """"""
        pygame = self.ring.package.pygame

        self.book.fill((0, 0, 0))

        super().draw(font=self.font, **star)

        pygame.display.flip()

    def extension(self) -> L[S]:
        return [
            ".bmp",
            ".sgi",
            ".rgb",
            ".bw",
            ".png",
            ".jpg",
            ".jpeg",
            ".jp2",
            ".j2c",
            ".tga",
            ".cin",
            ".dpx",
            ".exr",
            ".hdr",
            ".tif",
            ".tiff",
            ".webp",
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    def __enter__(self):
        pygame = self.ring.package.pygame

        def set_caption():
            caption = self.ring.language.APPLICATION_TITLE
            pygame.display.set_caption(caption)

        def set_font():
            pygame.font.init()
            file_path = load.pathway.asset("cascadia_code_regular.otf")
            size = 40
            self.font = pygame.font.Font(file_path, size)

        def set_icon():
            path = "icon.png"
            asset = load.pathway.asset(path)
            image = pygame.image.load(asset)
            icon = image.convert_alpha()
            pygame.display.set_icon(icon)

        def set_mode():
            size = self.container.area.size
            self.book = pygame.display.set_mode(size)

        super().__enter__()
        set_mode()
        set_icon()
        set_caption()
        set_font()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

        pygame = self.ring.package.pygame

        while True:
            event = pygame.event.wait()
            match event.type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    # TODO: This triggers on all mouse buttons
                    # including scroll wheel! That is bad.
                    (x_dot, y_dot) = pygame.mouse.get_pos()
                    self.page.poke(x_dot, y_dot)

        pygame.quit()
        return False

    def __init__(self, ring: R, **star) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
        }
        area = Area(Axis(0, 1280), Axis(0, 960))
        super().__init__(ring, element, area, **star)
        self.book = None
        self.font = None
