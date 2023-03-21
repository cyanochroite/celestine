""""""


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
        pack.pack(side=package.LEFT)


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
        self.item = package.PhotoImage(file=self.image)

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
