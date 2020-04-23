from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk
from PIL import Image

from list import list

import functools

root = Tk()
root.title("A title")
root.iconbitmap("favicon.ico")
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=0, column=1)


def reset_image():
    laddel["image"] = image_list.get()


def forward():
    image_list.next()
    reset_image()


def back():
    image_list.back()
    reset_image()


icon1 = ImageTk.PhotoImage(Image.open("character.jpg"))
icon2 = ImageTk.PhotoImage(Image.open("logo.jpg"))
icon3 = ImageTk.PhotoImage(Image.open("victory.jpg"))

image_list = list()
image_list.add(icon1)
image_list.add(icon2)
image_list.add(icon3)

laddel = Label(image=icon1)
laddel.grid(row=1, column=0, columnspan=3)

back_button = Button(root, text="<<", command=back)
button_forward = Button(root, text=">>", command=forward)

index = 0


back_button.grid(row=2, column=0)
button_forward.grid(row=2, column=2)


root.mainloop()


class Navbar(Frame):
    ...


class Toolbar(Frame):
    ...


class Statusbar(Frame):
    ...


class Main(Frame):
    ...


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)
