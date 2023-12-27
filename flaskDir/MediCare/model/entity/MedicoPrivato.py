import Medici

class MedicoPrivato(Medici.Medico):
    def __init__(self,email,password,nome,cognome,prenotazioni):
        super().__init__(email,password,prenotazioni)
        self.__nome = nome
        self.__cognome=cognome

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def getPrenotazioni(self):
        return self.__prenotazioni

    def setNome(self,nome):
        self.__nome = nome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password
    
    def setPrenotazioni(self,prenotazioni):
        self.__prenotazioni = prenotazioni