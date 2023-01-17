from celestine.data.alphabet import Divider
from celestine.data.alphabet import Unary
from celestine.data.alphabet import Comparison


class Operator():
    def __init__(self, name, primary, secondary):
        self.name = name
        self.value = primary
        self.value = str().join([getattr(item, "value", str(item)) for item in primary])

    def __str__(self):
        return self.value

    def __repr__(self):
        return "<Operator.{0}: '{1}'>".format(self.name, self.value)

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value


class _eq(Operator):
    def __init__(self):
        super().__init__(
            "EQ",
            [
                Comparison.SAME
            ],
            [
                Comparison.MARK,
                Comparison.LESS,
                Comparison.MORE
            ]
        )


class _ge(Operator):
    def __init__(self):
        super().__init__(
            "GE",
            [
                Comparison.MORE,
                Comparison.SAME
            ],
            [
                Comparison.MARK,
                Comparison.LESS
            ]
        )


class _gt(Operator):
    def __init__(self):
        super().__init__(
            "GT",
            [
                Comparison.MORE
            ],
            [
                Comparison.MARK,
                Comparison.LESS,
                Comparison.SAME
            ]
        )


class _le(Operator):
    def __init__(self):
        super().__init__(
            "LE",
            [
                Comparison.LESS,
                Comparison.SAME
            ],
            [
                Comparison.MARK,
                Comparison.MORE
            ]
        )


class _lt(Operator):
    def __init__(self):
        super().__init__(
            "LT",
            [
                Comparison.LESS
            ],
            [
                Comparison.MARK,
                Comparison.MORE,
                Comparison.SAME
            ]
        )


class _ne(Operator):
    def __init__(self):
        super().__init__(
            "NE",
            [
                Comparison.MARK,
                Comparison.SAME
            ],
            [
                Comparison.LESS,
                Comparison.MORE
            ]
        )


class _nn(Operator):
    def __init__(self):
        super().__init__(
            "NN",
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


class _nu(Operator):
    def __init__(self):
        super().__init__(
            "NU",
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


class _add(Operator):
    def __init__(self):
        super().__init__(
            "ADD",
            [
                Unary.PLUS
            ],
            [
            ]
        )


class _div(Operator):
    def __init__(self):
        super().__init__(
            "DIV",
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


class _mul(Operator):
    def __init__(self):
        super().__init__(
            "MUL",
            [
                Unary.STAR
            ],
            [
                Unary.PLUS,
                Unary.STAR
            ]
        )


class _sub(Operator):
    def __init__(self):
        super().__init__(
            "SUB",
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


class tab(Operator):
    def __init__(self, iterable):
        super().__init__(
            "TAB",
            [
                Divider.WHITESPACE
            ],
            [
            ]
        )


class word(Operator):
    def __init__(self, iterable):
        super().__init__(
            "WORD",
            [item for item in iterable],
            []
        )


class number(Operator):
    def __init__(self, iterable):
        super().__init__(
            "NUMBER",
            [item for item in iterable],
            []
        )


_comparison = {
    0x0: _nu(),  # ____
    0x1: _eq(),  # ___=
    0x2: _gt(),  # __>_
    0x3: _ge(),  # __>=
    0x4: _lt(),  # _<__
    0x5: _le(),  # _<_=
    0x6: _ne(),  # _<>_
    0x7: _nu(),  # _<>=
    0x8: _nn(),  # !___
    0x9: _ne(),  # !__=
    0xA: _le(),  # !_>_
    0xB: _lt(),  # !_>=
    0xC: _ge(),  # !<__
    0xD: _gt(),  # !<_=
    0xE: _eq(),  # !<>_
    0xF: _nn()   # !<>=
}
_unary = {
    0x0: _add(),  # ___
    0x1: _mul(),  # __*
    0x2: _sub(),  # _-_
    0x3: _div(),  # _-*
    0x4: _add(),  # +__
    0x5: _mul(),  # +_*
    0x6: _sub(),  # +-_
    0x7: _div(),  # +-*
}


def join(iterable):
    return str().join([item.value for item in iterable])


def tab_parse(iterable):
    return tab(join(iterable))


def word_parse(iterable):
    return word(join(iterable))


def number_parse(iterable):
    return number(join(iterable))


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


