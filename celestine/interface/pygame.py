""""""

from celestine import load
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.typed import (
    LS,
    A,
    B,
    H,
    K,
    N,
    R,
    S,
    override,
)
from celestine.window.collection import (
    Plane,
    Point,
)


class Element(Element_):
    """"""

    @override
    def make(self, canvas: A) -> N:
        """"""
        pillow = self.hold.package.pillow

        self.image = pillow.new(self.area.size.int)

        super().make(canvas)

    def draw(self, *, font, **star: R) -> B:
        """"""
        if not super().draw(**star):
            return False

        pygame = self.hold.package.pygame

        origin = (self.area.one.minimum, self.area.two.minimum)

        image = pygame.image.fromstring(
            self.image.image.tobytes(),
            self.image.image.size,
            self.image.image.mode,
        )
        self.canvas.blit(image, origin)

        text = font.render(self.text, True, (255, 0, 255))
        self.canvas.blit(text, origin)

    def __init__(self, hold: H, name: S, parent: K, **star: R) -> N:
        super().__init__(hold, name, parent, **star)
        self.path = star.get("path", "")


class View(View_):
    """"""


class Window(Window_):
    """"""

    @override
    def draw(self, **star: R) -> N:
        """"""
        pygame = self.hold.package.pygame

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
    def make(self) -> N:
        """"""
        pygame = self.hold.package.pygame

        self.canvas = pygame.display.set_mode(self.area.size.int)

        super().make()

    @override
    def __enter__(self):
        super().__enter__()

        pygame = self.hold.package.pygame

        def set_caption():
            caption = self.hold.language.APPLICATION_TITLE
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
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

        pygame = self.hold.package.pygame

        def set_icon():
            path = "icon.png"
            asset = load.asset(path)
            image = pygame.image.load(asset)
            icon = image.convert_alpha()
            pygame.display.set_icon(icon)

        set_icon()

        while True:
            self.hold.dequeue()
            event = pygame.event.wait()
            match event.type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    # TODO: This triggers on all mouse buttons
                    # including scroll wheel! That is bad.
                    self.click(Point(*pygame.mouse.get_pos()))

        pygame.quit()
        return False

    @override
    def __init__(self, hold: H, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(hold, element, **star)
        self.area = Plane.make(1280, 960)
        self.font = None
