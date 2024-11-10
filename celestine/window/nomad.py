""""""

from celestine.literal import (
    COMMA,
    FULL_STOP,
    LEFT_PARENTHESIS,
    RIGHT_PARENTHESIS,
    SPACE,
    string,
)
from celestine.typed import (
    TS,
    A,
    K,
    N,
    S,
    Struct,
    T,
    ignore,
    override,
)


class Nomad(Struct):
    """"""

    __slots__: TS = ("name",)

    name: S

    def __del__(self) -> N:
        super().__del__()
        del self.name

    def __new__(cls, *_: A) -> K:
        new = super().__new__(cls)
        name = repr(cls)
        index = name.rindex(FULL_STOP) + 1
        new.name = name[index:-2]
        return new

    def __repr__(self):
        data = self.__str__()
        result = string(self.name, data)
        return result

    def __str__(self):
        comma = string(COMMA, SPACE)
        data = comma.join(map(repr, self.data))
        result = string(LEFT_PARENTHESIS, data, RIGHT_PARENTHESIS)
        return result


class Monad[X](Nomad):
    """"""

    __slots__: TS = ("one",)

    one: X

    @override
    def _del(self) -> N:
        del self.one

    @override
    def _get(self) -> T[X]:
        return (self.one,)

    @override
    def _set(self, value: T[X]) -> N:
        self.one = value[0]

    def __init__(self, one: X) -> N:
        ignore(self)
        super().__init__(one)

    def __new__(cls, one: X) -> K:
        return super().__new__(cls, one)

    data = property(_get, _set, _del)


class Dyad[X](Nomad):
    """"""

    __slots__: TS = ("one", "two")

    one: X
    two: X

    @override
    def _del(self) -> N:
        del self.one
        del self.two

    @override
    def _get(self) -> T[X, X]:
        return (self.one, self.two)

    @override
    def _set(self, value: T[X, X]) -> N:
        self.one = value[0]
        self.two = value[1]

    def __init__(self, one: X, two: X) -> N:
        ignore(self)
        super().__init__(one, two)

    def __new__(cls, one: X, two: X) -> K:
        return super().__new__(cls, one, two)

    data = property(_get, _set, _del)


class Triad[X](Nomad):
    """"""

    __slots__: TS = ("one", "two", "tri")

    one: X
    two: X
    tri: X

    @override
    def _del(self) -> N:
        del self.one
        del self.two
        del self.tri

    @override
    def _get(self) -> T[X, X, X]:
        return (self.one, self.two, self.tri)

    @override
    def _set(self, value: T[X, X, X]) -> N:
        self.one = value[0]
        self.two = value[1]
        self.tri = value[2]

    def __init__(self, one: X, two: X, tri: X) -> N:
        ignore(self)
        super().__init__(one, two, tri)

    def __new__(cls, one: X, two: X, tri: X) -> K:
        return super().__new__(cls, one, two, tri)

    data = property(_get, _set, _del)


class Tetrad[X](Nomad):
    """"""

    __slots__: TS = ("one", "two", "tri", "tet")

    one: X
    two: X
    tri: X
    tet: X

    @override
    def _del(self) -> N:
        del self.one
        del self.two
        del self.tri
        del self.tet

    @override
    def _get(self) -> T[X, X, X, X]:
        return (self.one, self.two, self.tri, self.tet)

    @override
    def _set(self, value: T[X, X, X, X]) -> N:
        self.one = value[0]
        self.two = value[1]
        self.tri = value[2]
        self.tet = value[3]

    def __init__(self, one: X, two: X, tri: X, tet: X) -> N:
        ignore(self)
        super().__init__(one, two, tri, tet)

    def __new__(cls, one: X, two: X, tri: X, tet: X) -> K:
        return super().__new__(cls, one, two, tri, tet)

    data = property(_get, _set, _del)
