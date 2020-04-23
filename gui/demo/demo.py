import tkinter
from PIL import ImageTk
from PIL import Image
import os

root = tkinter.Tk()
img = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\mem_d\\Downloads\\external-content.duckduckgo.com.png"))

panel = tkinter.Label(root, image=img)

panel.pack(side="bottom", fill="both", expand="yes")


label1 = Label(root, text="some text")
label2 = Label(root, text="syou ugly ")
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

input = Entry(root)
input.pack()


def butt_click():
    lab = Label(root, text="Moan and groan")
    lab.pack()


butt = Button(root, text="moo", command=butt_click)
butt.pack()


root.mainloop()
