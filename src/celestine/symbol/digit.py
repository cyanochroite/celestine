from celestine.symbol.symbol import Symbol

from celestine.data.alphabet import DIGIT_0
from celestine.data.alphabet import DIGIT_1
from celestine.data.alphabet import DIGIT_2
from celestine.data.alphabet import DIGIT_3
from celestine.data.alphabet import DIGIT_4
from celestine.data.alphabet import DIGIT_5
from celestine.data.alphabet import DIGIT_6
from celestine.data.alphabet import DIGIT_7
from celestine.data.alphabet import DIGIT_8
from celestine.data.alphabet import DIGIT_9
from celestine.data.alphabet import DIGIT_A
from celestine.data.alphabet import DIGIT_B
from celestine.data.alphabet import DIGIT_C
from celestine.data.alphabet import DIGIT_D
from celestine.data.alphabet import DIGIT_E
from celestine.data.alphabet import DIGIT_F


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
