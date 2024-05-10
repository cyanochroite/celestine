""""""

from celestine import (
    bank,
    load,
)
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package import pygame
from celestine.typed import (
    LS,
    A,
    B,
    K,
    M,
    N,
    R,
    S,
    override,
)
from celestine.window.collection import (
    Area,
    Point,
)


class Abstract(Abstract_):
    """"""


class Element(Element_, Abstract):
    """"""

    image: M

    def draw(self, **star: R) -> B:
        """"""
        font = star.pop("font")

        if not super().draw(**star):
            return False

        origin = self.area.world.origin.value

        image = pygame.image.fromstring(
            self.image.image.tobytes(),
            self.image.image.size,
            self.image.image.mode,
        )
        self.canvas.blit(image, origin)

        text = font.render(self.text, True, (255, 0, 255))
        self.canvas.blit(text, origin)
        return True

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.path = star.get("path", "")


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
        value = self.area.world.size.value
        self.canvas = pygame.display.set_mode(value)

        super().make()

    @override
    def __enter__(self):
        super().__enter__()

        def set_caption():
            caption = bank.language.APPLICATION_TITLE
            pygame.display.set_caption(caption)

        def set_font():
            pygame.font.init()
            file_path = load.asset("cascadia_code_regular.otf")
            size = 40
            self.font = pygame.font.Font(file_path, size)

        set_caption()
        set_font()

        return self

    @override
    def __exit__(self, exc_type: A, exc_value: A, traceback: A):
        super().__exit__(exc_type, exc_value, traceback)

        def set_icon():
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
                    # TODO: This triggers on all mouse buttons
                    # including scroll wheel! That is bad.
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
