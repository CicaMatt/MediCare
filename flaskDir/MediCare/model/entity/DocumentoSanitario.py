class DocumentoSanitario():
    def __init__(self,id,tipo,dataEmissione):
        self.__id = id
        self.__tipo = tipo
        self.__dataEmissione =dataEmissione

    def getId(self):
        return self.__id

    def getTipo(self):
        return self

    def getDataEmissione(self):
        return self.__dataEmissione

    def setTipo(self,tipo):
        self.__tipo=tipo

    def setDataEmissione(self,date):
        self.__dataEmissione=date