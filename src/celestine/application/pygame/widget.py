class Widget():
    def __init__(self, frame, text, kind):
        self.frame = frame
        self.text = text
        self.type = kind
        self.cord_x = 0
        self.cord_y = 0
        self.width = 0
        self.height = 0

    def grid(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = len(self.text)
        self.height = 1
        return self
