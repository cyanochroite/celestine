import abc

import tkinter
import tkinter.ttk


class Frame(tkinter.Frame, metaclass=abc.ABCMeta):
    def __init__(self, master=None, cnf={}, **kw):
        self.data = kw.pop("data", None)
        super().__init__(master, cnf, **kw)
        self.master = self
        self._make()
        self._show()
        self.END = tkinter.END

    @abc.abstractmethod
    def _make(self):
        pass

    @abc.abstractmethod
    def _show(self):
        pass

    def Button(self, **kw):
        return tkinter.Button(self.master, **kw)

    def Entry(self, **kw):
        return tkinter.Entry(self.master, **kw)

    def Label(self, **kw):
        return tkinter.Label(self.master, **kw)

    def Text(self, **kw):
        return tkinter.Text(self.master, **kw)

    def StringVar(self, **kw):
        return tkinter.StringVar()


def Tk():
    return tkinter.Tk()
