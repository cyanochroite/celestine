""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import (
    Plane,
    Point,
)
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    tkinter,
)
from celestine.typed import (
    LS,
    A,
    B,
    D,
    N,
    P,
    R,
    S,
    ignore,
    override,
)
from celestine.window.cardinal import (
    Dyad,
    Round,
)


class Abstract(Abstract_):
    """"""

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)
        if parent:
            self.canvas = parent.canvas

    def place(self) -> N:
        """"""
        self.canvas.place(
            x=self.area.x_min,
            y=self.area.y_min,
            width=self.area.x_len,
            height=self.area.y_len,
        )


class Element(Element_, Abstract):
    """"""

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        self.canvas.place_forget()

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)

        # TODO: self.area.local.size.value
        self.image = tkinter.PhotoImage(
            width=200,
            height=200,
        )

        def callback() -> N:
            """"""
            self.click(self.area.centroid)
            bank.dequeue()

        # Change everything to button and disable if no action?
        if self.action or self.goto:
            star.update(command=callback)
            self.canvas = tkinter.Button(self.canvas, **star)
        else:
            self.canvas = tkinter.Label(self.canvas, **star)
        self.place()

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place()

    @override
    def reimage(self, path: P, **star: R) -> N:
        """"""
        if bool(PIL):
            pil_image = PIL.Image.open(
                fp=path,
                mode=LATIN_SMALL_LETTER_R,
                formats=bank.window.formats(),
            )
            pil_image = pil_image.convert("RGB")
            image_size = self.image_size(pil_image.size)
            pil_image = pil_image.resize(image_size.size.data)
            pil_photo = PIL.ImageTk.PhotoImage(image=pil_image)
            self.canvas.configure(image=pil_photo)
            self.canvas.image = pil_photo
        else:
            photo = tkinter.PhotoImage(file=path)

            old_width = photo.width()
            old_height = photo.height()

            image_size = self.image_size((old_width, old_height))
            new_width, new_height = image_size.size

            old_size = Dyad(old_width, old_height)
            new_size = Dyad(new_width, new_height)

            if new_width < old_width:
                change = old_size / new_size
                change = change.inplace(Round.positive)
                image = photo.subsample(change.one, change.two)
            else:
                change = new_size / old_size
                change = change.inplace(Round.negative)
                image = photo.zoom(change.one, change.two)

                self.canvas.configure(image=image)
                self.canvas.image = image

        super().reimage(path, **star)

    @override
    def retext(self, text: S, **star: R) -> N:
        """"""
        self.canvas.configure(text=text)
        super().retext(text, **star)

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.photo = None

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)
        self.canvas = tkinter.Frame(
            parent.canvas,
            padx=0,
            pady=0,
            bg="yellow",
            width=1920,
            height=1080,
        )
        self.place()

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        self.canvas.place_forget()

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place()


class Window(Window_, Element):
    """"""

    @override
    @classmethod
    def make(cls, *data: A, **star: R) -> Object:
        """"""
        return Element(*data, **star)

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        self.canvas = tkinter.Tk()
        self.canvas.title(bank.language.APPLICATION_TITLE)
        self.canvas.geometry("1920x1080")
        self.canvas.geometry("1900x1000")
        self.canvas.minsize(640, 480)
        self.canvas.maxsize(3840, 2160)
        self.canvas.configure(bg="blue")

    @override
    @classmethod
    def extension(cls) -> LS:
        ignore(cls)
        if bool(PIL):
            return super().extension()

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
        # self.item.canvas.tkraise()
        #  This might be able to be a draw call.

    @override
    def __init__(self) -> N:
        super().__init__()
        self.area = Plane.make(1280, 1080)
        self.area = Plane.make(1200, 1000)


ignore(Window)
