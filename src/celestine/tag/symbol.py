from abc import ABC
from abc import abstractmethod

from celestine.data.alphabet import *


class Symbol(ABC):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    @property
    @abstractmethod
    def alphabet(value):
        raise NotImplementedError

    @classmethod
    def contains(cls, value):
        return value in cls.alphabet


class Sign(Symbol):
    alphabet = frozenset(
        {
            SIGN_MARK,
            SIGN_STAR,
            SIGN_PLUS,
            SIGN_DASH,
            SIGN_LESS,
            SIGN_SAME,
            SIGN_MORE
        }
    )


class Digit(Symbol):
    alphabet = frozenset(
        {
            DIGIT_0,
            DIGIT_1,
            DIGIT_2,
            DIGIT_3,
            DIGIT_4,
            DIGIT_5,
            DIGIT_6,
            DIGIT_7,
            DIGIT_8,
            DIGIT_9,
            DIGIT_A,
            DIGIT_B,
            DIGIT_C,
            DIGIT_D,
            DIGIT_E,
            DIGIT_F
        }
    )


class Letter(Symbol):
    alphabet = frozenset(
        {
            LETTER_A,
            LETTER_B,
            LETTER_C,
            LETTER_D,
            LETTER_E,
            LETTER_F,
            LETTER_G,
            LETTER_H,
            LETTER_I,
            LETTER_J,
            LETTER_K,
            LETTER_L,
            LETTER_M,
            LETTER_N,
            LETTER_O,
            LETTER_P,
            LETTER_Q,
            LETTER_R,
            LETTER_S,
            LETTER_T,
            LETTER_U,
            LETTER_V,
            LETTER_W,
            LETTER_X,
            LETTER_Y,
            LETTER_Z
        }
    )
