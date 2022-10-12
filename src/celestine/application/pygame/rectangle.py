class Rectangle():
    def __init__(self, cord_x, cord_y, width, height):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = width
        self.height = height

    def cords_y(self):
        value = self.cord_y
        self.cord_y += 50
        return value
