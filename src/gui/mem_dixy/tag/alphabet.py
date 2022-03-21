from mem_dixy.Unicode.U0000 import *
from mem_dixy.Unicode.U0080 import *

from mem_dixy.Unicode_Encoding.U0000 import encoding as Basic_Latin
from mem_dixy.Unicode_Encoding.U0080 import encoding as Latin_1_Supplement

from mem_dixy.tag.comparison import *

convert = Basic_Latin | Latin_1_Supplement


lowercase = {
    LATIN_CAPITAL_LETTER_A: LATIN_SMALL_LETTER_A,
    LATIN_CAPITAL_LETTER_B: LATIN_SMALL_LETTER_B,
    LATIN_CAPITAL_LETTER_C: LATIN_SMALL_LETTER_C,
    LATIN_CAPITAL_LETTER_D: LATIN_SMALL_LETTER_D,
    LATIN_CAPITAL_LETTER_E: LATIN_SMALL_LETTER_E,
    LATIN_CAPITAL_LETTER_F: LATIN_SMALL_LETTER_F,
    LATIN_CAPITAL_LETTER_G: LATIN_SMALL_LETTER_G,
    LATIN_CAPITAL_LETTER_H: LATIN_SMALL_LETTER_H,
    LATIN_CAPITAL_LETTER_I: LATIN_SMALL_LETTER_I,
    LATIN_CAPITAL_LETTER_J: LATIN_SMALL_LETTER_J,
    LATIN_CAPITAL_LETTER_K: LATIN_SMALL_LETTER_K,
    LATIN_CAPITAL_LETTER_L: LATIN_SMALL_LETTER_L,
    LATIN_CAPITAL_LETTER_M: LATIN_SMALL_LETTER_M,
    LATIN_CAPITAL_LETTER_N: LATIN_SMALL_LETTER_N,
    LATIN_CAPITAL_LETTER_O: LATIN_SMALL_LETTER_O,
    LATIN_CAPITAL_LETTER_P: LATIN_SMALL_LETTER_P,
    LATIN_CAPITAL_LETTER_Q: LATIN_SMALL_LETTER_Q,
    LATIN_CAPITAL_LETTER_R: LATIN_SMALL_LETTER_R,
    LATIN_CAPITAL_LETTER_S: LATIN_SMALL_LETTER_S,
    LATIN_CAPITAL_LETTER_T: LATIN_SMALL_LETTER_T,
    LATIN_CAPITAL_LETTER_U: LATIN_SMALL_LETTER_U,
    LATIN_CAPITAL_LETTER_V: LATIN_SMALL_LETTER_V,
    LATIN_CAPITAL_LETTER_W: LATIN_SMALL_LETTER_W,
    LATIN_CAPITAL_LETTER_X: LATIN_SMALL_LETTER_X,
    LATIN_CAPITAL_LETTER_Y: LATIN_SMALL_LETTER_Y,
    LATIN_CAPITAL_LETTER_Z: LATIN_SMALL_LETTER_Z,
    LOW_LINE: LOW_LINE,
    LATIN_SMALL_LETTER_A: LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_B: LATIN_SMALL_LETTER_B,
    LATIN_SMALL_LETTER_C: LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_D: LATIN_SMALL_LETTER_D,
    LATIN_SMALL_LETTER_E: LATIN_SMALL_LETTER_E,
    LATIN_SMALL_LETTER_F: LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_G: LATIN_SMALL_LETTER_G,
    LATIN_SMALL_LETTER_H: LATIN_SMALL_LETTER_H,
    LATIN_SMALL_LETTER_I: LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_J: LATIN_SMALL_LETTER_J,
    LATIN_SMALL_LETTER_K: LATIN_SMALL_LETTER_K,
    LATIN_SMALL_LETTER_L: LATIN_SMALL_LETTER_L,
    LATIN_SMALL_LETTER_M: LATIN_SMALL_LETTER_M,
    LATIN_SMALL_LETTER_N: LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_O: LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_P: LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_Q: LATIN_SMALL_LETTER_Q,
    LATIN_SMALL_LETTER_R: LATIN_SMALL_LETTER_R,
    LATIN_SMALL_LETTER_S: LATIN_SMALL_LETTER_S,
    LATIN_SMALL_LETTER_T: LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_U: LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_V: LATIN_SMALL_LETTER_V,
    LATIN_SMALL_LETTER_W: LATIN_SMALL_LETTER_W,
    LATIN_SMALL_LETTER_X: LATIN_SMALL_LETTER_X,
    LATIN_SMALL_LETTER_Y: LATIN_SMALL_LETTER_Y,
    LATIN_SMALL_LETTER_Z: LATIN_SMALL_LETTER_Z,
}

number = {
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
    LATIN_CAPITAL_LETTER_F,
}

tag = {
    LOW_LINE,
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_B,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_D,
    LATIN_SMALL_LETTER_E,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_G,
    LATIN_SMALL_LETTER_H,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_J,
    LATIN_SMALL_LETTER_K,
    LATIN_SMALL_LETTER_L,
    LATIN_SMALL_LETTER_M,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_Q,
    LATIN_SMALL_LETTER_R,
    LATIN_SMALL_LETTER_S,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_V,
    LATIN_SMALL_LETTER_W,
    LATIN_SMALL_LETTER_X,
    LATIN_SMALL_LETTER_Y,
    LATIN_SMALL_LETTER_Z
}

space = {
    SPACE
}

sql_and = {
    AMPERSAND
}

sql_is = {
    PLUS_SIGN
}

sql_not = {
    HYPHEN_MINUS
}

sql_or = {
    VERTICAL_LINE
}

logica_operator = sql_and | sql_is | sql_not | sql_or


letter = {
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
    LATIN_CAPITAL_LETTER_F,
    LATIN_CAPITAL_LETTER_G,
    LATIN_CAPITAL_LETTER_H,
    LATIN_CAPITAL_LETTER_I,
    LATIN_CAPITAL_LETTER_J,
    LATIN_CAPITAL_LETTER_K,
    LATIN_CAPITAL_LETTER_L,
    LATIN_CAPITAL_LETTER_M,
    LATIN_CAPITAL_LETTER_N,
    LATIN_CAPITAL_LETTER_O,
    LATIN_CAPITAL_LETTER_P,
    LATIN_CAPITAL_LETTER_Q,
    LATIN_CAPITAL_LETTER_R,
    LATIN_CAPITAL_LETTER_S,
    LATIN_CAPITAL_LETTER_T,
    LATIN_CAPITAL_LETTER_U,
    LATIN_CAPITAL_LETTER_V,
    LATIN_CAPITAL_LETTER_W,
    LATIN_CAPITAL_LETTER_X,
    LATIN_CAPITAL_LETTER_Y,
    LATIN_CAPITAL_LETTER_Z,
    LOW_LINE,
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_B,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_D,
    LATIN_SMALL_LETTER_E,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_G,
    LATIN_SMALL_LETTER_H,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_J,
    LATIN_SMALL_LETTER_K,
    LATIN_SMALL_LETTER_L,
    LATIN_SMALL_LETTER_M,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_Q,
    LATIN_SMALL_LETTER_R,
    LATIN_SMALL_LETTER_S,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_V,
    LATIN_SMALL_LETTER_W,
    LATIN_SMALL_LETTER_X,
    LATIN_SMALL_LETTER_Y,
    LATIN_SMALL_LETTER_Z
}


one_token = {
    QUOTATION_MARK,
    NUMBER_SIGN,
    DOLLAR_SIGN,
    PERCENT_SIGN,
    AMPERSAND,
    APOSTROPHE,
    LEFT_PARENTHESIS,
    RIGHT_PARENTHESIS,
    ASTERISK,
    PLUS_SIGN,
    COMMA,
    HYPHEN_MINUS,
    FULL_STOP,
    SOLIDUS,
    COLON,
    SEMICOLON,
    QUESTION_MARK,
    COMMERCIA_AT,
    LEFT_SQUARE_BRACKET,
    REVERSE_SOLIDUS,
    RIGHT_SQUARE_BRACKET,
    CIRCUMFLEX_ACCENT,
    GRAVE_ACCENT,
    LEFT_CURLY_BRACKET,
    VERTICAL_LINE,
    RIGHT_CURLY_BRACKET,
    TILDE,
}

comparison = {
    EXCLAMATION_MARK,
    LESS_THAN_SIGN,
    EQUALS_SIGN,
    GREATER_THAN_SIGN,
}

logical = {
    AMPERSAND,
    PLUS_SIGN,
    HYPHEN_MINUS,
    CIRCUMFLEX_ACCENT,
    VERTICAL_LINE,
    TILDE
}


digit = {
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
}

consonant = {
    LATIN_SMALL_LETTER_B,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_D,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_G,
    LATIN_SMALL_LETTER_H,
    LATIN_SMALL_LETTER_J,
    LATIN_SMALL_LETTER_K,
    LATIN_SMALL_LETTER_L,
    LATIN_SMALL_LETTER_M,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_Q,
    LATIN_SMALL_LETTER_R,
    LATIN_SMALL_LETTER_S,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_V,
    LATIN_SMALL_LETTER_W,
    LATIN_SMALL_LETTER_X,
    LATIN_SMALL_LETTER_Z
}

vowel = {
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_E,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_Y
}

wildcard = {
    NUMBER_SIGN,
    PERCENT_SIGN,
    ASTERISK,
    COLON,
    QUESTION_MARK,
    COMMERCIA_AT,
}

comparison_primary = {
    enum_comparison.lt: lt.primary,
    enum_comparison.le: le.primary,
    enum_comparison.eq: eq.primary,
    enum_comparison.ne: ne.primary,
    enum_comparison.ge: ge.primary,
    enum_comparison.gt: gt.primary,
    enum_comparison.sa: sa.primary,
    enum_comparison.sn: sn.primary
}

comparison_secondary = {
    enum_comparison.lt: lt.secondary,
    enum_comparison.le: le.secondary,
    enum_comparison.eq: eq.secondary,
    enum_comparison.ne: ne.secondary,
    enum_comparison.ge: ge.secondary,
    enum_comparison.gt: gt.secondary,
    enum_comparison.sa: sa.secondary,
    enum_comparison.sn: sn.secondary
}

# The percent sign % can be used to match a number


# The asterisk (*) matches any number of characters. That means that you can use it as a placeholder for any sequence of letters or symbols. For example, if you enter blueb* you'll get all the terms that start with "blueb"; if you enter *bird you'll get all the terms that end with "bird"; if you enter *lueb* you'll get all the terms that contain the sequence "lueb", and so forth. An asterisk can match zero characters, too.

# The question mark (?) matches exactly one character. That means that you can use it as a placeholder for a single letter or symbol. The query l?b?n?n,  for example, will find the word "Lebanon".

# (NEW!) The number-sign (#) matches any English consonant. For example, the query tra#t finds the word "tract" but not "trait".

# (NEW!) The at-sign (@) matches any English vowel. For example, the query abo@t finds the word "about" but not "abort".

# Filter by meaning: Did you know that you can filter your wildcard searches by meaning? Put a colon (:) after your pattern and then type a word or two describing what you're looking for. For example, the query p*:ireland finds terms beginning with "p" that have something to do with Ireland, and the query *:widespread epidemic searches for terms having something to do with "widespread epidemic". The latter case demonstrates how OneLook.com can be used as a means of finding a word (in this case, pandemic) if you only know its definition. See the reverse dictionary page for more details on this feature.


comparison | logical | digit | consonant | vowel | wildcard

all_token = one_token | letter | comparison | logical
