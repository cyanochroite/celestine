import tkinter
import tkinter.ttk

from PIL import ImageTk
from list import list


class application():
    def __init__(self, image_list):
        self.tk = tkinter.Tk()
        self.tk.title("A title")
        self.tk.iconbitmap("favicon.ico")

        fist = image_list
        self.image_list = list()
        self.image_list.add(ImageTk.PhotoImage(fist.get()))
        fist.next()
        self.image_list.add(ImageTk.PhotoImage(fist.get()))
        fist.next()
        self.image_list.add(ImageTk.PhotoImage(fist.get()))
        fist.next()

    def _init_button(self, text, command):
        button = tkinter.Button(self.tk)
        button["text"] = text
        button["command"] = command
        return button

    def _init_label(self, image, width=None, height=None):
        label = tkinter.Label(self.tk)
        label["image"] = image
        if width:
            label["height"] = height
        if height:
            label["width"] = width
        return label

    def mainloop(self):
        self.tk.mainloop()
