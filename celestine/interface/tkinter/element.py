""""""

from celestine import load
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_

from . import package


class Abstract(Abstract_):
    """"""

    def render(self, view, item, **star):
        """"""
        self.item = item(view, **star)

        width = self.x_max - self.x_min
        height = self.y_max - self.y_min
        self.item.place(
            x=self.x_min,
            y=self.y_min,
            width=width,
            height=height,
        )


class Button(Abstract, Button_):
    """"""

    def callback(self):
        """"""
        self.call(self.action, **self.argument)

    def draw(self, view, *, make, **star):
        """"""

        if not make:
            return

        item = package.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.text}")
        self.render(view, item, **star)


class Image(Abstract, Image_):
    """"""

    def draw(self, view, *, make, **star):
        """"""
        file = self.image or load.asset("null.png")

        if not make:
            return

        item = package.Label
        self.cache = package.PhotoImage(file=file)
        star.update(image=self.cache)
        self.render(view, item, **star)

    def update(self, *, image, **star):
        """"""
        if not super().update(image=image, **star):
            return False

        self.cache = package.PhotoImage(file=self.image)
        self.item.configure(image=self.cache)
        self.item.image = self.cache
        return True


class Label(Abstract, Label_):
    """"""

    def draw(self, view, *, make, **star):
        """"""
        if not make:
            return

        item = package.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.text}")
        star.update(width=100)
        self.render(view, item, **star)
