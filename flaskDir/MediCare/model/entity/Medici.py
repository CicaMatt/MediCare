from abc import ABC, abstractmethod
class Medico(ABC):
    def __init__(self,email,password,prenotazioni):
        self.__email=email
        self.__password=password
        self.__prenotazioni=prenotazioni

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def getPassword(self):
        pass
    @abstractmethod
    def getPrenotazioni(self):
        pass

    def setEmail(self,email):
        pass

    def setPassword(self,password):
        pass

    def setPrenotazioni(self,prenotazioni):
        pass
