class Base:
    def __init__(self, **_):
        pass


class Rectangle(Base):
    def __init__(self, cord_x, cord_y, width, height, right, top, **kwargs):
        super().__init__(**kwargs)
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = width
        self.height = height
        self.right = right
        self.top = top

    def cords_x(self):
        value = self.cord_x
        self.cord_x += self.right
        return value

    def cords_y(self):
        value = self.cord_y
        self.cord_y += self.top
        return value

    def spawn(self):
        return Rectangle(
            self.cords_x(),
            self.cords_y(),
            0,
            0,
            self.right,
            self.top,
        )

    def inside(self, cord_x, cord_y):
        left = self.cord_x < cord_x
        right = self.cord_x + self.width > cord_x
        top = self.cord_y < cord_y
        bottom = self.cord_y + self.height > cord_y
        return left and right and top and bottom


class Row(Rectangle):
    def __init__(self, cord_x, cord_y, width, height, **kwargs):
        super().__init__(cord_x, cord_y, width, height, 200, 0, **kwargs)

    def spawn(self):
        return Rectangle(
            self.cords_x(),
            self.cords_y(),
            200,
            self.height,
            self.right,
            self.top,
        )


class Col(Rectangle):
    def __init__(self, cord_x, cord_y, width, height, **kwargs):
        super().__init__(cord_x, cord_y, width, height, 0, 50, **kwargs)

    def spawn(self):
        return Rectangle(
            self.cords_x(),
            self.cords_y(),
            self.width,
            50,
            self.right,
            self.top,
        )


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
        for key, thing in self.item.items():
            yield thing
