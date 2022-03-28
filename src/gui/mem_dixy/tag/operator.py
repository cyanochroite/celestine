class operator():
    @classmethod
    def __str__(cls):
        return cls.primary

    @classmethod
    def init(cls, array):
        return str().join(array)

    @classmethod
    def parse(cls, array):
        return NotImplementedError

    def __init__(self, primary, secondary):
        self._primary = str().join(primary)
        self._secondary = str().join(secondary)

    @property
    def primary(self):
        return self._primary

    @property
    def secondary(self):
        return self._secondary
