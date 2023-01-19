from .package.data import mesh as make_mesh
from .package import mesh as _mesh


class Widget():
    def __init__(self, text, rectangle):
        frame = None
        kind = None
        self.frame = frame
        self.text = text
        self.type = kind
        self.cord_x = 0
        self.cord_y = 0
        self.width = 0
        self.height = 0
        self.mesh = make_mesh.make(text, _mesh.plane(text))
        self.mesh.location = (rectangle.cord_x_min, rectangle.cord_y_min, 0)

    def select(self, cord_x, cord_y):
        temp_a = cord_x >= self.cord_x
        temp_b = cord_x < self.cord_x + self.width
        temp_c = cord_y >= self.cord_y
        temp_d = cord_y < self.cord_y + self.height
        return temp_a and temp_b and temp_c and temp_d

    def unselect(self, cord_x, cord_y):
        return not self.select(cord_x, cord_y)
