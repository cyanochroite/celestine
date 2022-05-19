from abc import ABC
from abc import abstractmethod


class Token(ABC):
    @property
    @abstractmethod
    def alphabet(item):
        raise NotImplementedError

    @abstractmethod
    def parse(self, array):
        raise NotImplementedError

    def __init__(self, value):
        self.value = value
        #self.value = self.parse(value)

    def __str__(self):
        return str().join(self.alphabet)

    def __repr__(self):
        return str(self.alphabet)

    def parse(cls, value):
        return NotImplementedError
