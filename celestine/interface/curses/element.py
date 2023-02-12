""""""

from celestine.window.collection import Box


class Element(Box):
    """"""

    def __init__(self, text, kind, **star):
        self.text = text
        self.type = kind
        self.cord_x = 0
        self.cord_y = 0
        self.width = 0
        self.height = 0
        super().__init__(**star)

    def select(self, cord_x, cord_y):
        """"""
        temp_a = cord_x >= self.cord_x
        temp_b = cord_x < self.cord_x + self.width
        temp_c = cord_y >= self.cord_y
        temp_d = cord_y < self.cord_y + self.height
        return temp_a and temp_b and temp_c and temp_d

    def unselect(self, cord_x, cord_y):
        """"""
        return not self.select(cord_x, cord_y)

    def draw(self, frame):
        """"""
        (x_dot, y_dot) = self.center_int()
        self.cord_x = x_dot
        self.cord_y = y_dot
        self.width = len(self.text)
        self.height = 1
        frame.addstr(x_dot, y_dot, self.text)
        return self
