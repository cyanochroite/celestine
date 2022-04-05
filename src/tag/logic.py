from tag.collection import collection
from tag.operator import operator
from unicode.u0000 import AMPERSAND
from unicode.u0000 import CIRCUMFLEX_ACCENT
from unicode.u0000 import VERTICAL_LINE
from unicode.u0000 import TILDE


class logic(collection):
    def __init__(self):
        super().__init__(
            {
                AMPERSAND,
                CIRCUMFLEX_ACCENT,
                VERTICAL_LINE,
                TILDE
            }
        )
    class _and(operator):
        def __init__(self):
            super().__init__(
                (
                    AMPERSAND
                ),
                (
                    AMPERSAND
                )
            )

    class _is(operator):
        def __init__(self):
            super().__init__(
                (
                    CIRCUMFLEX_ACCENT
                ),
                (
                    CIRCUMFLEX_ACCENT
                )
            )

    class _not(operator):
        def __init__(self):
            super().__init__(
                (
                    TILDE
                ),
                (
                    TILDE
                )
            )

    class _or(operator):
        def __init__(self):
            super().__init__(
                (
                    VERTICAL_LINE
                 ),
                (
                    VERTICAL_LINE
                )
            )

    @classmethod
    def parse(cls, array):
        index = 0
        index |= PLUS_SIGN in array
        index <<= 1
        index |= HYPHEN_MINUS in array
        index <<= 1
        index |= ASTERISK in array
        return cls._table.get(index)

    land = _and()  # UNARY_PLUS_OPERATOR
    his = _is()  # POINTER_INDIRECTION_OPERATOR
    snot = _not()  # POINTER_INDIRECTION_OPERATOR
    tor = _or()  # UNARY_MINUS_OPERATOR

    _table = {
        0x0: add,  # ___
        0x1: mul,  # __*
        0x2: sub,  # _-_
        0x3: div,  # _-*
        0x4: add,  # +__
        0x5: mul,  # +_*
        0x6: sub,  # +-_
        0x7: div,  # +-*
    }
