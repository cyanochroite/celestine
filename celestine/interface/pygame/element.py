""""""

from celestine import load
from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label

from . import package


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
        item = package.image.load(path)
        item = item.convert_alpha()
        self.render(view, item, **star)


class Label(Abstract, label):
    """"""

    def draw(self, view, *, font, **star):
        """"""
        item = font.render(self.text, True, (255, 255, 255))
        self.render(view, item, **star)
