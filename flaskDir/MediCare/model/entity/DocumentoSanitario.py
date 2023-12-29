class DocumentoSanitario():
    def __init__(self,id,tipo,dataEmissione, descrizione, tit):
        self.__id = id
        self.__tipo = tipo
        self.__dataEmissione =dataEmissione
        self.__descrizione=descrizione
        self.__titolare=tit

    def getId(self):
        return self.__id

    def getTipo(self):
        return self.__tipo

    def getDataEmissione(self):
        return self.__dataEmissione

    def getDescrizione(self):
        return self.__descrizione

    def getTitolare(self):
        return self.__titolare;
    def setTipo(self,tipo):
        self.__tipo=tipo

    def setDataEmissione(self,date):
        self.__dataEmissione=date

    def setDescrizione(self,desc):
        self.__descrizione=desc

    def setTitolare(self,tit):
        self.__titolare =tit