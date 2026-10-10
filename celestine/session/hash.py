"""
A custom hash function for special classes.

Make it so class objects and class instances map to the same slot in a
dictionary. Essentially this is just a weird fancy Enum.

dictionary = {}

class Test(HashClass):
    pass

instance = Test()

dictionary[instance] = "test"
print(dictionary[Test]) -> "test"
"""

from celestine.literal import (
    APOSTROPHE,
    FULL_STOP,
    SPACE,
)
from celestine.typed import (
    B,
    J,
    S,
    Z,
    ignore,
)


class HashMetaClass(type):
    """"""

    def __eq__(cls, other: J) -> B:
        return str(cls) == str(other)

    def __hash__(cls) -> Z:
        """"""
        return hash(str(cls))

    def __str__(cls) -> S:
        """
        Build the string representation.

        <class 'celestine.session.argument.Argument'>
        """
        ignore(cls)
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
        """
        Build the string representation.

        <celestine.session.argument.Argument object at 0x00000000>
        """
        ignore(self)
        string = super().__str__()
        (_, _, after) = string.rpartition(FULL_STOP)
        (before, _, _) = after.partition(SPACE)
        return before
