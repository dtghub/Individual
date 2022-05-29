from abc import ABC, abstractmethod

class DB(ABC):
    def dbConnect(self, filename):
        pass