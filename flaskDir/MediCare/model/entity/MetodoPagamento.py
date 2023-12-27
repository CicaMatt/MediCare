class MetodoPagamento:
    def __init__(self,CVV,PAN,titolare,beneficiario):
        self.__CVV=CVV
        self.__PAN=PAN
        self.__titolare=titolare
        self.__beneficiario=beneficiario

    def getCVV(self):
        return self.__CVV

    def getPAN(self):
        return self.__PAN

    def getTitolare(self):
        return self.__titolare

    def getBeneficiario(self):
        return self.__beneficiario

    def setCVV(self,CVV):
        self.__CVV=CVV

    def setPAN(self,pan):
        self.__PAN=pan

    def setTitolare(self,titolare):
        self.__titolare = titolare

    def setBeneficiario(self,beneficiario):
        self.__beneficiario = beneficiario
