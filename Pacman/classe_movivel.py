from abc import ABCMeta, abstractmethod

class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceitarMovimento(self):
        pass

    
    @abstractmethod
    def recusarMovimento(self, direcoes):
        pass


    @abstractmethod
    def esquina(self, direcoes):
        pass