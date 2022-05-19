from celestine.symbol.symbol import Symbol

from celestine.alphabet import SIGN_MARK
from celestine.alphabet import SIGN_STAR
from celestine.alphabet import SIGN_PLUS
from celestine.alphabet import SIGN_DASH
from celestine.alphabet import SIGN_LESS
from celestine.alphabet import SIGN_SAME
from celestine.alphabet import SIGN_MORE


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
