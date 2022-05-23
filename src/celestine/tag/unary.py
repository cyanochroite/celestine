from celestine.tag.token import Token
from celestine.tag.operator import operator

from celestine.data.alphabet import Unary

class Unary2(Token):
    def __init__(self):
        super().__init__(
            {
                Unary.STAR,
                Unary.DASH,
                Unary.PLUS
            }
        )

    class _add(operator):
        def __init__(self):
            super().__init__(
                (
                    Unary.PLUS
                ),
                (
                )
            )

    class _div(operator):
        def __init__(self):
            super().__init__(
                (
                    Unary.DASH,
                    Unary.STAR
                ),
                (
                    Unary.PLUS,
                    Unary.DASH,
                    Unary.STAR
                )
            )

    class _mul(operator):
        def __init__(self):
            super().__init__(
                (
                    Unary.STAR
                ),
                (
                    Unary.PLUS,
                    Unary.STAR
                )
            )

    class _sub(operator):
        def __init__(self):
            super().__init__(
                (
                    Unary.DASH
                 ),
                (
                    Unary.PLUS,
                    Unary.DASH
                )
            )

    @classmethod
    def parse(cls, array):
        index = 0
        index |= Unary.PLUS in array
        index <<= 1
        index |= Unary.DASH in array
        index <<= 1
        index |= Unary.STAR in array
        return cls._table.get(index)

    add = _add()  # UNARY_PLUS_OPERATOR
    div = _div()  # POINTER_INDIRECTION_OPERATOR
    mul = _mul()  # POINTER_INDIRECTION_OPERATOR
    sub = _sub()  # UNARY_MINUS_OPERATOR

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
