from mem_dixy.Unicode.U0000 import ASTERISK
from mem_dixy.Unicode.U0000 import HYPHEN_MINUS
from mem_dixy.Unicode.U0000 import PLUS_SIGN
from mem_dixy.tag.operator import operator


class unary():
    @classmethod
    def parse(cls, array):  # +-*
        index = 0
        index |= PLUS_SIGN in array
        index <<= 1
        index |= HYPHEN_MINUS in array
        index <<= 1
        index |= ASTERISK in array
        return index

    class _add(operator):  # UNARY_PLUS_OPERATOR
        def __init__(self):
            super().__init__(
                [PLUS_SIGN],  # +__
                []  # ___
            )

    class _sub(operator):  # UNARY_MINUS_OPERATOR
        def __init__(self):
            super().__init__(
                [HYPHEN_MINUS],  # _-_
                [PLUS_SIGN, HYPHEN_MINUS]  # +-_
            )

    class _mul(operator):  # POINTER_INDIRECTION_OPERATOR
        def __init__(self):
            super().__init__(
                [ASTERISK],  # __*
                [PLUS_SIGN, ASTERISK]  # +_*
            )

    class _div(operator):  # POINTER_INDIRECTION_OPERATOR
        def __init__(self):
            super().__init__(
                [HYPHEN_MINUS, ASTERISK],  # _-*
                [PLUS_SIGN, HYPHEN_MINUS, ASTERISK]  # +-*
            )

    add = _add()
    sub = _sub()
    mul = _mul()
    div = _div()
