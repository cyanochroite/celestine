class operator():
    @classmethod
    def __str__(cls):
        try:
            return str().join(cls.primary)
        except:
            return str()


    @classmethod
    def init(cls, array):
        return str().join(array)

    @classmethod
    def parse(cls, array):
        return NotImplementedError

    def __init__(self, primary, secondary):
        self._primary = frozenset(primary)
        self._secondary = frozenset(secondary)

    @property
    def primary(self):
        return self._primary

    @property
    def secondary(self):
        return self._secondary
