class Object:
    def __init__(self, **_):
        super().__init__()


class Box(Object):
    def __init__(self, cord_x_min, cord_y_min, cord_x_max, cord_y_max, **kwargs):
        super().__init__(**kwargs)
        self.cord_x_min = cord_x_min
        self.cord_y_min = cord_y_min
        self.cord_x_max = cord_x_max
        self.cord_y_max = cord_y_max

    def inside(self, cord_x, cord_y):
        aaa = self.cord_x_min < cord_x
        bbb = self.cord_y_min < cord_y
        ccc = self.cord_x_max > cord_x
        ddd = self.cord_y_max > cord_y
        return aaa and bbb and ccc and ddd


class Collection(Object):
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def children(self):
        for _, thing in self.item.items():
            yield thing

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item = {}


class Rectangle(Box, Collection):
    def __init__(self, cord_x_min=0, cord_y_min=0, cord_x_max=0, cord_y_max=0, offset_x=0, offset_y=0, **kwargs):
        super().__init__(
            cord_x_min = cord_x_min,
            cord_y_min = cord_y_min,
            cord_x_max = cord_x_max,
            cord_y_max = cord_y_max,
            **kwargs,
        )
        if "row" in kwargs:
            offset_x = 300
        if "col" in kwargs:
            offset_y = 50
        self.move_x_min = cord_x_min
        self.move_y_min = cord_y_min
        self.move_x_max = cord_x_max
        self.move_y_max = cord_y_max
        self.offset_x = offset_x
        self.offset_y = offset_y

    def get_x_min(self):
        value = self.move_x_min
        self.move_x_min += self.offset_x
        return value

    def get_y_min(self):
        value = self.move_y_min
        self.move_y_min += self.offset_y
        return value

    def get_x_max(self):
        # only works if you call get_x_min first
        return self.move_x_min if self.offset_x else self.cord_x_max

    def get_y_max(self):
        # only works if you call get_y_min first
        return self.move_y_min if self.offset_y else self.cord_y_max

    def action(self):
        pass

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()
            for child in self.children():
                child.select(cord_x, cord_y)

    def spawn(self):
        return Rectangle(
            self.get_x_min(),
            self.get_y_min(),
            self.get_x_max(),
            self.get_y_max(),
            self.offset_x,
            self.offset_y,
        )
