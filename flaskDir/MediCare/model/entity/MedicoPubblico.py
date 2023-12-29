import Medici

class MedicoPubblico(Medici.Medico):
    def __init__(self,email,password,prenotazioni, nomeReparto,enteSanitario):
        super().__init__(email,password,prenotazioni)
        self.nomeReparto=nomeReparto
        self.enteSanitario=enteSanitario

