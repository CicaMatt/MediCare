class FascicoloSanitario():
    id=1
    def __init__(self,paziente,documenti):
        self.__paziente = paziente
        self.__documents=documenti
        self.__id=FascicoloSanitario.id
        FascicoloSanitario.id+=1

    def getPaziente(self):
        return self.__paziente

    def getDocumenti(self):
        return self.__documents

    def getId(self):
        return self.__id

    def setPaziente(self,paziente):
        self.__paziente = paziente

    def setDocumenti(self,documenti):
        self.__documents = documenti