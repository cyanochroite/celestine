from window import window
from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk
from PIL import Image

from list import list

import functools


icon1 = Image.open("character.jpg")
icon2 = Image.open("logo.jpg")
icon3 = Image.open("victory.jpg")

image_list = list()
image_list.add(icon1)
image_list.add(icon2)
image_list.add(icon3)

app = window(image_list)


root = Tk()
root.title("A POOOP")
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


app.mainloop()
