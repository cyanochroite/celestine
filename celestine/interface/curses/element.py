""""""

from celestine import load

from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label


class Abstract(abstract):
    """"""

    def add_string(self, frame, x_dot, y_dot, text):
        """curses swaps x and y"""
        frame.addstr(y_dot, x_dot, text)

    def origin(self):
        """"""
        x_dot = int(self.x_min)
        y_dot = int(self.y_min)
        return (x_dot, y_dot)

    def render(self, collection, item, **star):
        """"""
        text = item
        (x_dot, y_dot) = self.origin()
        self.add_string(collection, x_dot, y_dot, text)


class Button(Abstract, button):
    """"""

    def draw(self, collection, **star):
        """"""
        item = f"button:{self.text}"
        self.render(collection, item, **star)


class Image(Abstract, image):
    """"""

    def draw(self, collection, **star):
        """"""
        path = self.image or load.asset("null.png")
        item = f"image:{path}"
        self.render(collection, item, **star)


class Label(Abstract, label):
    """"""

    def draw(self, collection, **star):
        """"""
        item = f"label:{self.text}"
        self.render(collection, item, **star)
