"""
Make it so class objects and class instances map to the same slot in a
dictionary. Essentially this is just a weird fancy Enum.

dictionary = {}

class Test(HashClass):
    pass

instance = Test()

dictionary[instance] = "test"
print(dictionary[Test]) -> "test"
"""


from celestine.typed import (
    O,
    B,
    S,
    Z,
)
from celestine.unicode import (
    APOSTROPHE,
    FULL_STOP,
    SPACE,
)


class HashMetaClass(type):
    """"""

    def __eq__(cls, other: O) -> B:
        return str(cls) == str(other)

    def __hash__(cls) -> Z:
        """"""
        return hash(str(cls))

    def __str__(cls) -> S:
        """<class 'celestine.session.argument.Argument'>"""
        string = super().__str__()
        (_, _, after) = string.rpartition(FULL_STOP)
        (before, _, _) = after.partition(APOSTROPHE)
        return before


class HashClass(metaclass=HashMetaClass):
    """"""

    def __hash__(self) -> Z:
        """"""
        return hash(str(self))

    def __str__(self) -> S:
        """<celestine.session.argument.Argument object at 0x00000000>"""
        string = super().__str__()
        (_, _, after) = string.rpartition(FULL_STOP)
        (before, _, _) = after.partition(SPACE)
        return before
