from tag.operator import operator
from Unicode.U0000 import EQUALS_SIGN
from Unicode.U0000 import EXCLAMATION_MARK
from Unicode.U0000 import GREATER_THAN_SIGN
from Unicode.U0000 import LESS_THAN_SIGN


class comparison():
    class _eq(operator):
        def __init__(self):
            super().__init__(
                (
                    EQUALS_SIGN
                ),
                (
                    EXCLAMATION_MARK,
                    LESS_THAN_SIGN,
                    GREATER_THAN_SIGN
                )
            )

    class _ge(operator):
        def __init__(self):
            super().__init__(
                (
                    GREATER_THAN_SIGN,
                    EQUALS_SIGN
                 ),
                (
                    EXCLAMATION_MARK,
                    LESS_THAN_SIGN
                )
            )

    class _gt(operator):
        def __init__(self):
            super().__init__(
                (
                    GREATER_THAN_SIGN
                 ),
                (
                    EXCLAMATION_MARK,
                    LESS_THAN_SIGN, EQUALS_SIGN
                )
            )

    class _le(operator):
        def __init__(self):
            super().__init__(
                (
                    LESS_THAN_SIGN,
                    EQUALS_SIGN
                 ),
                (
                    EXCLAMATION_MARK,
                    GREATER_THAN_SIGN
                )
            )

    class _lt(operator):
        def __init__(self):
            super().__init__(
                (
                    LESS_THAN_SIGN
                ),
                (
                    EXCLAMATION_MARK,
                    GREATER_THAN_SIGN,
                    EQUALS_SIGN
                )
            )

    class _ne(operator):
        def __init__(self):
            super().__init__(
                (
                    EXCLAMATION_MARK,
                    EQUALS_SIGN),
                (
                    LESS_THAN_SIGN,
                    GREATER_THAN_SIGN)
            )

    class _nn(operator):
        def __init__(self):
            super().__init__(
                (
                    EXCLAMATION_MARK
                ),
                (
                    EXCLAMATION_MARK,
                    LESS_THAN_SIGN,
                    EQUALS_SIGN,
                    GREATER_THAN_SIGN
                 )
            )

    class _nu(operator):
        def __init__(self):
            super().__init__(
                (
                ),
                (
                    LESS_THAN_SIGN,
                    EQUALS_SIGN,
                    GREATER_THAN_SIGN
                )
            )

    @classmethod
    def parse(cls, array):
        index = 0
        index |= EXCLAMATION_MARK in array
        index <<= 1
        index |= LESS_THAN_SIGN in array
        index <<= 1
        index |= GREATER_THAN_SIGN in array
        index <<= 1
        index |= EQUALS_SIGN in array
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
