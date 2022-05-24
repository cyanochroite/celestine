from celestine.data.alphabet import Divider
from celestine.data.alphabet import Unary
from celestine.data.alphabet import Comparison


class Token():
    def __init__(self, kind, value):
        self._kind = kind
        self._value = value

    @property
    def kind(self):
        return self._kind

    @property
    def value(self):
        return self._value



class operator():
    def __init__(self, primary, secondary):
        self._primary = primary
        self._secondary = secondary

    def __str__(self):
        return str().join([item.value for item in self._primary])

    def __repr__(self):
        return "<OPERATOR.{0}: '{1}'>".format("????", str().join([item.value for item in self._primary]))

    @classmethod
    def parse(cls, array):
        return NotImplementedError

    @property
    def primary(self):
        return frozenset(self._primary)

    @property
    def secondary(self):
        return frozenset(self._secondary)




def eq():
    return Token("eq", 
            [
                Comparison.SAME
            ],
            [
                Comparison.MARK,
                Comparison.LESS,
                Comparison.MORE
            ]
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

eq = _eq()  # EQUALITY_OPERATOR
ge = _ge()  # GREATER_THAN_OR_EQUAL_OPERATOR
gt = _gt()  # LESS_THAN_OR_EQUAL_OPERATOR
le = _le()  # LESS_THAN_OR_EQUAL_OPERATOR
lt = _lt()  # LESS_THAN_OPERATOR
ne = _ne()  # INEQUALITY_OPERATOR
nn = _nn()  # IS_NOT_NULL_OPERATOR
nu = _nu()  # IS_NULL_OPERATOR




class _add(operator):
    def __init__(self):
        super().__init__(
            [
                Unary.PLUS
            ],
            [
            ]
        )

class _div(operator):
    def __init__(self):
        super().__init__(
            [
                Unary.DASH,
                Unary.STAR
            ],
            [
                Unary.PLUS,
                Unary.DASH,
                Unary.STAR
            ]
        )

class _mul(operator):
    def __init__(self):
        super().__init__(
            [
                Unary.STAR
            ],
            [
                Unary.PLUS,
                Unary.STAR
            ]
        )

class _sub(operator):
    def __init__(self):
        super().__init__(
            [
                Unary.DASH
            ],
            [
                Unary.PLUS,
                Unary.DASH
            ]
        )


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


    
class _tab(operator):
    def __init__(self, iterable):
        super().__init__(
            [
                Divider.WHITESPACE
            ],
            [
            ]
        )

class _word(operator):
    def __init__(self, iterable):
        super().__init__(
            [item for item in iterable],
            []
        )


class _number(operator):
    def __init__(self, iterable):
        super().__init__(
            [item for item in iterable],
            []
        )




_comparison = {
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
_unary = {
    0x0: add,  # ___
    0x1: mul,  # __*
    0x2: sub,  # _-_
    0x3: div,  # _-*
    0x4: add,  # +__
    0x5: mul,  # +_*
    0x6: sub,  # +-_
    0x7: div,  # +-*
}

def tab_parse(iterable):
    return _tab(iterable)


def word_parse(iterable):
    return _word(iterable)


def number_parse(iterable):
    return _number(iterable)



def unary_parse(iterable):
    index = 0
    index |= Unary.PLUS in iterable
    index <<= 1
    index |= Unary.DASH in iterable
    index <<= 1
    index |= Unary.STAR in iterable
    return _unary.get(index)


def comparison_parse(iterable):
    index = 0
    index |= Comparison.MARK in iterable
    index <<= 1
    index |= Comparison.LESS in iterable
    index <<= 1
    index |= Comparison.MORE in iterable
    index <<= 1
    index |= Comparison.SAME in iterable
    return _comparison.get(index)






import enum



@enum.unique
class Comparison3(enum.Enum):
    eq = _eq()  # EQUALITY_OPERATOR
    ge = _ge()  # GREATER_THAN_OR_EQUAL_OPERATOR
    gt = _gt()  # LESS_THAN_OR_EQUAL_OPERATOR
    le = _le()  # LESS_THAN_OR_EQUAL_OPERATOR
    lt = _lt()  # LESS_THAN_OPERATOR
    ne = _ne()  # INEQUALITY_OPERATOR
    nn = _nn()  # IS_NOT_NULL_OPERATOR
    nu = _nu()  # IS_NULL_OPERATOR


@enum.unique
class Unary3(enum.Enum):
    STAR = chr(0x002A)
    PLUS = chr(0x002B)
    DASH = chr(0x002D)


@enum.unique
class Letter3(enum.Enum):
    LETTER_A = chr(0x0061)
    LETTER_B = chr(0x0062)
    LETTER_C = chr(0x0063)
    LETTER_D = chr(0x0064)
    LETTER_E = chr(0x0065)
    LETTER_F = chr(0x0066)
    LETTER_G = chr(0x0067)
    LETTER_H = chr(0x0068)
    LETTER_I = chr(0x0069)
    LETTER_J = chr(0x006A)
    LETTER_K = chr(0x006B)
    LETTER_L = chr(0x006C)
    LETTER_M = chr(0x006D)
    LETTER_N = chr(0x006E)
    LETTER_O = chr(0x006F)
    LETTER_P = chr(0x0070)
    LETTER_Q = chr(0x0071)
    LETTER_R = chr(0x0072)
    LETTER_S = chr(0x0073)
    LETTER_T = chr(0x0074)
    LETTER_U = chr(0x0075)
    LETTER_V = chr(0x0076)
    LETTER_W = chr(0x0077)
    LETTER_X = chr(0x0078)
    LETTER_Y = chr(0x0079)
    LETTER_Z = chr(0x007A)
    LETTER__ = chr(0x005F)


@enum.unique
class Digi3t(enum.Enum):
    DIGIT_0 = chr(0x0030)
    DIGIT_1 = chr(0x0031)
    DIGIT_2 = chr(0x0032)
    DIGIT_3 = chr(0x0033)
    DIGIT_4 = chr(0x0034)
    DIGIT_5 = chr(0x0035)
    DIGIT_6 = chr(0x0036)
    DIGIT_7 = chr(0x0037)
    DIGIT_8 = chr(0x0038)
    DIGIT_9 = chr(0x0039)
    DIGIT_A = chr(0x0041)
    DIGIT_B = chr(0x0042)
    DIGIT_C = chr(0x0043)
    DIGIT_D = chr(0x0044)
    DIGIT_E = chr(0x0045)
    DIGIT_F = chr(0x0046)


