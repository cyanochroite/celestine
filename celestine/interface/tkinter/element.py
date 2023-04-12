""""""

from celestine import load
from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label

from . import package


class Abstract(abstract):
    """"""

    def render(self, view, item, **star):
        """"""
        pack = item(view, **star)
        width = self.x_max - self.x_min
        height = self.y_max - self.y_min
        pack.place(
            x=self.x_min,
            y=self.y_min,
            width=width,
            height=height,
        )
        self.item2 = pack


class Button(Abstract, button):
    """"""

    def callback(self):
        """"""
        self.call(self.action, **self.argument)

    def draw(self, view, *, make, **star):
        """"""
        if make:
            item = package.Button
            star.update(command=self.callback)
            star.update(text=f"button:{self.text}")
            self.render(view, item, **star)


class Image(Abstract, image):
    """"""

    def draw(self, view, *, make, **star):
        """"""
        if make:
            path = self.image or load.asset("null.png")
            self.item = package.PhotoImage(file=path)
            item = package.Label
            star.update(image=self.item)
            self.render(view, item, **star)
        else:
            self.item2.configure(image=self.item)
            self.item2.image = self.item


class Label(Abstract, label):
    """"""

    def draw(self, view, *, make, **star):
        """"""
        if make:
            item = package.Label
            star.update(fg="blue")
            star.update(height=4)
            star.update(text=f"label:{self.text}")
            star.update(width=100)
            self.render(view, item, **star)
