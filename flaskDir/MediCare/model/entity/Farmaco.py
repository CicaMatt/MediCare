class Farmaco():

    def __init__(self,id,prezzo,nome,categoria, descrizione):
        self.__id=id
        self.__nome=nome
        self.__prezzo=prezzo
        self.__categoria=categoria
        self.__descrizione=descrizione

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getPrezzo(self):
        return self.__prezzo

    def getDescrizione(self):
        return self.__descrizione

    def getCategoria(self):
        return self.__categoria

    def setNome(self,nome):
        self.__nome=nome

    def setPrezzo(self,prezzo):
        self.__prezzo=prezzo

    def setDescrizione(self,descrizione):
        self.__descrizione=descrizione

    def setId(self,id):
        self.__id=id

    def setCategoria(self,categoria):
        self.__categoria=categoria