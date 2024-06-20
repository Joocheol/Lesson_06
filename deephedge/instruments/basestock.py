from abc import ABC, abstractmethod

class BaseStock(ABC):

    def __init__(self):
        self.buffer = {}

    @abstractmethod
    def simulate(self):
        pass

    def register_buffer(self, name, buffer):
        self.buffer[name] = buffer

    def get_buffer(self, name): 
        return self.buffer[name]
    
    @property
    def spot(self):
        return self.get_buffer('spot')
    

