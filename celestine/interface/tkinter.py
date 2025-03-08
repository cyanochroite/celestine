""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    tkinter,
)
from celestine.typed import (
    ANY,
    LS,
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
from celestine.window.collection import Area


class Abstract(Abstract_):
    """"""

    def place(self, item: ANY) -> N:
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
    def build(self, parent: ANY, **star: R) -> N:
        """"""
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
            self.item = tkinter.Button(parent, **star)
        else:
            self.item = tkinter.Label(parent, **star)
        self.place(self.item)

        super().build(parent, **star)

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place(self.item)

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
            pil_image = pil_image.resize(image_size.size.value)
            pil_photo = PIL.ImageTk.PhotoImage(image=pil_image)
            self.item.configure(image=pil_photo)
            self.item.image = pil_photo
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

                self.item.configure(image=image)
                self.item.image = image

        super().reimage(path, **star)

    @override
    def retext(self, text: S, **star: R) -> N:
        """"""
        self.item.configure(text=text)
        super().retext(text, **star)

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.photo = None


class View(View_, Abstract):
    """"""

    @override
    def build(self, parent: ANY, **star: R) -> N:
        """"""
        ignore(star)
        self.canvas = tkinter.Frame(
            parent,
            padx=0,
            pady=0,
            bg="yellow",
            width=1920,
            height=1080,
        )
        self.place(self.canvas)
        super().build(self.canvas)

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
        self.page.canvas.tkraise()

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.fast(1280, 1080)
        self.area = Area.fast(1200, 1000)

        self.canvas = tkinter.Tk()
        self.canvas.title(bank.language.APPLICATION_TITLE)
        self.canvas.geometry("1920x1080")
        self.canvas.geometry("1900x1000")
        self.canvas.minsize(640, 480)
        self.canvas.maxsize(3840, 2160)
        self.canvas.configure(bg="blue")


ignore(Window)
