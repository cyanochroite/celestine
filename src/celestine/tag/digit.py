from celestine.tag.token import Token

from celestine.alphabet import DIGIT_0
from celestine.alphabet import DIGIT_1
from celestine.alphabet import DIGIT_2
from celestine.alphabet import DIGIT_3
from celestine.alphabet import DIGIT_4
from celestine.alphabet import DIGIT_5
from celestine.alphabet import DIGIT_6
from celestine.alphabet import DIGIT_7
from celestine.alphabet import DIGIT_8
from celestine.alphabet import DIGIT_9
from celestine.alphabet import DIGIT_A
from celestine.alphabet import DIGIT_B
from celestine.alphabet import DIGIT_C
from celestine.alphabet import DIGIT_D
from celestine.alphabet import DIGIT_E
from celestine.alphabet import DIGIT_F


class Digit(Token):
    alphabet = frozenset({
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
    })

    def __init__(self, value):
        super().__init__(value)

    def parse(self, array):
        string = str().join(array)
        return int(string, 16)
