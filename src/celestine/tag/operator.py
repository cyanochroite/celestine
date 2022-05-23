class operator():
    def __init__(self, primary, secondary):
        self._primary = primary
        self._secondary = secondary

    def __str__(self):
        return str().join([item.value for item in self._primary])

    def __repr__(self):
        return str().join(self._primary)

    @classmethod
    def parse(cls, array):
        return NotImplementedError

    @property
    def primary(self):
        return frozenset(self._primary)

    @property
    def secondary(self):
        return frozenset(self._secondary)
