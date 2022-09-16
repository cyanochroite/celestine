class Window():

    def __init__(self, session):
        self.session = session
        self.item = {}
        self.grid = []
        self.cols = 4
        self.rows = 8

    def item_key(self, frame, tag):
        return F"{frame}-{tag}"

    def item_get(self, frame, tag):
        return self.item[self.item_key(frame, tag)]
        # return self.item[frame].item_get(tag)

    def item_set(self, frame, tag, value):
        self.item[self.item_key(frame, tag)] = value
        #self.item[frame].item_set(tag, value)

    def _frame_key(self, index):
        return F"Page {index}"

    def frame_get(self, frame):
        return self.item[self._frame_key(frame)]

    def frame_set(self, frame, value):
        self.item[self._frame_key(frame)] = value
