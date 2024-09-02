""""""

import math

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package import (
    pillow,
    tkinter,
)
from celestine.typed import (
    LS,
    A,
    K,
    N,
    P,
    R,
    S,
    override,
)
from celestine.window.collection import (
    Area,
    Plane,
    Point,
)
from celestine.window.container import Image


class Abstract(Abstract_):
    """"""

    def place(self, item: A) -> N:
        """"""
        width, height = self.area.local.size
        dot_x, dot_y = self.area.local.origin
        item.place(
            x=dot_x,
            y=dot_y,
            width=width,
            height=height,
        )


class Element(Element_, Abstract):
    """"""

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        self.item.place_forget()

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        super().make(canvas, **star)

        # TODO: self.area.local.size.value
        self.image = tkinter.PhotoImage(
            width=200,
            height=200,
        )

        def callback() -> N:
            """"""
            self.click(self.area.world.centroid)
            bank.dequeue()

        # Change everything to button and disable if no action?
        if self.action or self.goto:
            star.update(command=callback)
            self.item = tkinter.Button(canvas, **star)
        else:
            self.item = tkinter.Label(canvas, **star)
        self.place(self.item)

        if self.path:
            self.update_image(self.path)

        if self.text:
            self.update_text(self.text)

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place(self.item)

    def update_image(self, path: P, **star: R) -> N:
        """"""
        self.path = path
        target = Plane.create(*self.area.world.size.value)

        # image = pillow.open(self.path)

        # curent = Plane.make(image.image.width, image.image.height)
        # target = Plane.make(*self.area.world.size.value)

        # match self.fit:
        #    case Image.FILL:
        #        result = curent.scale_to_min(target)
        #    case Image.FULL:
        #        result = curent.scale_to_max(target)

        # result.center(target)

        # image.resize(result.size)
        # self.image.paste(image, result)

        # super().update(path)

        def resize(img, new_width, new_height):
            old_width = img.width()
            old_height = img.height()
            new_photo_image = tkinter.PhotoImage(
                height=new_height,
                width=new_width,
            )
            for x in range(new_width):
                for y in range(new_height):
                    x_old = int(x * old_width / new_width)
                    y_old = int(y * old_height / new_height)
                    rgb = "#%02x%02x%02x" % img.get(x_old, y_old)
                    new_photo_image.put(rgb, (x, y))
            return new_photo_image

        if pillow:
            photo = pillow.ImageTk.PhotoImage(image=self.image.image)
        else:
            width, height = target.size.value

            photo = tkinter.PhotoImage(file=self.path)
            photo = resize(photo, 200, 200)
            # photo = photo.subsample(4, 4)

        # self.photo = photo
        # self.item.configure(image=photo)
        # self.item.configure(image=self.image)

        self.image2 = photo
        self.item.configure(image=photo)
        self.item.image = photo

    def update_image(self, path: P, **star: R) -> N:
        """"""
        if pillow:
            return

        self.path = path
        photo = tkinter.PhotoImage(file=self.path)

        curent = Plane.create(photo.width(), photo.height())
        target = Plane.create(*self.area.world.size.value)

        match self.fit:
            case Image.FILL:
                curent.scale_to_min(target)
            case Image.FULL:
                curent.scale_to_max(target)

        curent.center(target)

        width, height = curent.size.value

        img = photo
        new_width = width
        new_height = height

        old_width = img.width()
        old_height = img.height()
        image = tkinter.PhotoImage(
            height=new_height,
            width=new_width,
        )
        hex_string = "#{:02X}{:02X}{:02X}"
        for x in range(new_width):
            for y in range(new_height):
                x_old = int(x * old_width / new_width)
                y_old = int(y * old_height / new_height)
                color = img.get(x_old, y_old)

                data = hex_string.format(*color)
                to = (x, y)
                image.put(data, to)

        self.item.configure(image=image)
        self.item.image = image

    def update_image(self, path: P, **star: R) -> N:
        """"""
        if pillow:
            return

        self.path = path
        photo = tkinter.PhotoImage(file=self.path)

        old_width = photo.width()
        old_height = photo.height()

        curent = Plane.create(old_width, old_height)
        target = Plane.create(*self.area.world.size)

        match self.fit:
            case Image.FILL:
                curent.scale_to_min(target)
            case Image.FULL:
                curent.scale_to_max(target)

        curent.center(target)

        new_width, new_height = curent.size

        Point(old_width, old_height)

        old_size = Plane.create(old_width, old_width)
        new_size = Plane.create(new_width, new_height)
        # crazy = old_size / new_size

        if new_width < old_width:
            change_width = math.ceil(old_width / new_width)
            change_height = math.ceil(old_height / new_height)
            image = photo.subsample(change_width, change_width)
        else:
            change_width = math.ceil(new_width // old_width)
            change_height = math.ceil(new_height // old_height)
            image = photo.zoom(change_width, change_height)

        self.item.configure(image=image)
        self.item.image = image

    def update_text(self, text: S) -> N:
        """"""
        self.text = text
        self.item.config(text=text)

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.photo = None


class View(View_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        self.canvas = tkinter.Frame(
            canvas,
            padx=0,
            pady=0,
            bg="yellow",
            width=1920,
            height=1080,
        )
        self.place(self.canvas)
        super().make(self.canvas)

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        self.canvas.place_forget()

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place(self.canvas)


class Window(Window_):
    """"""

    @override
    @staticmethod
    def extension() -> LS:
        """"""
        if bool(pillow):
            return pillow.extension()

        return [
            # ".pbm",
            ".pgm",
            ".ppm",
            # ".pnm",
            ".gif",
            ".png",
        ]

    @override
    def run(self) -> N:
        super().run()
        self.canvas.mainloop()

    @override
    def turn(self, page: S, **star: R) -> N:
        super().turn(page, **star)
        self.page.canvas.tkraise()

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.make(1280, 1080)
        self.area = Area.make(1200, 1000)

        self.canvas = tkinter.Tk()
        self.canvas.title(bank.language.APPLICATION_TITLE)
        self.canvas.geometry("1920x1080")
        self.canvas.geometry("1900x1000")
        self.canvas.minsize(640, 480)
        self.canvas.maxsize(3840, 2160)
        self.canvas.config(bg="blue")
