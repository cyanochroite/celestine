""""""

import pygame

from .element import Element


class Image(Element):
    """"""

    def __init__(self, image, **star):
        super().__init__(pygame.image.load(image), **star)
