import tkinter


class Frame(tkinter.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.master = self

    def _init_button(self, text, command):
        button = tkinter.Button(self.master)
        button["text"] = text
        button["command"] = command
        return button

    def _init_label(self, image, width=None, height=None):
        label = tkinter.Label(self.master)
        label["image"] = image
        if width:
            label["height"] = height
        if height:
            label["width"] = width
        return label
