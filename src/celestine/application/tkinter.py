"""Package tkinter."""
# https://docs.python.org/3/library/tk.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
import tkinter
import tkinter.ttk
import tkinter.filedialog
from functools import partial


class Image():
    """Holds an image."""
    def __init__(self, file):
        _image = tkinter.PhotoImage(file=file)
        self.height = _image.height()
        self.image = _image
        self.width = _image.width()
        self.name = file


def file_dialog(tag, bind):
    """pass"""
    command = partial(file_dialog_load, bind)
    button = tkinter.Button(
        root,
        text="Config find Exit",
        command=command
    )
    item[tag] = button
    button.pack()


def file_dialog_load(tag):
    """pass"""
    filename = tkinter.filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("Text files", "*.txt*"),
            ("all files", "*.*")
        )
    )
    item[tag].configure(text="File Opened: " + filename)


def image(tag, _image):
    """pass"""
    _label = tkinter.Label(root, image=_image.image)
    item[tag] = _label
    _label.pack()


def image_load(file):
    """pass"""
    return Image(file)


def label(tag, text):
    """pass"""
    _label = tkinter.Label(
        root,
        text=text,
        width=100,
        height=4,
        fg="blue"
    )
    item[tag] = _label
    _label.pack()


def main(**kwargs):
    """def main"""
    session = kwargs["session"]
    window = kwargs["window"]

    global item
    item = {}

    global root
    root = tkinter.Tk()
    root.title(session.language.APPLICATION_TITLE)

    root.geometry("1920x1080")
    root.minsize(640, 480)
    root.maxsize(3840, 2160)
    root.config(bg="skyblue")

    window.setup()
    window.view()

    root.mainloop()
