"""Internal representatino of letters and symbols."""
import enum


@enum.unique
class Divider(enum.Enum):
    """Spaces and tabs."""
    WHITESPACE = chr(0x0020)


@enum.unique
class Comparison(enum.Enum):
    """< > ! ="""
    MARK = chr(0x0021)
    MORE = chr(0x003E)
    LESS = chr(0x003C)
    SAME = chr(0x003D)


@enum.unique
class Unary(enum.Enum):
    """* + -"""
    STAR = chr(0x002A)
    PLUS = chr(0x002B)
    DASH = chr(0x002D)


@enum.unique
class Letter(enum.Enum):
    """Lowercase letters."""
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
class Digit(enum.Enum):
    """Hexadecimal numbers."""
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
