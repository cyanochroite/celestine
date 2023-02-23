""""""

import pygame

from celestine.window.image import Image as image

from .element import Element


class Image(image, Element):
    """"""

    def draw(self, frame, **star):
        """"""
        self.item = pygame.image.load(self.image)
        super().draw(frame, **star)
