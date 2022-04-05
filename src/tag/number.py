from tag.collection import collection
from tag.operator import operator
from mem_dixy.tag.operator import operator
from mem_dixy.Unicode.U0000 import ASTERISK
from mem_dixy.Unicode.U0000 import HYPHEN_MINUS
from mem_dixy.Unicode.U0000 import PLUS_SIGN


class number(collection): # digit?
    def __init__(self):
        super().__init__(
            {
                DIGIT_ZERO,
                DIGIT_ONE,
                DIGIT_TWO,
                DIGIT_THREE,
                DIGIT_FOUR,
                DIGIT_FIVE,
                DIGIT_SIX,
                DIGIT_SEVEN,
                DIGIT_EIGHT,
                DIGIT_NINE,
                LATIN_CAPITAL_LETTER_A,
                LATIN_CAPITAL_LETTER_B,
                LATIN_CAPITAL_LETTER_C,
                LATIN_CAPITAL_LETTER_D,
                LATIN_CAPITAL_LETTER_E,
                LATIN_CAPITAL_LETTER_F
            }
        )

    class _add(operator):
        def __init__(self):
            super().__init__(
                (
                    PLUS_SIGN
                ),
                (
                )
            )

    class _div(operator):
        def __init__(self):
            super().__init__(
                (
                    HYPHEN_MINUS,
                    ASTERISK
                ),
                (
                    PLUS_SIGN,
                    HYPHEN_MINUS,
                    ASTERISK
                )
            )

    class _mul(operator):
        def __init__(self):
            super().__init__(
                (
                    ASTERISK
                ),
                (
                    PLUS_SIGN,
                    ASTERISK
                )
            )

    class _sub(operator):
        def __init__(self):
            super().__init__(
                (
                    HYPHEN_MINUS
                 ),
                (
                    PLUS_SIGN,
                    HYPHEN_MINUS
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
