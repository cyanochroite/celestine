""""""

from celestine import load
from celestine.package import pygame
from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label
from celestine.window.window import Window as window


class Abstract(abstract):
    """"""

    def render(self, collection, item, **star):
        """"""
        position = (self.x_min, self.y_min)
        collection.blit(item, position)


class Button(Abstract, button):
    """"""

    def draw(self, view, *, font, **star):
        """"""
        text = f"Button{self.text}"

        item = font.render(text, True, (255, 255, 255))
        self.render(view, item, **star)


class Image(Abstract, image):
    """"""

    def draw(self, view, **star):
        """"""
        path = self.image or load.asset("null.png")
        item = pygame.image.load(path)
        item = item.convert_alpha()
        self.render(view, item, **star)


class Label(Abstract, label):
    """"""

    def draw(self, view, *, font, **star):
        """"""
        item = font.render(self.text, True, (255, 255, 255))
        self.render(view, item, **star)


class Window(window):
    """"""

    def data(self, container):
        """"""
        container.data = self.book

    def draw(self, **star):
        """"""
        self.book.fill((0, 0, 0))

        super().draw(font=self.font, **star)

        pygame.display.flip()

    def __enter__(self):
        def set_caption():
            caption = self.session.language.APPLICATION_TITLE
            pygame.display.set_caption(caption)

        def set_font():
            pygame.font.init()
            file_path = load.asset("CascadiaCode.ttf")
            size = 40
            self.font = pygame.font.Font(file_path, size)

        def set_icon():
            path = "icon.png"
            asset = load.asset(path)
            image = pygame.image.load(asset)
            icon = image.convert_alpha()
            pygame.display.set_icon(icon)

        def set_mode():
            size = (self.width, self.height)
            self.book = pygame.display.set_mode(size)

        super().__enter__()
        set_mode()
        set_icon()
        set_caption()
        set_font()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            event = pygame.event.wait()
            match event.type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    (x_dot, y_dot) = pygame.mouse.get_pos()
                    self.page.poke(x_dot, y_dot)

        pygame.quit()
        return False

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.book = None
        self.font = None


def image_format():
    """"""
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


def window(session, **star):
    """"""
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
    }
    size = (1280, 960)
    return Window(session, element, size, **star)
