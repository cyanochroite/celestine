from celestine.package import tkinter


class Widget():
    def __init__(self, item):
        self.item = item
        self.item.pack(side=tkinter.LEFT)
