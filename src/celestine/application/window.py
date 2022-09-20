class Button():
    def __init__(self, frame):
        self.frame = frame
        self.item = {}

    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value

    def clear(self):
        self.frame.clear()

    def noutrefresh(self):
        self.frame.noutrefresh()


class Frame():
    def __init__(self, frame):
        self.frame = frame
        self.item = {}

    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value

    def clear(self):
        self.frame.clear()

    def noutrefresh(self):
        self.frame.noutrefresh()


class Window():

    def __init__(self, session):
        self.session = session
        self.item = []
        self.grid = []
        self.cols = 4
        self.rows = 8

    def item_get(self, frame, tag):
        return self.item[frame].item_get(tag)

    def item_set(self, frame, tag, value):
        self.item[frame].item_set(tag, value)

    def frame_get(self, index):
        return self.item[index].frame

    def frame_set(self, value):
        self.item.append(Frame(value))
