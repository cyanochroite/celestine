from celestine.tag.token import Token
from celestine.tag.operator import operator

from celestine.data.alphabet import Divider

class Tab(Token):
    def __init__(self):
        super().__init__(
            {
                Divider.WHITESPACE
            }
        )

    class _tab(operator):
        def __init__(self):
            super().__init__(
                [
                    Divider.WHITESPACE
                ],
                [
                ]
            )

    @classmethod
    def parse(cls, array):
        return cls.tab

    tab = _tab()


class Word(Token):
    def __init__(self):
        super().__init__(
            {
            }
        )

    class _word(operator):
        def __init__(self, iterable):
            super().__init__(
                [item for item in iterable],
                []
            )

    @classmethod
    def parse(cls, iterable):
        return cls._word(iterable)


class Number(Token):
    def __init__(self):
        super().__init__(
            {
            }
        )

    class _word(operator):
        def __init__(self, iterable):
            super().__init__(
                [item for item in iterable],
                []
            )

    @classmethod
    def parse(cls, iterable):
        return cls._word(iterable)
    
