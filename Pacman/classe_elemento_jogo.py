from abc import ABCMeta, abstractmethod

class ElementoJogo(metaclass = ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass


    @abstractmethod
    def calcularRegras(self):
        pass


    @abstractmethod
    def processarEventos(self, eventos):
        pass
