from abc import ABC
from abc import abstractmethod


class Symbol(ABC):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    @property
    @abstractmethod
    def alphabet(value):
        raise NotImplementedError

    @classmethod
    def contains(cls, value):
        return value in cls.alphabet
