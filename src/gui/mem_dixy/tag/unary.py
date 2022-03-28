from mem_dixy.tag.operator import operator
from mem_dixy.Unicode.U0000 import ASTERISK
from mem_dixy.Unicode.U0000 import HYPHEN_MINUS
from mem_dixy.Unicode.U0000 import PLUS_SIGN


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

    class _div(operator):  # POINTER_INDIRECTION_OPERATOR
        def __init__(self):
            super().__init__(
                [HYPHEN_MINUS, ASTERISK],  # _-*
                [PLUS_SIGN, HYPHEN_MINUS, ASTERISK]  # +-*
            )

    class _mul(operator):  # POINTER_INDIRECTION_OPERATOR
        def __init__(self):
            super().__init__(
                [ASTERISK],  # __*
                [PLUS_SIGN, ASTERISK]  # +_*
            )

    class _sub(operator):  # UNARY_MINUS_OPERATOR
        def __init__(self):
            super().__init__(
                [HYPHEN_MINUS],  # _-_
                [PLUS_SIGN, HYPHEN_MINUS]  # +-_
            )

    add = _add()
    div = _div()
    mul = _mul()
    sub = _sub()
