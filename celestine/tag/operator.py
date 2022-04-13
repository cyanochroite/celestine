class operator():
    def __init__(self, primary, secondary):
        self._primary = tuple(primary)
        self._secondary = tuple(secondary)

    def __str__(self):
        return str().join(self._primary)

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
