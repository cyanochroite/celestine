import tkinter
import tkinter.ttk

from PIL import ImageTk
from PIL import Image
from list import list


class application():
    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title("A title")
        self.tk.iconbitmap("favicon.ico")

    def _init_button(self, text, command):
        button = tkinter.Button(self.tk)
        button["text"] = text
        button["command"] = command
        return button

    def mainloop(self):
        self.tk.mainloop()


class window(application):
    def __init__(self, image_list):
        super().__init__()
        self.image_list = image_list

        self.button_back = self._init_button("<<", self._button_back)
        self.button_next = self._init_button(">>", self._button_next)
        self.button_quit = self._init_button("Exit Program", self.tk.quit)
        self.label_screen = tkinter.Label(self.tk)

        self.create_widgets()

    def create_widgets(self):
        self.button_quit.grid(row=0, column=1)
        self.button_back.grid(row=2, column=0)
        self.button_next.grid(row=2, column=2)
        self.label_screen.grid(row=1, column=0, columnspan=3)

    def reset_image(self):
        image = self.image_list.get()
        self.image = ImageTk.PhotoImage(image)
        self.label_screen["image"] = self.image

    def _button_back(self):
        self.image_list.back()
        self.reset_image()

    def _button_next(self):
        self.image_list.next()
        self.reset_image()


#app = window()
# app.mainloop()


icon1 = Image.open("character.jpg")
icon2 = Image.open("logo.jpg")
icon3 = Image.open("victory.jpg")


image_list = list()
image_list.add(icon1)
image_list.add(icon2)
image_list.add(icon3)

app = window(image_list)
app.mainloop()
