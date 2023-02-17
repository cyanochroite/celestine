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

from celestine.typed import B
from celestine.typed import S
from celestine.typed import Z
from celestine.typed import SELF

from celestine.unicode import APOSTROPHE
from celestine.unicode import FULL_STOP
from celestine.unicode import SPACE


class HashMetaClass(type):
    """"""

    def __eq__(cls, other: SELF) -> B:
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
