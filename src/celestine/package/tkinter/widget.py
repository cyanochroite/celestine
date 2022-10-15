from . import package


class Widget():
    def __init__(self, item):
        self.item = item
        self.item.pack(side=package.LEFT)
