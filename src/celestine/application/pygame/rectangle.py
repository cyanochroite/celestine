class Base:
    def __init__(self, **_):
        pass


class Box(Base):
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


class Rectangle(Box):
    def __init__(self, cord_x_min, cord_y_min, cord_x_max, cord_y_max, offset_x=0, offset_y=0):
        super().__init__(
            cord_x_min = cord_x_min,
            cord_y_min = cord_y_min,
            cord_x_max = cord_x_max,
            cord_y_max = cord_y_max,
        )
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

    def spawn(self):
        return Rectangle(
            self.get_x_min(),
            self.get_y_min(),
            self.get_x_max(),
            self.get_y_max(),
            self.offset_x,
            self.offset_y,
        )




class Row(Rectangle):
    def __init__(self, cord_x_min, cord_y_min, cord_x_max, cord_y_max, **kwargs):
        super().__init__(cord_x_min, cord_y_min, cord_x_max, cord_y_max, 200, 0, **kwargs)


class Col(Rectangle):
    def __init__(self, cord_x_min, cord_y_min, cord_x_max, cord_y_max, **kwargs):
        super().__init__(cord_x_min, cord_y_min, cord_x_max, cord_y_max, 0, 50, **kwargs)


class Collection(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item = {}

    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def children(self):
        for _, thing in self.item.items():
            yield thing
