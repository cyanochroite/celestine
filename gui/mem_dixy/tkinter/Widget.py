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

    @abc.abstractmethod
    def _make(self):
        pass

    @abc.abstractmethod
    def _show(self):
        pass

    def button(self, **kw):
        return tkinter.Button(self.master, **kw)

    def label(self, **kw):
        return tkinter.Label(self.master, **kw)


def Tk():
    return tkinter.Tk()
