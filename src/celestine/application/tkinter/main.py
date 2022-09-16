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


class Window():

    def item_key(self, frame, tag):
        return F"{frame}-{tag}"

    def item_get(self, frame, tag):
        return self.item[self.item_key(frame, tag)]

    def item_set(self, frame, tag, value):
        self.item[self.item_key(frame, tag)] = value

    def frame_key(self, index):
        return F"Page {index}"

    def frame_get(self, frame):
        return self.item[frame]

    def frame_set(self, frame, value):
        self.item[frame] = value

    def show_frame(self, text):

        frame = self.item[text]
        frame.grid(row=0, column=0, sticky="nsew")

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
        self.item_get(frame, tag).configure(text="File Opened: " + filename)

    def image_load(self, file):
        """pass"""
        return Image(file)

    def button(self, frame, tag, text, cord_x, cord_y):
        """pass"""
        self.item_set(
            frame,
            tag,
            tkinter.Button(
                self.frame_get(frame),
                text=text,
                command=lambda: self.show_frame(text),
            ),
        )
        self.item_get(frame, tag).grid(column=cord_x, row=cord_y)

    def file_dialog(self, frame, tag, bind, cord_x, cord_y):
        """pass"""
        self.item_set(
            frame,
            tag,
            tkinter.Button(
                self.frame_get(frame),
                text="Config find Exit",
                command=partial(self.file_dialog_load, frame, bind),
            ),
        )
        self.item_get(frame, tag).grid(column=cord_x, row=cord_y)

    def image(self, frame, tag, _image, cord_x, cord_y):
        """pass"""
        self.item_set(
            frame,
            tag,
            tkinter.Label(
                self.frame_get(frame),
                image=_image.image,
            ),
        )
        self.item_get(frame, tag).grid(column=cord_x, row=cord_y)

    def label(self, frame, tag, text, cord_x, cord_y):
        """pass"""
        self.item_set(
            frame,
            tag,
            tkinter.Label(
                self.frame_get(frame),
                text=text,
                width=100,
                height=4,
                fg="blue",
            ),
        )
        self.item_get(frame, tag).grid(column=cord_x, row=cord_y)

    def __init__(self):
        self.item = {}
        self.root = None

    def main(self, session):
        """def main"""

        global root
        self.root = tkinter.Tk()
        self.root.title(session.language.APPLICATION_TITLE)

        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")

        index = 0
        for window in session.window:
            frame = tkinter.Frame(self.root, padx=5, pady=5, bg="skyblue")

            key = self.frame_key(index)
            self.frame_set(key, frame)
            window.main(session, key, self)
            index += 1

        self.show_frame(self.frame_key(0))

        self.root.mainloop()
