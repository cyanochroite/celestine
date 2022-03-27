class operator():
    primary = NotImplementedError
    secondary = NotImplementedError

    @classmethod
    def __str__(cls):
        return cls.primary

    @classmethod
    def init(cls, array):
        return str().join(array)

    @classmethod
    def parse(cls, array):
        return NotImplementedError
