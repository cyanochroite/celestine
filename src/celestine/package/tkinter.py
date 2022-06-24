# https://docs.python.org/3/library/tk.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
import tkinter
import tkinter.ttk
import tkinter.filedialog
from functools import partial


class Image():
    def __init__(self, file):
        image = tkinter.PhotoImage(file=file)
        self.height = image.height()
        self.image = image
        self.width = image.width()
        self.name = file


def browseFiles():
    filename = tkinter.filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("Text files", "*.txt*"),
            ("all files", "*.*")
        )
    )

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


class Window():
    def __init__(self):
        self.item = {}

    def file_dialog(self, tag, bind):
        command = partial(self.filebox_load, bind)
        item = tkinter.Button(
            self.root,
            text="Config find Exit",
            command=command
        )
        self.item[tag] = item
        item.pack()

    def file_dialog_load(self, tag):
        filename = tkinter.filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(
                ("Text files", "*.txt*"),
                ("all files", "*.*")
            )
        )
        self.item[tag].configure(text="File Opened: " + filename)

    def image(self, tag, image):
        item = tkinter.Label(self.root, image=image.image)
        self.item[tag] = item
        item.pack()

    def image_load(self, file):
        return Image(file)

    def label(self, tag, text):
        item = tkinter.Label(
            self.root,
            text=text,
            width=100,
            height=4,
            fg="blue"
        )
        self.item[tag] = item
        item.pack()

    def run(self, app):
        self.root = tkinter.Tk()
        self.root.title('celestine · PyPI')

        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="skyblue")

        app.setup(self)
        app.view(self)

        self.root.mainloop()


