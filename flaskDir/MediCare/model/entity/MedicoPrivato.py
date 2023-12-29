import Medici

class MedicoPrivato(Medici.Medico):
    def __init__(self,email,password,nome,cognome,prenotazioni):
        super().__init__(email,password,prenotazioni)
        self.nome = nome
        self.cognome=cognome
