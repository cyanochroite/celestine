from .widget import Widget

import pygame


class Image(Widget):
    def __init__(self, window, image, rectangle):
        super().__init__(
            window,
            pygame.image.load(image),
            rectangle,
        )
