class FascicoloSanitario():
    id=1
    def __init__(self,paziente,documenti):
        self.paziente = paziente
        self.documents=documenti
        self.id=FascicoloSanitario.id
        FascicoloSanitario.id+=1

