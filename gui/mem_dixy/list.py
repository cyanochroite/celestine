class list:
    def __init__(self):
        self._list = []
        self._index = 0
        self._min = 0
        self._max = -1

    def add(self, item):
        self._list.append(item)
        self._max += 1

    def back(self):
        if self._index > self._min:
            self._index -= 1

    def get(self):
        return self._list[self._index]

    def next(self):
        if self._index < self._max:
            self._index += 1

    def reset(self):
        self._index = self._min
