class Collection():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item = {}

    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def children(self):
        for _, thing in self.item.items():
            yield thing

