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


def image_load(file):
    """pass"""
    return Image(file)


def image(frame, tag, _image):
    """pass"""
    _label = tkinter.Label(frame, image=_image.image)
    item[tag] = _label
    _label.pack()


def button(frame, tag, text):
    """pass"""
    _button = tkinter.Button(
        frame,
        text=text,
        command=lambda: show_frame(text)
    )
    item[F"{frame}-{tag}"] = _button
    _button.pack()


def file_dialog(frame, tag, bind):
    """pass"""
    command = partial(file_dialog_load, bind)
    button = tkinter.Button(
        frame,
        text="Config find Exit",
        command=command
    )
    item[tag] = button
    button.pack()


def label(frame, tag, text):
    """pass"""
    _label = tkinter.Label(
        frame,
        text=text,
        width=100,
        height=4,
        fg="blue"
    )
    item[F"{frame}-{tag}"] = _label
    _label.pack()


def show_frame(text):
    global item

    frame = item[text]
    frame.grid(row=0, column=0, sticky="nsew")

    frame.tkraise()


def main(session):
    """def main"""
    global item
    item = {}

    global root
    root = tkinter.Tk()
    root.title(session.language.APPLICATION_TITLE)

    root.geometry("1920x1080")
    root.minsize(640, 480)
    root.maxsize(3840, 2160)

    container = tkinter.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    index = 0
    for window in session.window:
        frame = tkinter.Frame(container, padx=5, pady=5)
        frame.config(bg="skyblue")
        item[F"Page {index}"] = frame
        window.main(session.task, frame)
        index += 1

    show_frame("Page 0")

    root.mainloop()
