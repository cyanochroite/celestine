""""""

import enum

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    pygame,
)
from celestine.typed import (
    LS,
    A,
    D,
    N,
    P,
    R,
    S,
    ignore,
    override,
)
from celestine.window.collection import (
    Plane,
    Point,
)


class Mouse(enum.IntEnum):
    """Values returned by mouse click."""

    PRIMARY = 1
    MIDDLE = 2
    SECONDARY = 3
    SCROLL_UP = 4
    SCROLL_DOWN = 5
    TERTIARY = 6
    QUATERNARY = 7


class Abstract(Abstract_):
    """"""


class Element(Element_, Abstract):
    """"""

    image: pygame.Surface
    text_item: pygame.Surface
    font: pygame.font.Font

    @override
    def draw_foreground(self) -> N:
        """"""
        data = self.area.origin.data
        one = data[0].one
        two = data[1].one
        dest = (one, two)

        def render(source: A) -> N:
            """"""
            if source:

                self.parent.blit(source, dest)

        render(self.image)
        render(self.text_item)

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)
        self.color = (255, 0, 255)
        default = pygame.font.Font(None, 12)
        self.font = star.get("font", default)

        data = self.area.size.data
        one = data[0].one
        two = data[1].one
        size = (one, two)
        self.image = pygame.Surface(size)

    @override
    def reimage(self, path: P, **star: R) -> N:
        """"""
        # reset image
        self.image.fill((0, 0, 0))

        if bool(PIL):
            image = PIL.Image.open(
                fp=path,
                mode=LATIN_SMALL_LETTER_R,
                formats=bank.window.formats(),
            )
            buffer = image.tobytes()
            size = image.size
            format_ = image.mode
            surface = pygame.image.frombuffer(buffer, size, format_)
        else:
            surface = pygame.image.load(self.path)

        width = surface.get_width()
        height = surface.get_height()

        # TODO got to figure out Plane coordinates
        # or cache this somehow
        image_size = self.image_size((width, height))

        size = image_size.size.data
        source = pygame.transform.smoothscale(surface, size)

        dest = image_size.origin.data
        self.image.blit(source, dest)

        super().reimage(path, **star)

    @override
    def retext(self, text: S, **star: R) -> N:
        """"""
        self.text = text
        antialias = True
        color = self.color
        self.text_item = self.font.render(text, antialias, color)
        super().retext(text, **star)

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.color = (0, 0, 0)
        self.font = pygame.font.Font()
        self.text_item = pygame.Surface((0, 0))


class Window(Window_, Abstract):
    """"""

    area: Plane
    font: pygame.font.Font
    item: pygame.Surface
    star: R

    @override
    @classmethod
    def make(cls, *data: A, **star: R) -> Object:
        """"""
        return Element(*data, **star)

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)
        data = self.area.size.data
        one = data[0].one
        two = data[1].one
        size = (one, two)
        self.item = pygame.display.set_mode(size)
        star |= {"font": self.font}

    @override
    def draw_background(self) -> N:
        """"""
        self.item.fill((0, 0, 0))

    @override
    def draw_foreground(self) -> N:
        """"""
        ignore(self)
        pygame.display.flip()

    @override
    @classmethod
    def extension(cls) -> LS:
        ignore(cls)
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

    @override
    @classmethod
    def formats(cls) -> LS:
        ignore(cls)
        return [
            "BMP",
            "DIB",
            "GIF",
            "JPEG",
            "PCX",
            "PNG",
            "PPM",
            "TGA",
            "TIFF",
            "TGA",
            "WEBP",
            "XPM",
        ]

    @override
    def run(self) -> N:
        super().run()
        while True:
            bank.dequeue()
            self.draw(self)
            event = pygame.event.wait()
            match event.type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == Mouse.PRIMARY:
                        mouse_pos = pygame.mouse.get_pos()
                        point = Point.create(*mouse_pos)
                        self.clicker(self, point)
                case _:
                    pass
        pygame.quit()

    @override
    def __init__(self) -> N:
        super().__init__()
        self.area = Plane.create(1920, 1080)

        caption = bank.language.APPLICATION_TITLE
        pygame.display.set_caption(caption)

        pygame.font.init()
        size = 64
        self.font = pygame.font.Font(None, size)


ignore(Window)
