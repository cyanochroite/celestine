from tkinter import *
from PIL import ImageTk
from PIL import Image

import functools

root = Tk()
root.title("A title")
root.iconbitmap("favicon.ico")
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=0, column=1)


def reset_image():
    global index
    global laddel
    laddel.grid_forget()
    laddel = Label(image=image_list[index])
    laddel.grid(row=1, column=0, columnspan=3)


def forward():
    global index
    index += 1
    reset_image()
    return


def back():
    global index
    index -= 1
    reset_image()
    return


icon1 = ImageTk.PhotoImage(Image.open("character.jpg"))
icon2 = ImageTk.PhotoImage(Image.open("logo.jpg"))
icon3 = ImageTk.PhotoImage(Image.open("victory.jpg"))

image_list = [icon1, icon2, icon3]

laddel = Label(image=icon1)
laddel.grid(row=1, column=0, columnspan=3)

back_button = Button(root, text="<<", command=back)
button_forward = Button(root, text=">>", command=forward)

index = 0


back_button.grid(row=2, column=0)
button_forward.grid(row=2, column=2)

root.mainloop()
