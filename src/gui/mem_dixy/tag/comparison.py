from mem_dixy.Unicode.U0000 import *
from mem_dixy.tag.operator import operator


class comparison(operator):
    @classmethod
    def parse(cls, array):  # !<>=
        index = 0
        index |= EXCLAMATION_MARK in array
        index <<= 1
        index |= LESS_THAN_SIGN in array
        index <<= 1
        index |= GREATER_THAN_SIGN in array
        index <<= 1
        index |= EQUALS_SIGN in array
        return index


class eq(comparison):  # EQUALITY_OPERATOR
    primary = comparison.init([EQUALS_SIGN])  # __=_
    secondary = comparison.init([EXCLAMATION_MARK, LESS_THAN_SIGN, GREATER_THAN_SIGN])  # !<_>


class ge(comparison):  # GREATER_THAN_OR_EQUAL_OPERATOR
    primary = comparison.init([GREATER_THAN_SIGN, EQUALS_SIGN])  # __=>
    secondary = comparison.init([EXCLAMATION_MARK, GREATER_THAN_SIGN])  # !<__


class gt(comparison):  # GREATER_THAN_OPERATOR
    primary = comparison.init([GREATER_THAN_SIGN])  # ___>
    secondary = comparison.init([EXCLAMATION_MARK, LESS_THAN_SIGN, EQUALS_SIGN])  # !<=_


class le(comparison):  # LESS_THAN_OR_EQUAL_OPERATOR
    primary = comparison.init([LESS_THAN_SIGN, EQUALS_SIGN])  # _<=_
    secondary = comparison.init([EXCLAMATION_MARK, GREATER_THAN_SIGN])  # !__>


class lt(comparison):  # LESS_THAN_OPERATOR
    primary = comparison.init([LESS_THAN_SIGN])  # _<__
    secondary = comparison.init([EXCLAMATION_MARK, EQUALS_SIGN, LESS_THAN_SIGN])  # !_=>


class ne(comparison):  # INEQUALITY_OPERATOR
    primary = comparison.init([EXCLAMATION_MARK, EQUALS_SIGN])  # !_=_
    secondary = comparison.init([LESS_THAN_SIGN, GREATER_THAN_SIGN])  # _<_>


class nn(comparison):  # IS_NOT_NULL_OPERATOR
    primary = comparison.init([EXCLAMATION_MARK])  # !___
    secondary = comparison.init([EXCLAMATION_MARK, LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN])  # !<=>


class nu(comparison):  # IS_NULL_OPERATOR
    primary = comparison.init([])  # ____
    secondary = comparison.init([LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN])  # _<=>
