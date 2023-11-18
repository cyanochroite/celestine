""""""

from celestine import load
from celestine.typed import (
    LS,
    H,
    N,
    R,
    override,
)
from celestine.window import Window as Window_
from celestine.window.collection import (
    Plane,
    Point,
)
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_


class Abstract(Abstract_):
    """"""

    def render(self, item):
        """"""
        origin = (self.area.one.minimum, self.area.two.minimum)
        self.canvas.blit(item, origin)


class Button(Abstract, Button_):
    """"""

    def draw(self, *, font, **star: R):
        """"""

        text = f"Button{self.data}"

        item = font.render(text, True, (255, 255, 255))
        self.render(item)


class Label(Abstract, Label_):
    """"""

    def draw(self, *, font, **star: R):
        """"""

        item = font.render(self.data, True, (255, 255, 255))
        self.render(item)


class Image(Abstract, Image_):
    """"""

    def draw(self, *, mode="hi", **star: R):
        """"""

        pillow = self.hold.package.pillow
        pygame = self.hold.package.pygame

        # do we call parent or some other function to get this right?
        # maybe call super, which does nothing but set name
        size = self.area.size

        if mode == "one":
            pass

        #  TODO explore how to resize
        # resize = self.scale_to_fit(self.area.size)

        if pillow:
            image = pillow.open(self.path)

            image.scale_to_fit(self.area.size)
            # image.scale_to_fill(self.area.size)

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

        self.render(image)


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
    def __enter__(self):
        pygame = self.hold.package.pygame

        def set_caption():
            caption = self.hold.language.APPLICATION_TITLE
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

        super().__enter__()
        set_icon()
        set_caption()
        set_font()
        return self

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

        pygame = self.hold.package.pygame

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
            "button": Button,
            "image": Image,
            "label": Label,
        }
        area = Plane.make(1280, 960)
        canvas = hold.package.pygame.display.set_mode(area.size.int)
        super().__init__(hold, canvas, element, **star)
        self.area = area
        self.font = None
