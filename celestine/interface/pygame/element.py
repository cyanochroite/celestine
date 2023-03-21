""""""

import pygame

from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label


class Abstract(abstract):
    """"""

    def render(self, collection, item, **star):
        """"""
        position = (self.x_min, self.y_min)
        collection.blit(item, position)


class Button(Abstract, button):
    """"""

    def draw(self, collection, *, font, **star):
        """"""
        text = f"Button{self.text}"

        item = font.render(text, True, (255, 255, 255))
        self.render(collection, item, **star)


class Image(Abstract, image):
    """"""

    def draw(self, collection, **star):
        """"""
        item = pygame.image.load(self.image)
        self.render(collection, item, **star)


class Label(Abstract, label):
    """"""

    def draw(self, collection, *, font, **star):
        """"""
        item = font.render(self.text, True, (255, 255, 255))
        self.render(collection, item, **star)
