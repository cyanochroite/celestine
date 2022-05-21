from celestine.symbol.symbol import Symbol

from celestine.data.alphabet import SIGN_MARK
from celestine.data.alphabet import SIGN_STAR
from celestine.data.alphabet import SIGN_PLUS
from celestine.data.alphabet import SIGN_DASH
from celestine.data.alphabet import SIGN_LESS
from celestine.data.alphabet import SIGN_SAME
from celestine.data.alphabet import SIGN_MORE


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
