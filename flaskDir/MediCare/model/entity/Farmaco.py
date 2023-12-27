class Farmaco():
    id=1
    def __init__(self,nome,prezzo,descrizione):
        self.__id=Farmaco.id
        Farmaco.id+=1
        self.__nome=nome
        self.__prezzo=prezzo
        self.__descrizione=descrizione

    def getNome(self):
        return self.__nome

    def getPrezzo(self):
        return self

    def getDescrizione(self):
        return self.__descrizione

    def setNome(self,nome):
        self.__nome=nome

    def setPrezzo(self,prezzo):
        self.__prezzo=prezzo

    def setDescrizione(self,descrizione):
        self.__descrizione=descrizione

