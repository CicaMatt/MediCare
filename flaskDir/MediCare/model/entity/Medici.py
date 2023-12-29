from abc import ABC, abstractmethod
class Medico(ABC):
    def __init__(self,email,password,prenotazioni):
        self.email=email
        self.password=password
        self.prenotazioni=prenotazioni
