""""""

import pygame

from celestine.window.image import Image as image

from .element import Element


class Image(Element, image):
    """"""

    def __init__(self, file, **star):
        super().__init__(pygame.image.load(file), **star)
