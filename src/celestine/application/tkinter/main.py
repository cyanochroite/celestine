"""Package tkinter."""
# https://docs.python.org/3/library/tk.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
import tkinter
import tkinter.ttk
import tkinter.filedialog
from functools import partial


def item_key(frame, tag):
    global item
    return F"{frame}-{tag}"


def item_get(frame, tag):
    global item
    return item[item_key(frame, tag)]


def item_set(frame, tag, value):
    global item
    item[item_key(frame, tag)] = value


def frame_key(index):
    return F"Page {index}"


def frame_get(frame):
    global item
    return item[frame]


def frame_set(frame, value):
    global item
    item[frame] = value


def show_frame(text):
    global item

    frame = item[text]
    frame.grid(row=0, column=0, sticky="nsew")

    frame.tkraise()



class Image():
    """Holds an image."""

    def __init__(self, file):
        _image = tkinter.PhotoImage(file=file)
        self.height = _image.height()
        self.image = _image
        self.width = _image.width()
        self.name = file


def file_dialog_load(frame, tag):
    """pass"""
    filename = tkinter.filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("Text files", "*.txt*"),
            ("all files", "*.*")
        )
    )
    item_get(frame, tag).configure(text="File Opened: " + filename)


def image_load(file):
    """pass"""
    return Image(file)





def button(frame, tag, text):
    """pass"""
    item_set(
        frame,
        tag,
        tkinter.Button(
            frame_get(frame),
            text=text,
            command=lambda: show_frame(text),
        ),
    )
    item_get(frame, tag).pack()


def file_dialog(frame, tag, bind):
    """pass"""
    item_set(
        frame,
        tag,
        tkinter.Button(
            frame_get(frame),
            text="Config find Exit",
            command=partial(file_dialog_load, frame, bind),
        ),
    )
    item_get(frame, tag).pack()


def image(frame, tag, _image):
    """pass"""
    item_set(
        frame,
        tag,
        tkinter.Label(
            frame_get(frame),
            image=_image.image,
        ),
    )
    item_get(frame, tag).pack()


def label(frame, tag, text):
    """pass"""
    item_set(
        frame,
        tag,
        tkinter.Label(
            frame_get(frame),
            text=text,
            width=100,
            height=4,
            fg="blue",
        ),
    )
    item_get(frame, tag).pack()


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
        key = frame_key(index)
        frame_set(key, frame)
        window.main(session, key)
        index += 1

    show_frame(frame_key(0))

    root.mainloop()
