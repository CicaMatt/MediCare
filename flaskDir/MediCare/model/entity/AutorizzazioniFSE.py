class AutorizzazioniFSE:
    def __init__(self,medico,fseConcesso):
        self.__authorize=medico
        self.__fse=fseConcesso

    def autorizzazioniFSE(self):
        return self.__authorize

    def fseConcesso(self):
        return self.__fse

    def setAutorizzazioniFSE(self,med):
        self.authorizzazioniFSE = med

    def setFseConcesso(self,fse):
        self.__fse = fse