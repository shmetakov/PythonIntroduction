from abc import ABC, abstractmethod


class WearAbstractClass(ABC):

    def __init__(self, size):
        self._size = size

    @abstractmethod
    def result(self):
        pass


class Coat(WearAbstractClass):
    @property
    def result(self):
        return self._size / 6.5 + 0.5


class Costume(WearAbstractClass):
    @property
    def result(self):
        return self._size * 2 + 0.3


coat = Coat(6.5)
costume = Costume(5)
print(coat.result)
print(costume.result)
