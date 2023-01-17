class Widget():
    def __init__(self, frame, text, kind):
        self.frame = frame
        self.text = text
        self.type = kind
        self.cord_x = 0
        self.cord_y = 0
        self.width = 0
        self.height = 0

    def select(self, cord_x, cord_y):
        temp_a = cord_x >= self.cord_x
        temp_b = cord_x < self.cord_x + self.width
        temp_c = cord_y >= self.cord_y
        temp_d = cord_y < self.cord_y + self.height
        return temp_a and temp_b and temp_c and temp_d

    def unselect(self, cord_x, cord_y):
        return not self.select(cord_x, cord_y)

    def grid(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = len(self.text)
        self.height = 1
        self.frame.addstr(cord_y, cord_x * 20, self.text)
        return self
