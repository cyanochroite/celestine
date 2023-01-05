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

from celestine.text.unicode import APOSTROPHE
from celestine.text.unicode import FULL_STOP
from celestine.text.unicode import SPACE

from .type import B
from .type import I
from .type import S
from .type import SELF


class HashMetaClass(type):
    """"""

    def __eq__(cls, other: SELF) -> B:
        """This seems to always be called even on class instances."""
        return str(cls) == str(other)

    def __hash__(cls) -> I:
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

    def __eq__(self, other: SELF) -> B:
        """This might never be called but wont hurt to keep it."""
        return str(self) == str(other)

    def __hash__(self) -> I:
        """"""
        return hash(str(self))

    def __str__(self) -> S:
        """<celestine.session.argument.Argument object at 0x00000000>"""
        string = super().__str__()
        (_, _, after) = string.rpartition(FULL_STOP)
        (before, _, _) = after.partition(SPACE)
        return before
