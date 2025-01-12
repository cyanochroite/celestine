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
from celestine.package import (
    pillow,
    pygame,
)
from celestine.typed import (
    LS,
    A,
    B,
    K,
    N,
    P,
    R,
    S,
    ignore,
    override,
)
from celestine.window.collection import (
    Area,
    Plane,
    Point,
)
from celestine.window.container import Image


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

        def render(source: A) -> N:
            """"""
            if source:
                self.canvas.blit(source, dest)

        render(self.image)
        render(self.text_item)

        return True

    @override
    def build(self, canvas: A, **star: R) -> N:
        """"""
        super().build(canvas, **star)

        self.color = (255, 0, 255)
        # self.warp("font")
        self.font = star.pop("font")

        size = self.area.local.size.value
        self.image = pygame.Surface(size)

        if self.path:
            self.update_image(self.path)

        if self.text:
            self.update_text(self.text)

    def update_image(self, path: P, **star: R) -> N:
        """"""
        self.path = path

        # reset image
        self.image.fill((0, 0, 0))

        if bool(pillow):
            image = pillow.Image.open(self.path)
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
        target = self.area.local
        target = Plane.create(*self.area.world.size.value)
        curent = Plane.create(width, height)

        if self.fit == Image.FILL:
            curent.scale_to_min(target)
        elif self.fit == Image.FULL:
            curent.scale_to_max(target)
        curent.center(target)

        size = curent.size.value
        source = pygame.transform.smoothscale(surface, size)

        dest = curent.origin.value
        self.image.blit(source, dest)

    def update_text(self, text: S) -> N:
        """"""
        self.text = text
        antialias = True
        color = self.color
        self.text_item = self.font.render(text, antialias, color)

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.color = (0, 0, 0)
        self.font = pygame.font.Font()
        self.text_item = pygame.Surface((0, 0))


class View(View_, Abstract):
    """"""


class Window(Window_):
    """"""

    area: Area
    canvas: pygame.Surface
    font: pygame.font.Font

    @override
    def build(self, **star: R) -> N:
        """"""
        super().build(font=self.font, **star)

    @override
    def draw(self, **star: R) -> N:
        """"""
        self.canvas.fill((0, 0, 0))

        super().draw(font=self.font, **star)

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

        value = self.area.world.size.value
        self.canvas = pygame.display.set_mode(value)

        caption = bank.language.APPLICATION_TITLE
        pygame.display.set_caption(caption)

        pygame.font.init()
        file_path = load.asset("cascadia_code_regular.otf")
        size = 40
        self.font = pygame.font.Font(file_path, size)
