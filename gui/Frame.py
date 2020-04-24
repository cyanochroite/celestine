import abc
import tkinter


class Frame(tkinter.Frame, metaclass=abc.ABCMeta):
    def __init__(self, master=None, cnf={}, **kw):
        self.data = kw.pop("data", None)
        super().__init__(master, cnf, **kw)
        self.master = self
        self._make()
        self._show()

    def _init_button(self, text, command):
        button = tkinter.Button(self.master)
        button["text"] = text
        button["command"] = command
        return button

    def _init_label(self, image, width=None, height=None):
        label = tkinter.Label(self.master)
        if image:
            label["image"] = image
        if width:
            label["height"] = height
        if height:
            label["width"] = width
        return label

    @abc.abstractmethod
    def _make(self):
        pass

    @abc.abstractmethod
    def _show(self):
        pass
