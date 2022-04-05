class collection():
    def __init__(self, members):
        self._members = frozenset(members)

    def __str__(self):
        return str().join(self._members)

    def __repr__(self):
        return str().join(self._members)