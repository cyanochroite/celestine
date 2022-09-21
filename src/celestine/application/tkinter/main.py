"""Package tkinter."""
# https://docs.python.org/3/library/tk.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
from functools import partial

from celestine.application.window import Window as Window_
from celestine.package import tkinter


class Widget():
    def __init__(self, item):
        self.item = item
        self.item.pack(side=tkinter.LEFT)

    def grid(self, cord_x, cord_y):
        self.item.grid(column=cord_x, row=cord_y)


class Button(Widget):
    def __init__(self, frame, text, command):
        super().__init__(
            tkinter.Button(
                frame,
                text=text,
                command=command,
            )
        )


class Label(Widget):
    def __init__(self, frame, **kwargs):
        super().__init__(
            tkinter.Label(
                frame,
                **kwargs,
            )
        )


class Image():
    """Holds an image."""

    def __init__(self, file):
        _image = tkinter.PhotoImage(file=file)
        self.height = _image.height()
        self.image = _image
        self.width = _image.width()
        self.name = file



class Frame():
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def __init__(self, window):
        self.window = window
        self.item = {}
        self.frame = tkinter.Frame(
            self.window.root,
            padx=5,
            pady=5,
            bg="skyblue",
        )

    def __enter__(self):
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.index = len(self.window.item)
        self.window.frame_set(self.frame)
        return self

    def __exit__(self, *_):
        return False

    def row(self, tag):
        return self.item_set(tag, Row(self, tag))


class Row():
    def __init__(self, frame, tag):
        self.frame = frame
        self.tag = tag
        self.row = tkinter.Frame(frame.frame)

    def __enter__(self):
        self.row.pack()
        return self

    def __exit__(self, *_):
        return False

    def button(self, tag, label, action):
        return self.frame.item_set(
            tag,
            Button(
                self.row,
                label,
                lambda: self.frame.window.show_frame(action),
            ),
        )

    def label(self, tag, text):
        return self.frame.item_set(
            tag,
            Label(
                self.row,
                text=text,
                width=100,
                height=4,
                fg="blue",
            ),
        )

class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        self.root = None

    def show_frame(self, index):
        frame = self.frame_get(index)
        frame.tkraise()

    def file_dialog_load(self, frame, tag):
        """pass"""
        filename = tkinter.filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(
                ("Text files", "*.txt*"),
                ("all files", "*.*")
            )
        )
        self.item_get(frame, tag).item.configure(
            text="File Opened: " + filename)

    def image_load(self, file):
        """pass"""
        return Image(file)

    def _button(self, frame, tag, label, action):
        item = Button(
            self.frame_get(frame),
            label,
            lambda: self.show_frame(action),
        )
        self.item_set(frame, tag, item)
        return item

    def file_dialog(self, frame, tag, action):
        item = Button(
            self.frame_get(frame),
            "Config find Exit",
            partial(self.file_dialog_load, frame, action),
        )
        self.item_set(frame, tag, item)
        return item

    def image(self, frame, tag, _image):
        item = Label(
            self.frame_get(frame),
            image=_image.image,
        )
        self.item_set(frame, tag, item)
        return item

    def _label(self, index, frame, tag, text):
        item = Label(
            frame,
            text=text,
            width=100,
            height=4,
            fg="blue",
        )
        self.item_set(index, tag, item)
        return item

    def frame(self):
        return Frame(self)


    def main(self):
        self.root = tkinter.Tk()
        self.root.title(self.session.language.APPLICATION_TITLE)

        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")

        for window in self.session.window:
            window.main(self)

        self.show_frame(0)

        self.root.mainloop()
