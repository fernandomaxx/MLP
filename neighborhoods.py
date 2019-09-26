from abc import abstractmethod, ABC

class Neighborhoods:
    def __init__(self):
        pass

class Neighborhood(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, args):
        pass
