from enum import Enum


from mem_dixy.Unicode.U0000 import *


class enum_comparison(Enum):
    lt = 0,  # less then
    le = 1,  # less then or equal to
    eq = 2,  # equal to
    ne = 3,  # not equal to
    ge = 4,  # greater then
    gt = 5,  # greater then or equal to
    sa = 6,  # select all
    sn = 7  # select none


class operator():
    pass


class comparison(operator):
    primary = NotImplementedError
    secondary = NotImplementedError

    @classmethod
    def __str__(cls):
        return cls.primary

    @classmethod
    def init(cls, array):
        return str().join(array)


class lt(comparison):
    primary = comparison.init([LESS_THAN_SIGN])  # _<__
    secondary = comparison.init([EXCLAMATION_MARK, EQUALS_SIGN, LESS_THAN_SIGN])  # !_=>


class le(comparison):
    primary = comparison.init([LESS_THAN_SIGN, EQUALS_SIGN])  # _<=_
    secondary = comparison.init([EXCLAMATION_MARK, GREATER_THAN_SIGN])  # !__>


class eq(comparison):
    primary = comparison.init([EQUALS_SIGN])  # __=_
    secondary = comparison.init([EXCLAMATION_MARK, LESS_THAN_SIGN, GREATER_THAN_SIGN])  # !<_>


class ne(comparison):
    primary = comparison.init([EXCLAMATION_MARK, EQUALS_SIGN])  # !_=_
    secondary = comparison.init([LESS_THAN_SIGN, GREATER_THAN_SIGN])  # _<_>


class ge(comparison):
    primary = comparison.init([GREATER_THAN_SIGN, EQUALS_SIGN])  # __=>
    secondary = comparison.init([EXCLAMATION_MARK, GREATER_THAN_SIGN])  # !<__


class gt(comparison):
    primary = comparison.init([GREATER_THAN_SIGN])  # ___>
    secondary = comparison.init([EXCLAMATION_MARK, LESS_THAN_SIGN, EQUALS_SIGN])  # !<=_


class sa(comparison):
    primary = comparison.init([])  # ____
    secondary = comparison.init([LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN])  # _<=>


class sn(comparison):
    primary = comparison.init([EXCLAMATION_MARK])  # !___
    secondary = comparison.init([EXCLAMATION_MARK, LESS_THAN_SIGN, EQUALS_SIGN, GREATER_THAN_SIGN])  # !<=>

