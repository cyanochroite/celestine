from application import application
import PIL


from list import list


class window(application):
    def __init__(self, image_list):
        super().__init__(image_list)

        self.button_back = self._init_button("<<", self._button_back)
        self.button_next = self._init_button(">>", self._button_next)
        self.button_quit = self._init_button("Exit Program", self.tk.quit)
        self.label_screen = self._init_label(
            self.image_list.get(), 512, 512)

        self.create_widgets()

    def create_widgets(self):
        self.button_quit.grid(row=0, column=1)
        self.button_back.grid(row=2, column=0)
        self.button_next.grid(row=2, column=2)
        self.label_screen.grid(row=1, column=0, columnspan=3)

    def reset_image(self):
        self.label_screen["image"] = self.image_list.get()

    def _button_back(self):
        self.image_list.back()
        self.reset_image()

    def _button_next(self):
        self.image_list.next()
        self.reset_image()


from Frame import Frame
from one import one
import tkinter
import tkinter.ttk


class MainApplication(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.statusbar = one(self.master)
        self.left = one(self.master)

        self.statusbar.grid(row=0, column=1)

        icon1 = PIL.Image.open("character.jpg")
        icon2 = PIL.Image.open("logo.jpg")
        icon3 = PIL.Image.open("victory.jpg")

        image_list = list()
        image_list.add(icon1)
        image_list.add(icon2)
        image_list.add(icon3)

        self.statusbar.create_widgets(image_list)
        self.left.create_widgets(image_list)

        self.left.grid(row=1, column=0)


if __name__ == "__main__":
    root = tkinter.Tk()
    MainApplication(root).grid(row=0, column=0)
    root.mainloop()
