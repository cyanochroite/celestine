""""""

import enum

from celestine import (
    bank,
    load,
)
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    pygame,
)
from celestine.typed import (
    ANY,
    LS,
    B,
    D,
    N,
    P,
    R,
    S,
    ignore,
    override,
)
from celestine.window.collection import (
    Area,
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
    def draw(self, **star: R) -> B:
        """"""
        if not super().draw(**star):
            return False

        dest = self.area.world.origin.value

        def render(source: ANY) -> N:
            """"""
            if source:
                self.parent.blit(source, dest)

        render(self.image)
        render(self.text_item)

        return True

    @override
    def build(self, parent: ANY, star: D[S, ANY]) -> N:
        """"""
        super().build(parent, star)
        self.color = (255, 0, 255)
        # self.warp("font")
        self.font = star.get("font", None)

        size = self.area.local.size.value
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

        # TODO got to figure out Area coordinates
        # or cache this somehow
        image_size = self.image_size((width, height))

        size = image_size.size.value
        source = pygame.transform.smoothscale(surface, size)

        dest = image_size.origin.value
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


class View(View_, Abstract):
    """"""


class Window(Window_, Abstract):
    """"""

    area: Area
    font: pygame.font.Font
    item: pygame.Surface
    star: R

    @override
    def build(self, parent: ANY, star: D[S, ANY]) -> N:
        """"""
        super().build(parent, star)
        self.item = pygame.display.set_mode(self.area.world.size.value)
        star |= {"font": self.font}

    @override
    def draw(self, **star: R) -> B:
        """"""
        self.item.fill((0, 0, 0))

        super().draw(font=self.font, **star)

        pygame.display.flip()

        return True

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

        def set_icon() -> N:
            path = "icon.png"
            asset = load.asset(path)
            image = pygame.image.load(asset)
            icon = image.convert_alpha()
            pygame.display.set_icon(icon)

        set_icon()

        while True:
            bank.dequeue()
            event = pygame.event.wait()
            match event.type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == Mouse.PRIMARY:
                        self.click(Point(*pygame.mouse.get_pos()))
                case _:
                    pass

        pygame.quit()

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.fast(1920, 1080)

        caption = bank.language.APPLICATION_TITLE
        pygame.display.set_caption(caption)

        pygame.font.init()
        file_path = load.asset("cascadia_code_regular.otf")
        size = 40
        self.font = pygame.font.Font(file_path, size)


ignore(Window)
