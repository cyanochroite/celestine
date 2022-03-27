from mem_dixy.Unicode.U0000 import *
from mem_dixy.tag.operator import operator


class unary(operator):
    @classmethod
    def parse(cls, array):  # +-*
        index = 0
        index |= PLUS_SIGN in array
        index <<= 1
        index |= HYPHEN_MINUS in array
        index <<= 1
        index |= ASTERISK in array
        return index


class add(unary):  # UNARY_PLUS_OPERATOR
    primary = unary.init([PLUS_SIGN])  # +__
    secondary = unary.init([])  # ___


class sub(unary):  # UNARY_MINUS_OPERATOR
    primary = unary.init([HYPHEN_MINUS])  # _-_
    secondary = unary.init([PLUS_SIGN, HYPHEN_MINUS])  # +-_


class mul(unary):  # POINTER_INDIRECTION_OPERATOR
    primary = unary.init([ASTERISK])  # __*
    secondary = unary.init([PLUS_SIGN, ASTERISK])  # +_*


class div(unary):  # POINTER_INDIRECTION_OPERATOR
    primary = unary.init([HYPHEN_MINUS, ASTERISK])  # _-*
    secondary = unary.init([PLUS_SIGN, HYPHEN_MINUS, ASTERISK])  # +-*
