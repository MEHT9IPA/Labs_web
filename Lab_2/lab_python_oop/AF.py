import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def Area(self):
        pass