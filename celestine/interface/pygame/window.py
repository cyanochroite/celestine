""""""

from celestine import load
from celestine.package import pygame
from celestine.window.window import Window as window


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
