# https://docs.python.org/3/library/tk.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
import tkinter
import tkinter.ttk


class Image():
    def __init__(self, file):
        image = tkinter.PhotoImage(file=file)
        self.height = image.height()
        self.image = image
        self.width = image.width()
        self.name = file


class Window():
    def label_add(self, image):
        tkinter.Label(self.root, image=image.image).pack()

    def image_load(self, file):
        return Image(file)

    def run(self, setup, view):
        self.root = tkinter.Tk()
        self.root.title('celestine · PyPI')

        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="skyblue")

        setup(self)
        view(self)

        self.root.mainloop()


