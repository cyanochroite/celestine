""""""

from celestine.window.element import Element as element


class Element(element):
    """"""

    def __init__(self, text, kind, **star):
        self.text = text
        self.type = kind
        self.cord_x = 0
        self.cord_y = 0
        self.width = 0
        self.height = 0
        super().__init__(**star)

    def origin(self):
        """"""
        x_dot = int(self.x_min)
        y_dot = int(self.y_min)
        return (x_dot, y_dot)

    def add_string(self, frame, x_dot, y_dot, text):
        """curses swaps x and y"""
        frame.addstr(y_dot, x_dot, text)

    def draw(self, frame):
        """"""
        (x_dot, y_dot) = self.origin()
        self.cord_x = x_dot
        self.cord_y = y_dot
        self.width = len(self.text)
        self.height = 1
        self.add_string(frame, x_dot, y_dot, self.text)
        return self
