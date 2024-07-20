""""""

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

        size = self.area.local.size.value
        self.image = tkinter.PhotoImage()

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
        target = Plane.make(*self.area.world.size.value)

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

        if pillow:
            photo = pillow.ImageTk.PhotoImage(image=self.image.image)
        else:
            width, height = target.size.value
            photo = tkinter.PhotoImage(
                file=self.path,
                width=0,
                height=0,
            )

        self.photo = photo
        # self.item.configure(image=photo)
        self.item.configure(image=self.image)

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
    def extension(self) -> LS:
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

        self.canvas = tkinter.Tk()
        self.canvas.title(bank.language.APPLICATION_TITLE)
        self.canvas.geometry("1920x1080")
        self.canvas.minsize(640, 480)
        self.canvas.maxsize(3840, 2160)
        self.canvas.config(bg="blue")
