from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def desc(self):
        pass

    def __init__(self, dimension):
        self.dimension = dimension
