from celestine.tag.token import Token
from celestine.tag.operator import operator

from celestine.data.alphabet import Comparison


class Comparison2(Token):
    def __init__(self):
        super().__init__(
            {
                Comparison.SAME,
                Comparison.MARK,
                Comparison.MORE,
                Comparison.LESS
            }
        )

    class _eq(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.SAME
                ],
                [
                    Comparison.MARK,
                    Comparison.LESS,
                    Comparison.MORE
                ]
            )

    class _ge(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.MORE,
                    Comparison.SAME
                ],
                [
                    Comparison.MARK,
                    Comparison.LESS
                ]
            )

    class _gt(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.MORE
                ],
                [
                    Comparison.MARK,
                    Comparison.LESS, Comparison.SAME
                ]
            )

    class _le(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.LESS,
                    Comparison.SAME
                ],
                [
                    Comparison.MARK,
                    Comparison.MORE
                ]
            )

    class _lt(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.LESS
                ],
                [
                    Comparison.MARK,
                    Comparison.MORE,
                    Comparison.SAME
                ]
            )

    class _ne(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.MARK,
                    Comparison.SAME
                ],
                [
                    Comparison.LESS,
                    Comparison.MORE
                ]
            )

    class _nn(operator):
        def __init__(self):
            super().__init__(
                [
                    Comparison.MARK
                ],
                [
                    Comparison.MARK,
                    Comparison.LESS,
                    Comparison.SAME,
                    Comparison.MORE
                ]
            )

    class _nu(operator):
        def __init__(self):
            super().__init__(
                [
                ],
                [
                    Comparison.LESS,
                    Comparison.SAME,
                    Comparison.MORE
                ]
            )

    @classmethod
    def parse(cls, iterable):
        index = 0
        index |= Comparison.MARK in iterable
        index <<= 1
        index |= Comparison.LESS in iterable
        index <<= 1
        index |= Comparison.MORE in iterable
        index <<= 1
        index |= Comparison.SAME in iterable
        return cls._table.get(index)

    eq = _eq()  # EQUALITY_OPERATOR
    ge = _ge()  # GREATER_THAN_OR_EQUAL_OPERATOR
    gt = _gt()  # LESS_THAN_OR_EQUAL_OPERATOR
    le = _le()  # LESS_THAN_OR_EQUAL_OPERATOR
    lt = _lt()  # LESS_THAN_OPERATOR
    ne = _ne()  # INEQUALITY_OPERATOR
    nn = _nn()  # IS_NOT_NULL_OPERATOR
    nu = _nu()  # IS_NULL_OPERATOR

    _table = {
        0x0: nu,  # ____
        0x1: eq,  # ___=
        0x2: gt,  # __>_
        0x3: ge,  # __>=
        0x4: lt,  # _<__
        0x5: le,  # _<_=
        0x6: ne,  # _<>_
        0x7: nu,  # _<>=
        0x8: nn,  # !___
        0x9: ne,  # !__=
        0xA: le,  # !_>_
        0xB: lt,  # !_>=
        0xC: ge,  # !<__
        0xD: gt,  # !<_=
        0xE: eq,  # !<>_
        0xF: nn   # !<>=
    }
