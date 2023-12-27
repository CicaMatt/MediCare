import Medici

class MedicoPubblico(Medici.Medico):
    def __init__(self,email,password,prenotazioni, nomeReparto,enteSanitario):
        super().__init__(email,password,prenotazioni)
        self.__nomeReparto=nomeReparto
        self.__enteSanitario=enteSanitario

    def getNomeReparto(self):
        return self.__nomeReparto

    def getEnte(self):
        return self.__enteSanitario

    def getEmail(self):
        return self.__email

    def getPrenotazioni(self):
        return self.__prenotazioni

    def getPassword(self):
        return self.__password

    def setNomeReparto(self,reparto):
        self.__nomeReparto=reparto

    def setEnte(self,ente):
        self.__enteSanitario=ente

    def setEmail(self,email):
        self.__email=email

    def setPrenotazioni(self,prenotazioni):
        self.__prenotazioni=prenotazioni

    def setPassword(self,password):
        self.__password=password

    