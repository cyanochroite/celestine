class list:
    def __init__(self):
        self.list = []
        self.index = 0
        self._min = 0
        self._max = -1

    def back(self):
        if self.index > self._min:
            self.index -= 1

    def next(self):
        if self.index < self._max:
            self.index += 1

    def add(self, item):
        self.list.append(item)
        self._max += 1

    def get(self):
        return self.list[self.index]
