""""""


class Object:
    """"""

    def __init__(self, **_):
        super().__init__()


class Box(Object):
    """"""

    def center_float(self):
        """"""
        x_dot = (self.x_min + self.x_max) / 2
        y_dot = (self.y_min + self.y_max) / 2
        return (x_dot, y_dot)

    def center_int(self):
        """"""
        x_dot = (self.x_min + self.x_max) // 2
        y_dot = (self.y_min + self.y_max) // 2
        return (x_dot, y_dot)

    def inside(self, x_dot, y_dot):
        """"""
        x_test = self.x_min <= x_dot < self.x_max
        y_test = self.y_min <= y_dot < self.y_max
        x = F"{self.x_min}<={x_dot}<{self.x_max}={x_test}"
        y = F"{self.y_min}<={y_dot}<{self.y_max}={y_test}"
        print(F"{x} & {y}")

        return x_test and y_test

    def __init__(self, x_min=0, y_min=0, x_max=0, y_max=0, **kwargs):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        super().__init__(**kwargs)


class Collection(Object):
    """"""

    def children(self):
        """"""
        for _, thing in self.item.items():
            yield thing

    def item_get(self, tag):
        """"""
        return self.item[tag]

    def item_set(self, tag, value):
        """"""
        self.item[tag] = value
        return value

    def __init__(self, **kwargs):
        self.item = {}
        super().__init__(**kwargs)


class Rectangle(Box, Collection):
    """"""

    def action(self):
        """"""
        raise NotImplementedError()

    def get_next(self):
        """"""
        x_min = self.move_x_min
        self.move_x_min += self.offset_x

        y_min = self.move_y_min
        self.move_y_min += self.offset_y

        x_max = self.move_x_min if self.offset_x else self.x_max
        y_max = self.move_y_min if self.offset_y else self.y_max

        return (x_min, y_min, x_max, y_max)

    def select(self, x_dot, y_dot):
        """"""
        if self.inside(x_dot, y_dot):
            self.action()
            for child in self.children():
                child.select(x_dot, y_dot)

    def spawn(self):
        """"""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return Rectangle(
            x_min=x_min,
            y_min=y_min,
            x_max=x_max,
            y_max=y_max,
            offset_x=self.offset_x,
            offset_y=self.offset_y,
        )

    def __init__(self, offset_x=0, offset_y=0, **kwargs):
        super().__init__(**kwargs)
        if "row" in kwargs:
            offset_x = 300
        if "col" in kwargs:
            offset_y = 50

        self.start_x_min = self.x_min
        self.start_y_min = self.y_min
        self.start_x_max = self.x_max
        self.start_y_max = self.y_max

        self.move_x_min = self.x_min
        self.move_y_min = self.y_min
        self.move_x_max = self.x_max
        self.move_y_max = self.y_max

        self.offset_x = offset_x
        self.offset_y = offset_y
