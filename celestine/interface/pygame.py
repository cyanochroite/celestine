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
    BF,
    LS,
    A,
    B,
    K,
    M,
    N,
    P,
    R,
    S,
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

    image: M
    text_item: A
    image_item: A

    @override
    def draw(self, **star: R) -> B:
        """"""
        if not super().draw(**star):
            return False

        self.render(self.image_item)
        self.render(self.text_item)

        return True

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        super().make(canvas, **star)
        self.font = star.pop("font")

        if self.text:
            self.update_text(self.text)

        if self.path:
            self.update_image(self.path)

    def render(self, source: A) -> N:
        """"""
        if not source:
            return
        point = self.area.world.origin + self.offset
        dest = point.value
        area = None
        special_flags = 0
        self.canvas.blit(source, dest, area, special_flags)

    def update_image(self, path: P, **star: R) -> N:
        """"""
        self.path = path

        if pillow:
            image = pillow.open(self.path)
            width = image.image.width
            height = image.image.height
        else:
            image = pygame.image.load(self.path)
            width = image.get_width()
            height = image.get_height()

        curent = Plane.make(width, height)
        target = Plane.make(*self.area.world.size.value)

        match self.fit:
            case Image.FILL:
                result = curent.scale_to_min(target)
            case Image.FULL:
                result = curent.scale_to_max(target)

        result.center(target)
        self.offset = result.origin

        if pillow:
            image.resize(result.size)
            bytes_ = image.image.tobytes()
            size = image.image.size
            format_ = image.image.mode
            flipped = False
            self.image_item = pygame.image.fromstring(
                bytes_,
                size,
                format_,
                flipped,
            )
        else:
            cow = result.size
            image = pygame.transform.smoothscale(
                image,
                result.size.value,
            )
            self.image_item = image

    def update_text(self, text: S) -> N:
        """"""
        self.text = text
        antialias = True
        color = self.color
        background = None
        self.text_item = self.font.render(
            text,
            antialias,
            color,
            background,
        )

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.path = star.pop("path", "")
        self.color = (255, 0, 255)
        self.offset = Point(0, 0)
        self.font = None

        self.image_item = None
        self.text_item = None


class View(View_, Abstract):
    """"""


class Window(Window_):
    """"""

    @override
    def draw(self, **star: R) -> N:
        """"""
        self.canvas.fill((0, 0, 0))

        super().draw(font=self.font, **star)

        pygame.display.flip()

    @override
    def extension(self) -> LS:
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
    def make(self, **star: R) -> N:
        """"""
        super().make(font=self.font, **star)

    @override
    def __enter__(self) -> K:
        super().__enter__()

        def set_caption() -> N:
            caption = bank.language.APPLICATION_TITLE
            pygame.display.set_caption(caption)

        def set_font() -> N:
            pygame.font.init()
            file_path = load.asset("cascadia_code_regular.otf")
            size = 40
            self.font = pygame.font.Font(file_path, size)

        set_caption()
        set_font()

        return self

    @override
    def __exit__(self, exc_type: A, exc_value: A, traceback: A) -> BF:
        super().__exit__(exc_type, exc_value, traceback)

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
        return False

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.make(1280, 960)
        self.area = Area.make(1920, 1080)
        self.font = None

        value = self.area.world.size.value
        self.canvas = pygame.display.set_mode(value)
