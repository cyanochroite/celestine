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
        pack = item(collection, **star)
        width = self.x_max - self.x_min
        height = self.y_max - self.y_min
        pack.place(
            x=self.x_min,
            y=self.y_min,
            width=width,
            height=height,
        )


class Button(Abstract, button):
    """"""

    def callback(self):
        """"""
        self.call(self.action, **self.argument)

    def draw(self, collection, **star):
        """"""
        item = package.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.text}")
        self.render(collection, item, **star)


class Image(Abstract, image):
    """"""

    def draw(self, collection, **star):
        """"""
        path = self.image or load.asset("null.png")
        self.item = package.PhotoImage(file=path)

        item = package.Label
        star.update(image=self.item)
        self.render(collection, item, **star)


class Label(Abstract, label):
    """"""

    def draw(self, collection, **star):
        """"""
        item = package.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.text}")
        star.update(width=100)
        self.render(collection, item, **star)
